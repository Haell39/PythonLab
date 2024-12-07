# Dicionário de Dados - LojaVirtualDB

## Tabela: Cliente
| Coluna       | Tipo         | Descrição                      | Restrições                |
|--------------|--------------|--------------------------------|---------------------------|
| Id_Cliente   | INT          | Identificador único do cliente | PK, Identity(1000,10)     |
| Nome         | VARCHAR(100) | Nome completo do cliente       | NOT NULL                  |
| CPF          | VARCHAR(11)  | CPF do cliente                 | NOT NULL, UNIQUE          |
| Email        | VARCHAR(100) | E-mail do cliente              | NOT NULL, UNIQUE          |
| Endereco     | VARCHAR(200) | Endereço do cliente            | NOT NULL                  |
| DataCadastro | DATE         | Data de cadastro do cliente    | DEFAULT (data atual)      |

## Tabela: Produto
| Coluna         | Tipo          | Descrição                      | Restrições                |
|----------------|---------------|--------------------------------|---------------------------|
| Id_Produto     | INT           | Identificador único do produto | PK, Identity(1000,10)     |
| Nome           | VARCHAR(100)  | Nome do produto                | NOT NULL                  |
| Descricao      | VARCHAR(200)  | Descrição do produto           | NULL                      |
| Cd_Categoria   | INT           | Código da categoria            | NOT NULL, FK              |
| Preco          | DECIMAL(10,2) | Preço do produto               | CHECK (Preco > 0)         |

## Tabela: NotaFiscalCompra
| Coluna         | Tipo          | Descrição                      | Restrições                |
|----------------|---------------|--------------------------------|---------------------------|
| Id_NFC         | INT           | Identificador da nota fiscal   | PK, Identity(1000,10)     |
| Id_Cliente     | INT           | Cliente da compra              | NOT NULL, FK              |
| DataPedido     | DATE          | Data do pedido                 | DEFAULT (data atual)      |
| Descricao      | VARCHAR(200)  | Descrição da compra            | NULL                      |

## Tabela: Pagamento
| Coluna         | Tipo          | Descrição                      | Restrições                |
|----------------|---------------|--------------------------------|---------------------------|
| Cd_Pagamento   | INT           | Identificador do pagamento     | PK, Identity(1000,10)     |
| Id_NFC         | INT           | Nota fiscal relacionada        | NOT NULL, FK              |
| Data           | DATE          | Data do pagamento              | DEFAULT (data atual)      |
| Valor          | DECIMAL(10,2) | Valor do pagamento             | NOT NULL, CHECK (Valor > 0)|
| TipoPagamento  | VARCHAR(20)   | Tipo de pagamento              | CHECK (Pix, Cartao, Boleto)|

## Tabela: Fornecedor
| Coluna         | Tipo          | Descrição                      | Restrições                |
|----------------|---------------|--------------------------------|---------------------------|
| Id_Fornecedor  | INT           | Identificador do fornecedor    | PK, Identity(1000,10)     |
| CNPJ           | VARCHAR(14)   | CNPJ do fornecedor             | NOT NULL, UNIQUE          |
| Nome           | VARCHAR(100)  | Nome do fornecedor             | NOT NULL                  |
| Telefone       | VARCHAR(15)   | Telefone do fornecedor         | NULL                      |
| Endereco       | VARCHAR(200)  | Endereço do fornecedor         | NOT NULL                  |
| Frn_Contato    | VARCHAR(100)  | Contato do fornecedor          | NULL                      |

**Observações:**
- Todas as tabelas usam Identity começando em 1000 e incrementando de 10 em 10
- Chaves estrangeiras (FK) mantêm integridade referencial
- Restrições de CHECK garantem a consistência dos dados