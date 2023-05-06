import psycopg2

class DatabaseManager:
    def __init__(self, logger, **kwargs):
        self.logger = logger

        self.conn = psycopg2.connect(
                dbname=kwargs['db_name'],
                user=kwargs['db_user'],
                password=kwargs['db_pass'], 
                host=kwargs['db_host'],
                port=kwargs['db_port']
        )
        
        self.cursor = self.conn.cursor()

    
    def getUserInfoByID(self, user_id: int) -> tuple:
        self.cursor.execute('SELECT nickname, is_guest, rating FROM users WHERE id=%d;' % int(user_id))
        return self.cursor.fetchone()
    

    def getLobbyIDbyUserID(self, user_id: int) -> int:
        self.cursor.execute(f'SELECT lobby_id FROM players_in_lobbies WHERE player_id = {user_id};')
        row = self.cursor.fetchone()
        return None if not row else row[0]
        

    def getList(self) -> tuple:
        self.cursor.execute('''SELECT l.id, l.name, l.lobby_type, 
                                      l.max_players, count(pil.player_id) 
                               FROM lobbies AS l 
                               LEFT JOIN players_in_lobbies AS pil 
                               ON l.id = pil.lobby_id 
                               WHERE l.lobby_type < 3 and pil.player_state < 3 
                               GROUP BY l.id;''')
        return self.cursor.fetchall()


    def getFullLobbyInfo(self, lobby_id: int) -> tuple:
        self.cursor.execute(f'''SELECT owner_id, name, lobby_type, password, max_players, 
                                      time_for_turn, victory_type, score_victory_value, 
                                      turn_victory_value, is_running, game_address, game_port
                                FROM lobbies WHERE id = {lobby_id};''')
        return self.cursor.fetchone()

    
    def raiseUserToLobbyOwner(self, user_id: int, lobby_id: int):
        self.cursor.execute("UPDATE lobbies SET owner_id = %d WHERE id = %d;", (user_id, lobby_id))
        self.conn.commit()

    
    def deleteLobby(self, lobby_id: int):
        self.cursor.execute(f'DELETE FROM lobbies WHERE id = {lobby_id};')
        self.conn.commit()

    
    def getActivePlayersInLobby(self, lobby_id: int) -> tuple:
        self.cursor.execute(f'''SELECT u.id, u.nickname, u.is_guest, u.rating, 
                                       pil.player_state 
                                FROM players_in_lobbies AS pil 
                                LEFT JOIN users AS u 
                                ON pil.player_id = u.id 
                                WHERE pil.lobby_id={lobby_id} AND pil.player_state < 3;''')
        return self.cursor.fetchall()


    def findNewOwnerOrDeleteLobby(self, lobby_id: int):
        self.cursor.execute(f'SELECT player_id FROM players_in_lobbies WHERE lobby_id = {lobby_id};')
        row = self.cursor.fetchone()
        if row:
            self.raiseUserToLobbyOwner(row[0], lobby_id)
        else:
            self.deleteLobby(lobby_id)


    def disconnectUser(self, user_id: int):
        self.cursor.execute(f'DELETE FROM players_in_lobbies WHERE player_id = {user_id} RETURNING lobby_id;')
        row = self.cursor.fetchone()
        self.conn.commit()
        
        if row:
            lobby_id = row[0] 
            lobby_owner_id, *_ = self.getFullLobbyInfo(lobby_id)
            if user_id == lobby_owner_id:
                self.findNewOwnerOrDeleteLobby(lobby_id)

   
    def connectUserToLobby(self, user_id: int, lobby_id: int):
        self.disconnectUser(user_id)
        self.cursor.execute(f'INSERT INTO players_in_lobbies (player_id, lobby_id) VALUES ({user_id}, {lobby_id});')
        self.conn.commit()


    def createLobby(self, owner_id: int, settings: dict = None) -> int:
        variables = 'name, owner_id' + ('' if not settings else ', lobby_type, password, max_players, time_for_turn, victory_type, score_victory_value, turn_victory_value')
        
        if not settings:
            values = "'%s''s lobby', %d" % (self.getUserInfoByID(owner_id)[0].replace("'", "''"), owner_id)
        else:
            values = "'%s', %d, %d, '%s', %d, %d, %d, %d, %d" % (settings["name"].replace("'", "''"),
                                                                 owner_id,
                                                                 settings["type"],
                                                                 settings["password"].replace("'", "''"),
                                                                 settings["maxPlayers"],
                                                                 settings["timeForTurn"],
                                                                 settings["victoryType"],
                                                                 settings["scoreVictoryValue"],
                                                                 settings["turnVictoryValue"]
                                                                 )
    
        self.cursor.execute(f'INSERT INTO lobbies ({variables}) VALUES ({values}) RETURNING id;')
        lobby_id = self.cursor.fetchone()[0]
        self.conn.commit() 

        return lobby_id
