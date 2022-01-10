PREFIX ?= /usr/local

all:
	@echo Run \'make install\' to install PS-Typer.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@printf "#!/bin/env bash\n%s" "$(realpath ./bin/run_program.sh)" > $(DESTDIR)$(PREFIX)/bin/ps-typer
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/ps-typer
	@printf "\nps-typer easy launch script installed successfully at $(PREFIX)/ps-typer\n"

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/ps-typer