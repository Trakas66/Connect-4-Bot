import discord
from discord import app_commands
import random
import json

with open("key.txt", 'r') as file:
    token = file.read()


# Classes
class aClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'We have logged in as {self.user}')


class JoinMenu(discord.ui.View):

    p1 = 0
    p2 = 0

    def __init__(self, p1):
        super().__init__()
        self.value = None
        self.p1 = p1
    
    @discord.ui.button(label="Join Game", style=discord.ButtonStyle.green)
    async def joinMenu(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.p1:
            await interaction.response.send_message("You can't join your own game!", ephemeral=True)
            return
        self.p2 = interaction.user
        start = StartC4Menu([self.p1, self.p2])
        embed = C4StartEmbed(start.players)
        await interaction.response.edit_message(embed=embed, view=start)


class StartC4Menu(discord.ui.View):

    players = []

    def __init__(self, players):
        super().__init__()
        self.players = players

    @discord.ui.button(label='Start Game', style=discord.ButtonStyle.green)
    async def startGame(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.players[0]:
            await interaction.response.send_message('Only the creator can start the game!', ephemeral=True)
            return
        game = Connect4Game(self.players)
        embed = C4Embed(self.players[0], game.board)
        await interaction.response.edit_message(embed=embed, view=game)


class Connect4Game(discord.ui.View):

    players = []
    board = []
    turn = 0

    def __init__(self, players):
        super().__init__()
        self.players = players
        self.board = C4InitBoard()
        self.turn = 0

    def changeTurn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def processTurn(self, interaction: discord.Interaction):
        if checkWin(self.board, self.turn):
            return True
        else:
            return False

    @discord.ui.button(label='1', style=discord.ButtonStyle.grey)
    async def button1(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 0)
        if row == 0:
            button.disabled = True
        self.board[row][0] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label='2', style=discord.ButtonStyle.grey)
    async def button2(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 1)
        if row == 0:
            button.disabled = True
        self.board[row][1] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label='3', style=discord.ButtonStyle.grey)
    async def button3(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 2)
        if row == 0:
            button.disabled = True
        self.board[row][2] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label='4', style=discord.ButtonStyle.grey)
    async def button4(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 3)
        if row == 0:
            button.disabled = True
        self.board[row][3] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label='5', style=discord.ButtonStyle.grey)
    async def button5(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 4)
        if row == 0:
            button.disabled = True
        self.board[row][4] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label='6', style=discord.ButtonStyle.grey)
    async def button6(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 5)
        if row == 0:
            button.disabled = True
        self.board[row][5] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label='7', style=discord.ButtonStyle.grey)
    async def button7(self, interaction: discord.Interaction, button: discord.Button):
        if interaction.user not in self.players:
            await interaction.response.send_message('You are not in this game!', ephemeral=True)
            return
        if interaction.user != self.players[self.turn]:
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            return
        row = GetNextLocation(self.board, 6)
        if row == 0:
            button.disabled = True
        self.board[row][6] = self.turn + 1
        if not self.processTurn(interaction):
            self.changeTurn()
            embed = C4Embed(self.players[self.turn], self.board)
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = C4Embed(self.players[self.turn], self.board, self.turn + 1)
            await interaction.response.edit_message(embed=embed, view=None)


client = aClient()
tree = app_commands.CommandTree(client)


# Commands
@tree.command(name = 'play', description = 'Plays game')
async def play(interaction: discord.Interaction):
    try:
        file = open(f'{interaction.guild_id}.txt', 'r')
    except:
        file = open(f'{interaction.guild_id}.txt', 'w')
        data = {}
        for user in interaction.guild.members:
            data[user.id] = {'money': 0}
        file.write(json.dumps(data))
        file.close()
        file = open(f'{interaction.guild_id}.txt', 'r')

    data = json.loads(file.read())
    file.close()

    file = open(f'{interaction.guild_id}.txt', 'w')
    userId = str(interaction.user.id)
    amount = 10

    data[userId]['money'] += amount

    file.write((json.dumps(data)))
    file.close()

    await interaction.response.send_message(embed=playEmbed(interaction, data, userId, amount))


