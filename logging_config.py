"""Logger for the application."""

import logging
import structlog


logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
)

processors = [
    structlog.stdlib.add_log_level,
    structlog.processors.CallsiteParameterAdder(
        parameters=[
            structlog.processors.CallsiteParameter.FILENAME,
            structlog.processors.CallsiteParameter.LINENO,
            structlog.processors.CallsiteParameter.FUNC_NAME,
        ]
    ),
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.dev.ConsoleRenderer(),
]

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    processors=processors,  # type: ignore
)


logger = structlog.get_logger()
