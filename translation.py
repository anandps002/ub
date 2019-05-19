class Translation(object):
    START_TEXT = """Thank You for using me.\n\nNow send me a valid link to upload.\n\nMade by @AnanTEcH_MasTer"""
        
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@GetPublicLinkBot URL detected. Please do not abuse the service!"
    DOWNLOAD_START = "Downloading Your Video ....."
    UPLOAD_START = "Uploading Your Video....."
        RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please rate me if you find me useful. https://t.me/TRV_HD"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nPlease rate me if you find me useful. https://t.me/tlgrmcbot?start=utubegobot-review \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.me/AnandTEcH_MasTer'>@Anand</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
     NO_VOID_FORMAT_FOUND = "something is wrong with the URL you gave me 🤦‍♀️. If you think this could be a bug please report on https://github.com/thwarikh/fmDL_Bot/issues OR https://telegram.org/thwarikh\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: <a href='https://t.me/Flowers_TV'>{}</a>
Expires on: {}"""
    HELP_USER = """To Download youtube videos send any valid link so that i can upload it to Telegram directly.

Send /me to know current plan details"""
    
     USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
        CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per hour.
/upgrade or Try 3600 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users. "
