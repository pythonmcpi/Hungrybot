from discord.ext import commands


class HungryContext(commands.Context):
    def reply(self, message):
        return self.send("{0} | {1}".format(self.author.mention, message))
    
    async def send(self, content = None, **kwargs):
        if not content is None and len(content) > 2000:
            messages = [""]
            for line in content.split("\n"):
                if len(messages[-1]+line+"\n") > 2000:
                    messages.append("")
                messages[-1] += line + "\n"
            for message in messages:
                last = await super().send(message, **kwargs)
            return last
        elif "embed" in kwargs.keys() and kwargs["embed"].description and len(kwargs["embed"].description) > 2048:
            embed = kwargs["embed"]
            messages = [""]
            for line in embed.description.split("\n"):
                if len(messages[-1]+line+"\n") > 2048:
                    messages.append("")
                messages[-1] += line + "\n"
            for message in messages:
                embed.description = message
                kwargs["embed"] = embed
                last = await super().send(content, **kwargs)
            return last
        else:
            return await super().send(content, **kwargs)
