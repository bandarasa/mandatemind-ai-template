import os  # ✅ This must be at the top

# Define folder structure
folders = [
    "frontend",
    "frontend/public",
    "frontend/src",
    "frontend/src/components",
    "frontend/src/components/MandateComposer",
    "frontend/src/components/AuditPrepWizard",
    "frontend/src/components/MSSPDashboard",
    "frontend/src/components/CopilotSidebar",
    "frontend/src/pages",
    "frontend/src/styles",
    "backend",
    "backend/app",
    "backend/app/api",
    "backend/app/models",
    "backend/app/services",
    "backend/app/utils",
    "schemas",
    "copilot",
    "copilot/prompts",
    "scripts",
    "docs"
]

# Define files to create
files = [
    "README.md", "LICENSE", ".env.example",
    "backend/app/main.py",
    "backend/app/api/mandates.py",
    "backend/app/api/controls.py",
    "backend/app/api/siem_adapter.py",
    "backend/app/api/audit.py",
    "backend/app/models/mandate.py",
    "backend/app/models/control.py",
    "backend/app/models/evidence.py",
    "backend/app/services/qradar.py",
    "backend/app/services/sentinel.py",
    "backend/app/services/splunk.py",
    "backend/app/services/elastic.py",
    "backend/app/utils/narrative_generator.py",
    "copilot/copilot_engine.py",
    "copilot/copilot_interface.md",
    "copilot/prompts/audit_narratives.md",
    "copilot/prompts/drift_detection.md",
    "copilot/prompts/mandate_mapping.md",
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

print("✅ MandateMind AI folder and file structure created successfully.")
