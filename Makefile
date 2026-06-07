# Root passthrough to the local OSS substrate in local/.
# Additive / local-only / $0. See local/README.md for details.

.PHONY: up down seed smoke teardown logs help

help up down seed smoke teardown logs:
	$(MAKE) -C local $@
