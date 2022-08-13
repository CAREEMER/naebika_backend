from pydantic import BaseModel


class VkSign(BaseModel):
    vk_access_token_settings: str = ""
    vk_app_id: str
    vk_are_notifications_enabled: bool
    vk_is_app_user: bool
    vk_is_favorite: bool
    vk_language: str
    vk_platform: str
    vk_ref: str
    vk_ts: str
    vk_user_id: str
    sign: str
