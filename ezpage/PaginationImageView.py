import discord

class ImagePaginationView(discord.ui.View):
    """A reusable pagination view for images"""

    def __init__(self, images: list[str], timeout: int = 60):
        super().__init__(timeout=timeout)
        self.images = images
        self.current_page = 0
        self.update_buttons()

    def update_buttons(self):
        self.previous_page.disabled = self.current_page == 0
        self.next_page.disabled = self.current_page == len(self.images) - 1

    async def update_message(self, interaction: discord.Interaction):
        self.update_buttons()
        image_url = self.images[self.current_page]
        embed = discord.Embed()
        embed.set_image(url=image_url)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="⬅️", style=discord.ButtonStyle.blurple, disabled=True)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page -= 1
        await self.update_message(interaction)

    @discord.ui.button(emoji="➡️", style=discord.ButtonStyle.blurple)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page += 1
        await self.update_message(interaction)