import pytest
from csp_bot import BotCommand, BotUser

from csp_bot_commands.trout import TroutSlapCommand

cmd = TroutSlapCommand()


class TestTroutSlap:
    def test_statics(self):
        assert cmd.backends() == []  # All
        assert cmd.command() == "slap"
        assert cmd.name() == "Slap"
        assert cmd.help() == "Slap someone with a wet fish. Syntax: /slap <user> [/channel <channel>]"

    @pytest.mark.parametrize(
        "args,",
        [
            ("random",),
            ("trout",),
        ],
    )
    def test_execute(self, args):
        msg = cmd.execute(
            BotCommand(
                backend="slack",
                channel_id="test_channel",
                channel_name="test_channel",
                source=BotUser(
                    user_id="123",
                    name="Test User",
                    email="test@example.com",
                    handle="testuser",
                ),
                targets=(
                    BotUser(
                        user_id="456",
                        name="Target User",
                        email="target@example.com",
                        handle="targetuser",
                    ),
                ),
                args=args,
            )
        )
        assert msg is not None
        assert msg.backend == "slack"
        assert msg.channel.id == "test_channel"
        assert msg.content.startswith("<@123> slaps <@456> with")
        if args[0] == "trout":
            assert "trout" in msg.content
