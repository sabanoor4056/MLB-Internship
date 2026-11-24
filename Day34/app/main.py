
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

from app.routes import students

tags_metadata = [
    {
        "name": "General",
        "description": "Basic API information and health status."
    },
    {
        "name": "Students",
        "description": "Create, view, search, update and delete student records."
    }
]

app = FastAPI(
    title="Student Management API",
    description=(
        "A RESTful API for managing student records using FastAPI, "
        "Pydantic validation and in-memory storage."
    ),
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url=None,
    redoc_url="/redoc"
)


@app.get("/", tags=["General"], summary="API Welcome")
def home():
    return {
        "message": "Welcome to Student Management API",
        "status": "Running",
        "documentation": "/docs"
    }


@app.get("/health", tags=["General"], summary="Check API Health")
def health_check():
    return {
        "status": "healthy",
        "message": "API is running successfully"
    }


@app.get("/docs", include_in_schema=False)
async def custom_docs():
    swagger_html = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Student Management API | API Documentation",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "displayRequestDuration": True,
            "filter": True,
            "docExpansion": "none"
        }
    )

    html = swagger_html.body.decode("utf-8")

    dark_css = """
    <style>
        body, .swagger-ui {
            background: #0b1120 !important;
            color: #e2e8f0 !important;
        }

        .swagger-ui .topbar {
            background: #111827 !important;
            border-bottom: 1px solid #334155;
        }

        .swagger-ui .info .title,
        .swagger-ui .info p,
        .swagger-ui .info li,
        .swagger-ui .opblock-tag,
        .swagger-ui label,
        .swagger-ui .parameter__name,
        .swagger-ui .parameter__type,
        .swagger-ui table,
        .swagger-ui .response-col_status,
        .swagger-ui .response-col_description,
        .swagger-ui .model-title {
            color: #e2e8f0 !important;
        }

        .swagger-ui .opblock {
            background: #172033 !important;
            border: 1px solid #334155 !important;
            border-radius: 10px;
            margin-bottom: 12px;
            box-shadow: none !important;
        }

        .swagger-ui .opblock .opblock-summary {
            border-color: #334155 !important;
        }

        .swagger-ui .opblock .opblock-summary-path,
        .swagger-ui .opblock .opblock-summary-description {
            color: #f8fafc !important;
        }

        .swagger-ui .opblock .opblock-section-header,
        .swagger-ui .scheme-container {
            background: #1e293b !important;
            box-shadow: none !important;
        }

        .swagger-ui .opblock-body,
        .swagger-ui .responses-wrapper,
        .swagger-ui .parameters-container {
            background: #111827 !important;
        }

        .swagger-ui input,
        .swagger-ui textarea,
        .swagger-ui select {
            background: #1e293b !important;
            color: #ffffff !important;
            border: 1px solid #475569 !important;
        }

        .swagger-ui .model-box,
        .swagger-ui section.models {
            background: #172033 !important;
            border-color: #334155 !important;
        }

        .swagger-ui .btn.execute {
            background: #6366f1 !important;
            color: #ffffff !important;
            border: none !important;
        }

        .swagger-ui .btn {
            color: #e2e8f0 !important;
        }

        .swagger-ui .markdown p,
        .swagger-ui .markdown li {
            color: #cbd5e1 !important;
        }

        .swagger-ui .info {
            margin: 35px 0;
        }

        .swagger-ui .opblock-tag {
            border-bottom: 1px solid #334155 !important;
        }
    </style>
    """

    html = html.replace("</head>", dark_css + "</head>")

    return HTMLResponse(content=html)


app.include_router(students.router)
