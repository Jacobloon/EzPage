import discord

class PaginationEmbedView(discord.ui.View):
    """A reusable pagination view for Discord embeds."""

    def __init__(self, embeds: list[discord.Embed], timeout: int = 60):
        """Initialize the pagination view with a list of embeds."""
        super().__init__(timeout=timeout)
        self.embeds = embeds
        self.current_page = 0
        self.update_buttons()

    def update_buttons(self):
        """Updates the button states based on the current page index."""
        self.previous_page.disabled = self.current_page == 0
        self.next_page.disabled = self.current_page == len(self.embeds) - 1

    async def update_message(self, interaction: discord.Interaction):
        """Edits the message to show the current embed and update buttons."""
        self.update_buttons()
        embed = self.embeds[self.current_page]
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="⬅️", style=discord.ButtonStyle.blurple, disabled=True)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Go to the previous page."""
        self.current_page -= 1
        await self.update_message(interaction)

    @discord.ui.button(emoji="➡️", style=discord.ButtonStyle.blurple)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Go to the next page."""
        self.current_page += 1
        await self.update_message(interaction)