<h1 align="center">Sword Masters Sniper</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v1.0.0-purple.svg?cacheSeconds=2592000" />
</p>

Sword Masters Sniper is a powerful tool designed to help you find trade lobbies with a low number of players in the popular MMO game [Sword Masters](https://swordmasters.io) by [emolingo games](https://emolingo.games). It also includes a convenient account generation feature, ensuring a smooth and hassle-free sniping experience.

### Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Todo](#todo)
- [Disclaimer](#disclaimer)

# Features
- Create accounts
- Snipe trade lobbies
  - Provides the room ID along with join link
    - Saves to file and prints to console
  - Snipes by a minimum limit of players per lobby

# Setup
Clone the repo and install the requirements.
```bash
git clone https://github.com/NoobToolzz/Sword-Masters-Sniper.git
cd Sword-Masters-Sniper
pip install -r requirements.txt
```

Next, open `config.json` and set `clients` to your desired amount of minimum players in a lobby (Default is 5).

If you want, place accounts inside of `data/accounts.txt`. Supported formats are listed below:
- Tokens (e.g. `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`)
- Account combos (e.g. `username:password`)

**Note:** This step isn't necessary, as the account generation feature places tokens inside `accounts.txt` for you.

### Example
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZEEXCEERqweawesTIxODQwwcaWfsJhbmRvbSI6IjQ1YmRkODA4LTIxYjgtNDIzMC1iOGY1LTA3MmEWerdDSwNyIsImlhdCSdecaZE4NH0.aFvdy4EAsE-X...
bob:supersecretpassword
```

Start `main.py` and navigate through the menu to begin sniping!
```
python3 main.py
```

## Todo
- [ ] Full lobby sniping
- [ ] Automatic joining on main account (toggleable)
  - This will require a Chromium instance within the root folder, which might be auto-extracted depending on implementation. 
  - Could implement a method to grab your account token via logging in the Chromium instance, instead of you having to capture it yourself.
- [ ] Error handling (it's yucky rn, sorry!)

## Disclaimer

This project and its owner ([@NoobToolzz](https://github.com/NoobToolzz)) are not affiliated with [Sword Masters](https://swordmasters.io) or [emolingo games](https://emolingo.games). The owner disclaims any liability for any consequences, including but not limited to, actions taken against you, your account(s), or your IP address, resulting from the use of this project. You use this project at your own risk and are solely responsible for any outcomes.