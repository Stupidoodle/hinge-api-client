"""Pydantic schemas for API responses.

The holy texts. Parsing this much JSON without Pydantic is a war crime.
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class BaseHingeModel(BaseModel):
    """Base model with common configuration."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        extra="ignore",
        populate_by_name=True,
    )


class HingeAuthToken(BaseHingeModel):
    """Schema for the main Hinge Bearer token."""

    identity_id: str
    token: str
    expires: datetime


class SendbirdAuthToken(BaseHingeModel):
    """Schema for the Sendbird Bearer token."""

    token: str
    expires: datetime


class LikeLimit(BaseHingeModel):
    """Schema for the daily like limit status."""

    likes_left: int
    super_likes_left: int  # If you have those, consider yourself lost


class TextReview(BaseHingeModel):
    """Schema for the text moderation pre-flight check."""

    is_harmful: bool


class RecommendationSubject(BaseHingeModel):
    """A single user recommendation from the feed."""

    subject_id: str
    rating_token: str


class RecommendationsFeed(BaseHingeModel):
    """A feed of user recommendations."""

    origin: str
    subjects: list[RecommendationSubject]


class RecommendationsResponse(BaseHingeModel):
    """The full response from the recommendations' endpoint."""

    feeds: list[RecommendationsFeed]


class Location(BaseHingeModel):
    """Schema for a user's location."""

    name: str


class Profile(BaseHingeModel):
    """Schema for a user's profile data."""

    covid_vax: int | None = None
    children: int | None = None
    dating_intention: int | None = None
    dating_intention_text: str | None = None
    drinking: int | None = None
    drugs: int | None = None
    educations: list[str] | None = None
    ethnicities: list[int] | None = None
    family_plans: int | None = None
    first_name: str
    gender_identity_id: int | None = None
    height: int | None = None
    hometown: str | None = None
    job_title: str | None = None
    languages_spoken: list[int] | None = None
    last_name: str | None = None
    location: Location
    marijuana: int | None = None
    pets: list[int] | None = None
    politics: int | None = None
    pronouns: list[int] | None = None
    relationship_type_ids: list[int] | None = None
    relationship_types_text: str | None = None
    religions: list[int] | None = None
    selfie_verified: bool | None = None
    sexual_orientations: list[int] | None = None
    smoking: int | None = None
    works: str | None = None
    last_active_status_id: int | None = None
    did_just_join: bool | None = Field(default=None, alias="didjustJoin")


class UserProfile(BaseHingeModel):
    """Schema for a user's public profile data."""

    user_id: str
    profile: Profile


class PhotoContent(BaseHingeModel):
    """Schema for a single photo in a user's profile."""

    caption: str | None = None
    content_id: str
    cdn_id: str
    location: str | None = None
    prompt_id: str | None = None
    source: str | None = None
    url: str


class AnswerContent(BaseHingeModel):
    """Schema for a prompt answer."""

    content_id: str
    question_id: str
    response: str


class PromptContent(BaseHingeModel):
    """Schema for a user's prompt content."""

    content_id: str
    question_id: str
    options: list[str]


class ProfileContent(BaseHingeModel):
    """Schema for a user's full content (photos, answers, etc.)."""

    user_id: str
    content: dict[str, list[PhotoContent | AnswerContent]]
