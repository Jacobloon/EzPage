# ezpage

A simple and efficient Python library for creating pagination in Discord bots using `discord.py`. `ezpage` makes it easy to handle multi-page embeds with navigation buttons.

## Features

- Simple and clean API for pagination.
- Uses `discord.ui.View` for interactive navigation.
- Automatically enables/disables buttons based on the current page.
- Works seamlessly with `discord.ext.commands` and `discord.app_commands`.
- Customizable timeout and behavior.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- `discord.py` version 2.0 or later

### Install via pip

```bash
pip install ezpage
```

## Usage

### Basic Example

Here's how you can use `ezpage` to create paginated embeds in your bot:

```python
import discord
from discord.ext import commands
from ezpage import PaginationView

bot = commands.Bot(command_prefix="!")

@bot.command()
async def help(ctx):
    embeds = [
        discord.Embed(title="Help - Page 1", description="This is the first page."),
        discord.Embed(title="Help - Page 2", description="This is the second page."),
        discord.Embed(title="Help - Page 3", description="This is the third page.")
    ]
    view = PaginationView(embeds)
    await ctx.send(embed=embeds[0], view=view)

bot.run("YOUR_BOT_TOKEN")
```

### Using with Slash Commands

If you are using `discord.app_commands`, you can use pagination like this:

```python
import discord
from discord import app_commands
from discord.ext import commands
from ezpage import PaginationView

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Show the help menu with pagination.")
    async def help(self, interaction: discord.Interaction):
        embeds = [
            discord.Embed(title="Help - Page 1", description="This is the first page."),
            discord.Embed(title="Help - Page 2", description="This is the second page."),
            discord.Embed(title="Help - Page 3", description="This is the third page.")
        ]
        view = PaginationView(embeds)
        await interaction.response.send_message(embed=embeds[0], view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Help(bot))
```

## Or Embeds With Multiple Fields
```python
import discord
from discord.ext import commands
from pagination import PaginationView

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        embeds = []

        # Splitting embeds into multiple pages
        embed1 = discord.Embed(title="Help - Page 1", description="General Commands", color=discord.Color.blue())
        embed1.add_field(name="`/balance`", value="Check your balance", inline=False)
        embed1.add_field(name="`/shop`", value="View the shop", inline=False)
        embeds.append(embed1)

        embed2 = discord.Embed(title="Help - Page 2", description="Economy Commands", color=discord.Color.green())
        embed2.add_field(name="`/work`", value="Earn money by working", inline=False)
        embed2.add_field(name="`/gamble`", value="Try your luck at gambling", inline=False)
        embeds.append(embed2)

        embed3 = discord.Embed(title="Help - Page 3", description="Business Commands", color=discord.Color.purple())
        embed3.add_field(name="`/startbusiness`", value="Start your own business", inline=False)
        embed3.add_field(name="`/apply`", value="Apply for a job", inline=False)
        embeds.append(embed3)

        view = PaginationView(embeds)
        await ctx.send(embed=embeds[0], view=view)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
```

## Customization

### Change Timeout
By default, `PaginationView` times out after 60 seconds. You can change this by passing `timeout` as an argument:

```python
view = PaginationView(embeds, timeout=120)  # 120 seconds timeout
```

### Custom Buttons
You can override the button behavior by subclassing `PaginationView`:

```python
class CustomPaginationView(PaginationView):
    @discord.ui.button(emoji="⏮️", style=discord.ButtonStyle.blurple)
    async def first_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page = 0
        await self.update_message(interaction)
```

## License
This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests on GitHub.

Enjoy using `ezpage` to simplify your Discord bot pagination! 🚀