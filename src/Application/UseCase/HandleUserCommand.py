from src.Application.DTO.UserActivityDTO import UserActivityDTO
from src.Application.Factory.UserFactory import UserFactory
from src.Domain.Repository.UserRepository import UserRepository
from src.Domain.Constant.Action import Action

class HandleUserCommand:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, dto: UserActivityDTO, is_admin: bool, has_command: bool) -> Action:

        if is_admin:
            return Action.ALLOW

        user = self.user_repository.find_by_id(dto.user_id)

        if not user:
            user = UserFactory.create_from_dto(dto=dto)

        if has_command:
            user.record_spam_activity()
            self.user_repository.save(user)
        else:
            return Action.ALLOW

        if user.is_muted:
            return Action.MUTE

        return Action.DELETE