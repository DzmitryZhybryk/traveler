from aiogram import Bot, types


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(
            command="start",
            description="Beginning of work"
        ),
        types.BotCommand(
            command="my_data",
            description="My personal data"
        ),
        types.BotCommand(
            command="load",
            description="Load you travel info"
        )
    ]

    await bot.set_my_commands(commands, types.BotCommandScopeDefault())