@tree.command(name = 'coinflip', description = 'Flips a coin for money')
async def coinflip(interaction: discord.Interaction, selection: str, amount: int):
    userId = str(interaction.user.id)
    serverId = str(interaction.guild_id)

    with open(f'{serverId}.txt', 'r') as file:
        data = json.loads(file.read())

    if amount > data[userId]['money']:
        await interaction.response.send_message("You don't have enough money!")
        return

    if amount < 0:
        await interaction.response.send_message("You can't flip for a negative number!")
        return

    p = ['heads', 'tails']
    if selection.lower() not in p:
        await interaction.response.send_message("Invalid selection! Please choose heads or tails")
        return

    choice = random.choice(p)
    if choice == selection.lower():
        data[userId]['money'] += amount
    else:
        data[userId]['money'] -= amount

    await interaction.response.send_message(embed=flipEmbed(interaction, selection, data, choice, userId))

    with open(f'{serverId}.txt', 'w') as file:
        file.write(json.dumps(data))


@tree.command(name='connect4', description='Starts a game of connect4')
async def challenge(interaction: discord.Interaction):
    view = JoinMenu(interaction.user)
    await interaction.response.send_message(embed=challengeEmbed(interaction), view=view)


'''@tree.command(name='test', description='Tests embed')
async def test(interaction: discord.Interaction):
    embed = C4Embed(interaction.user, [[2 for j in range(7)] for i in range(7)])
    await interaction.response.send_message(embed=embed)'''


# Embeds
def playEmbed(interaction, data, userId, amount):
    embed = discord.Embed(color=0x0be524, title='Game')
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
    embed.add_field(name='You earned:', value=f'${amount}')
    embed.add_field(name='Money:', value=data[userId]['money'])
    return embed


def flipEmbed(interaction, selection, data, choice, userId):
    embed = discord.Embed()
    embed.color = 0x0be524
    embed.title = 'Coinflip'
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
    embed.add_field(name='You chose:', value=selection.lower())
    embed.add_field(name='The result was:', value=choice)
    embed.add_field(name='Money:', value=data[userId]['money'], inline=False)
    return embed


def challengeEmbed(interaction, player2 = None):
    embed = discord.Embed(color=discord.Color.red(), title='Connect4')
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
    embed.add_field(name=interaction.user.name, value='wants to play connect4')
    if(player2 != None):
        embed.add_field(name=player2.name, value='joined the game')
    return embed


def C4StartEmbed(players):
    embed = discord.Embed(color=discord.Color.red(), title='Connect4')
    embed.add_field(name='Player 1:  ', value=players[0].name)
    embed.add_field(name='Player 2:', value=players[1].name)
    return embed


def C4Embed(player, board, win=0):
    red = ':red_circle:'
    blue = ':blue_circle:'
    white = ':white_circle:'
    embed = discord.Embed(color=discord.Color.red(), title='Connect4')
    embed.set_author(name=player.name, icon_url=player.avatar.url)
    string = ''
    for i in range(7):
        for j in range(7):
            if board[i][j] == 0:
                string += white
            elif board[i][j] == 1:
                string += red
            else:
                string += blue
        string += '\n'
    string += '-1---2--3--4--5--6--7-'
    embed.add_field(name='Board:', value=string)
    if win != 0:
        embed.add_field(name=player.name, value='wins!')
    return embed


# Connect4 funcs
def C4InitBoard():
    board = [[0 for j in range(7)] for i in range(7)]
    return board


def GetNextLocation(board, col):  # returns empty place closest to bottom
    bottom = None
    for i in range(7):
        if board[i][col] == 0:
            bottom = i
    return bottom


def checkWin(board, turn):
    num = turn + 1
    for i in range(7):
        for j in range(7):
            if board[i][j] == num:
                if checkWinHor(board, i, j):
                    return True
                if checkWinVer(board, i, j):
                    return True
                if checkWinDia(board, i, j):
                    return True
    return False


def checkWinHor(board, x, y):
    num = board[x][y]
    if x-3 >= 0:
        if board[x-3][y] == num and board[x-2][y] == num and board[x-1][y] == num:
            return True
    return False


def checkWinVer(board, x, y):
    num = board[x][y]
    if y-3 >= 0:
        if board[x][y-3] == num and board[x][y-2] == num and board[x][y-1] == num:
            return True
    return False


def checkWinDia(board, x, y):
    num = board[x][y]
    if y-3 >= 0:
        if x-3 >= 0:
            if board[x-3][y-3] == num and board[x-2][y-2] == num and board[x-1][y-1] == num:
                return True
        if x+3 <= 6:
            if board[x+3][y-3] == num and board[x+2][y-2] == num and board[x+1][y-1] == num:
                return True
    return False


client.run(token)
