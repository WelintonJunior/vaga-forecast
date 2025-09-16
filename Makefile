sql_up:
	@echo "Removendo container anterior (se existir)..."
	-@docker rm -f mysql

	@echo "Iniciando novo container mysql com volume persistente..."
	@docker run --name mysql \
		-e MYSQL_ROOT_PASSWORD=1234 \
		-e MYSQL_DATABASE=vaga-forecast \
		-v mysql_data:/var/lib/mysql \
		-p 3306:3306 \
		-d mysql:8.0

	@echo "Aguardando inicialização do container mysql..."
	@sleep 10

migrate:
	@python3 migrate.py