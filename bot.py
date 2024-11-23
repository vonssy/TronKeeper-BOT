import requests
import json
import os
from colorama import *
from datetime import datetime
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class TronKeeper:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'bot-api.tronkeeper.app',
            'Origin': 'https://bot.tronkeeper.app',
            'Pragma': 'no-cache',
            'Referer': 'https://bot.tronkeeper.app/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Tron Keeper - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def user_login(self, query: str):
        url = 'https://bot-api.tronkeeper.app/bot/auth'
        data = json.dumps({"data":query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']['token']
            else:
                return None
        else:
            return None

    def user_profile(self, token: str):
        url = 'https://bot-api.tronkeeper.app/bot/profile'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']
            else:
                return None
        else:
            return None

    def user_verify(self, token: str):
        url = 'https://bot-api.tronkeeper.app/bot/verify'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']
            else:
                return None
        else:
            return None
        
    def hold_usdt(self, token: str):
        url = 'https://bot-api.tronkeeper.app/daily/hold'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']
            else:
                return None
        else:
            return None
        
    def check_ton(self, token: str):
        url = 'https://bot-api.tronkeeper.app/ton/check-hold'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']['ton']
            else:
                return None
        else:
            return None
        
    def hold_ton(self, token: str):
        url = 'https://bot-api.tronkeeper.app/ton/hold'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']
            else:
                return None
        else:
            return None
        
    def check_tonarx(self, token: str):
        url = 'https://bot-api.tronkeeper.app/tonarx/check-hold'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']['limit']
            else:
                return None
        else:
            return None
        
    def hold_tonarx(self, token: str):
        url = 'https://bot-api.tronkeeper.app/tonarx/hold'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']
            else:
                return None
        else:
            return None
        
    def complete_tasks(self, token: str, task_id: int):
        url = 'https://bot-api.tronkeeper.app/bot/tasks'
        data = json.dumps({'id':task_id, 'code':''})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code == 200:
            if result and result['success']:
                return result['data']
            else:
                return None
        else:
            return None

    def process_query(self, query: str):
        token = self.user_login(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query May Expired {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if token:
            user = self.user_profile(token)
            wallet = user.get('wallet') if user else None
            if not wallet:
                verify = self.user_verify(token)
                if not verify:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {user['user']['fullName']} {Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT}Isn't Verified{Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Subscribe Tron Keeper Channel First {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    return
                
                wallet = verify.get('wallet')

                if wallet:
                    user = self.user_profile(token)

            if wallet and user:
                usdt = wallet.get('USDT', {}).get('balance', 0)
                tonarx = wallet.get('TONARX', {}).get('balance', 0)
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['user']['fullName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {usdt} $USDT {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {tonarx} $TONARX {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                hold_count = user['hold']
                if hold_count > 0:
                    while hold_count > 0:
                        hold = self.hold_usdt(token)
                        if hold:
                            hold_count = hold['limit']
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} USDT {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['USDT']} $USDT {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Chance{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {hold_count} Left {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            break

                        time.sleep(1)

                    if hold_count == 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} USDT {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}No Avaialable Chance{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} USDT {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}No Avaialable Chance{Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                ton = self.check_ton(token)
                if ton:
                    hold_count = ton['count']
                    if hold_count > 0:
                        while hold_count > 0:
                            hold = self.hold_ton(token)
                            if hold:
                                hold_count = hold['ton']['count']
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} TON {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Chance{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {hold_count} Left {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['Blum']} $BLUM {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['Paws']} $PAWS {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['Major']} $MAJOR {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['Moonbix']} $MOONBIX {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['NotPixel']} $NPX {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                break

                            time.sleep(1)

                        if hold_count == 0:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} TON {Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT}No Avaialable Chance{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} TON {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}No Avaialable Chance{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} TON {Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT}Data Is None{Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                hold_count = self.check_tonarx(token)
                if hold_count > 0:
                    while hold_count > 0:
                        hold = self.hold_tonarx(token)
                        if hold:
                            hold_count = hold['limit']
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} TONARX {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {hold['prize']['TONARX']} $TONARX {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Chance{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {hold_count} Left {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            break

                        time.sleep(1)

                    if hold_count == 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} TONARX {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}No Avaialable Chance{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Hold{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} TONARX {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}No Avaialable Chance{Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                tasks = user['tasks']
                user_task_ids = user['userTask']
                if tasks:
                    pending_tasks = [
                        task for task in tasks if task['id'] not in user_task_ids
                    ]

                    for task in pending_tasks:
                        task_id = task['id']

                        if task:
                            complete = self.complete_tasks(token, task_id)
                            if complete:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['reward']['USDT']} $USDT {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Tron Keeper - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = TronKeeper()
    bot.main()