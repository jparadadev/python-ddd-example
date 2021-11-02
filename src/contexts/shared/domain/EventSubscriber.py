from abc import abstractmethod
from typing import List

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.Interface import Interface


class EventSubscriber(Interface):

    @abstractmethod
    def subscribed_to(self) -> List[type]:
        raise NotImplementedError()

    @abstractmethod
    def on(self, domain_event: DomainEvent):
        raise NotImplementedError()
