# KutGif for icss by: @rruuurr

from . import reply_id

ICSS_IMG = "https://telegra.ph/file/48c31877954d9fb53ee1f.mp4"
ICSS_TEXT = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑼𝑻𝑬 𝑮𝑰𝑭 𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ك5$"))
@icssbot.on(sudo_cmd(pattern="ك5$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    if ICSS_IMG:
        icss_caption = f"**{ICSS_TEXT}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الخامسه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, ICSS_IMG, caption=icss_caption, reply_to=reply_to_id
        )
        await icss.delete()
    else:
        await edit_or_reply(
            icss,
            f"**{ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الخامسه 𓆰.**",
        )