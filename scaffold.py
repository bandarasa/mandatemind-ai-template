import os

folders = [
    "frontend/src/components/MandateComposer",
    "frontend/src/components/AuditPrepWizard",
    "frontend/src/components/MSSPDashboard",
    "frontend/src/components/CopilotSidebar",
    "backend/app/api",
    "backend/app/models",
    "backend/app/services",
    "backend/app/utils",
    "schemas",
    "copilot/prompts",
    "scripts",
    "docs"
]

files = [
    "README.md", "LICENSE", ".env.example",
    "backend/app/main.py",
    "backend/app/api/mandates.py",
    "backend/app/api/controls.py",
    "backend/app/api/siem_adapter.py",
    "backend/app/api/audit.py",
    "copilot/copilot_engine.py",
    "copilot/copilot_interface.md",
    "scripts/seed_controls.py",
    "scripts/simulate_control_test.py",
    "scripts/generate_audit_package.py",
    "docs/architecture.md",
    "docs/onboarding_flow.md",
    "docs/api_reference.md",
    "docs/demo_script.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with placeholder content
for file in files:
    folder_path = os.path.dirname(file)
    if folder_path and not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    with open(file, "w") as f:
        f.write(f"# {os.path.basename(file)}\n")
