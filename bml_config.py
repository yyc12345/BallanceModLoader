# BML_CONFIG.PY TEMPLATE
# You shoule copy bml_config.py.template as bml_config.py,
# then modify it for your proper path

# Specific whether current build is nightly build.
# If this field is blank(empty string), it mean that current build is not nightly build.
# Otherwise, this field should fill a git commit hash ot indicate its version.
nightly = None

# Specific BML deploy path. Usually it is Ballance root path.
deploy_path = "Build"
