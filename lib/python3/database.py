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

    
    def getUserInfoByID(self, id: int) -> tuple:
        self.cursor.execute('SELECT nickname, is_guest, rating FROM users WHERE id=%d' % int(id))
        return self.cursor.fetchone()
    

    def findNewOwnerOrDeleteLobby(self, lobby: int):
        pass
    

    def disconnectUserReturningLobbyID(self, user_id: int) -> int:
        pass

   
    def connectUserToLobby(self, user_id int, lobby_id: int):
        try:
            self.findNewOwnerOrDeleteLobby(self.disconnectUserReturningLobbyID(user_id))
        except:
            pass
        self.cursor.execute(f'INSERT INTO players_in_lobbies (i) VALUES (%d, %d);')
        user_id = self.cursor.fetchone()[0]
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


    def createUserAndReturnID(self, nickname: str, vk_id:int=None) -> int:
        vk_id = int(vk_id)
        variables = 'nickname' + (', vk_id, is_guest' if vk_id else '')
        values = f"'{nickname}'" + ('' if not vk_id else f', {vk_id}, false')

        self.cursor.execute(f'INSERT INTO users ({variables}) VALUES ({values}) RETURNING id;')
        user_id = self.cursor.fetchone()[0]
        self.conn.commit()
        
        return user_id
    
    def changeNickname(self, user_id: int, nickname: str):
        user_id = int(user_id)
        nickname = nickname.replace("'", '"')
        if len(nickname) > 16:
            nickname = nickname[:16]
        self.cursor.execute(f"UPDATE users SET nickname='{nickname}' WHERE id={user_id};")
        self.conn.commit()

    
