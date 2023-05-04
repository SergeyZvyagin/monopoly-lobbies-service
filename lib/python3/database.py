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
    

    def getFullLobbyInfo(self, lobby_id: int) -> tuple:
        self.cursor.execute('''SELECT name, owner_id, lobby_type, password, max_players, 
                                      time_for_turn, victory_type, score_victory_value, 
                                      turn_victory_value, is_running, game_address, game_port
                               FROM lobbies WHERE id = %d;''', (lobby_id))
        return self.cursor.fetchone()

    
    def raiseUserToLobbyOwner(self, user_id, lobby_id):
        self.cursor.execute("UPDATE lobbies SET owner_id = %d WHERE id = %d;", (user_id, lobby_id))
        self.conn.commit()

    
    def deleteLobby(self, lobby_id: int):
        self.cursor.execute(f'DELETE FROM lobbies WHERE id = {lobby_id};')
        self.conn.commit()


    def findNewOwnerOrDeleteLobby(self, lobby_id: int):
        self.cursor.execute(f'SELECT player_id FROM players_in_lobbies WHERE lobby_id = {lobby_id};')
        row = self.cursor.fetchall()
        if row:
            self.raiseUserToLobbyOwner(row[0], lobby_id)
        else:
            self.deleteLobby(lobby_id)


    def disconnectUser(self, user_id: int):
        self.cursor.execute(f'DELETE FROM players_in_lobbies WHERE player_id = {user_id} RETURNING lobby_id;')
        lobby_id = self.cursor.fetchone()[0]
        self.conn.commit()
        
        _, lobby_owner_id, *_ = self.getFullLobbyInfo(lobby_id)
        if user_id == lobby_owner_id:
            self.findNewOwnerOrDeleteLobby(lobby_id)

   
    def connectUserToLobby(self, user_id int, lobby_id: int):
        try:
            self.disconnectUser(user_id)
        except:
            pass
        self.cursor.execute(f'INSERT INTO players_in_lobbies (player_id, lobby_id) VALUES ({user_id}, {lobby_id});'
        self.conn.commit()


    def createLobby(self, owner_id: int, settings: dict = None) -> (int, dict):
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
    
        self.cursor.execute(f'INSERT INTO lobbies ({variables}) VALUES ({values}) RETURNING *;')
        lobby_info = self.cursor.fetchone()[0]
        self.conn.commit()

        applied_settings = dict()
        lobby_id = lobby_info[0]
        applied_settings["name"] = lobby_info[2].replace("''", "'")
        applied_settings["type"] = lobby_info[3]
        applied_settings["password"] = lobby_info[4].replace("''", "'")
        applied_settings["maxPlayers"] = lobby_info[5]
        applied_settings["timeForTurn"] = lobby_info[6]
        applied_settings["victoryType"] = lobby_info[7]
        applied_settings["scoreVictoryValue"] = lobby_info[8]
        applied_settings["turnVictoryValue"] = lobby_info[9]

        return lobby_id, applied_settings
