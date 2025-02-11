import discord

class PaginationTextView(discord.ui.View):
    """A reusable pagination view for long text content."""
    
    def __init__(self, content: list[str], timeout: int = 60):
        """Initialize the pagination view with a list of text content."""
        super().__init__(timeout=timeout)
        self.content = content  # A list of strings (text content)
        self.current_page = 0
        self.update_buttons()

    def update_buttons(self):
        """Updates the button states based on the current page index."""
        self.previous_page.disabled = self.current_page == 0
        self.next_page.disabled = self.current_page == len(self.content) - 1

    async def update_message(self, interaction: discord.Interaction):
        """Edits the message to show the current page content and update buttons."""
        self.update_buttons()
        text = self.content[self.current_page]
        # Send the current page text content in the message.
        await interaction.response.edit_message(content=text, view=self)

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

    async def on_timeout(self):
        """Called when the pagination times out (e.g., after 60 seconds)."""
        for button in self.children:
            button.disabled = True  # Disable all buttons
        await self.message.edit(content="This pagination has expired.", view=self)