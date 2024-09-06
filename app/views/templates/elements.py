###############################################  초기 화면 element(CI/CD) ###############################################
## CI/CD 서비스 버튼 Elements
elements1 = [
        {"text" : "Pipeline 생성" , "value" : "Pipeline", "action_id" : "Pipeline"},
        {"text" : "Repository 생성" , "value" : "Repository", "action_id" : "Repository"},
]

## 파이프라인 생성 버튼 elements
elements7 = [
        {"text" : "AWS Pipeline 생성" , "value" : "company_aws_pipeline", "action_id" : "company_aws_pipeline"},
        {"text" : "Gitlab Pipeline 생성" , "value" : "company_gitlab_pipeline", "action_id" : "company_gitlab_pipeline"},
]

## repository 종류 선택 버튼 elements
select_Kinds_of_Repository = [
        {"text" : "AWS" , "value" : "AWS", "action_id" : "AWS"},
        {"text" : "GITLAB" , "value" : "GITLAB", "action_id" : "GITLAB"}
]


company_aws_pipeline = [
        {"text" : "디지몽" , "value" : "dgmong", "action_id" : "DGMONG"},
        {"text" : "하마랩" , "value" : "hamalab", "action_id" : "HAMALAB"},
        {"text" : "쿠발토" , "value" : "cubalto", "action_id" : "CUBALTO"},
        {"text" : "유메이" , "value" : "umay", "action_id" : "UMAY"},
        {"text" : "위키포키" , "value" : "wikifoki", "action_id" : "WIKIFOKI"},
        {"text" : "신사유람단" , "value" : "sinsa", "action_id" : "SINSA"},
        {"text" : "씨엠비" , "value" : "cmb", "action_id" : "CMB"},
        {"text" : "세이프스쿨" , "value" : "safeschool", "action_id" : "SAFESCHOOL"},
        {"text" : "매니지온" , "value" : "manageon", "action_id" : "MANAGEON"},
        {"text" : "아이오엔" , "value" : "ion", "action_id" : "ION"},
        {"text" : "코리안쌤" , "value" : "ppntalk", "action_id" : "PPNTALK"}
]

## 
company_gitlab_pipeline = [
        {"text" : "디지몽" , "value" : "dgmong", "action_id" : "46"},
        {"text" : "하마랩" , "value" : "hamalab", "action_id" : "2"},
        {"text" : "쿠발토" , "value" : "cubalto", "action_id" : "45"},
        {"text" : "카고랩" , "value" : "cargolab", "action_id" : "199"},
        {"text" : "신사유람단" , "value" : "sinsa", "action_id" : "58"},
        {"text" : "씨엠비" , "value" : "cmb", "action_id" : "43"},
        {"text" : "피알원" , "value" : "prone", "action_id" : "203"},
        {"text" : "아이오엔" , "value" : "ion", "action_id" : "88"}
]

###############################################  초기 화면 element(## 각 AWS 서비스 선택 버튼 Elements) ###############################################
elements2 = [
        {"text" : "IAM 계정 생성" , "value" : "awsIam", "action_id" : "awsIam"},
        {"text" : "IAM 권한 요청" , "value" : "awsIamPermission", "action_id" : "awsIamPermission"},
] 
elements3 = [
        {"text" : "Ec2 생성" , "value" : "awsEC2", "action_id" : "awsEC2"},
        {"text" : "S3 생성" , "value" : "awsS3", "action_id" : "awsS3"},
        {"text" : "Elb 생성" , "value" : "awsELB", "action_id" : "awsELB"},
]
elements4=[
        {"text" : "RDS 생성" , "value" : "awsRDS", "action_id" : "awsRDS"},
        {"text" : "Migration 요청" , "value" : "Migration", "action_id" : "Migration"}
]
elements5=[
        {"text" : "Elasticsearch 요청" , "value" : "awsElasticSearch", "action_id" : "awsElasticSearch"},
        {"text" : "Parameter-store 요청" , "value" : "awsParameterStore", "action_id" : "awsParameterStore"}
]
elements6 = [
        {"text" : "기타 문의 사항" , "value" : "inquiryEtc", "action_id" : "inquiryEtc"}
]

############################################ 선택 항목 Elements ############################################
## CodeBuild,CodeDeploy 선택 할때 사용
stages = [
        {"text" : "CodeBuild" , "value" : "CodeBuild"},
        {"text" : "CodeDeploy" , "value" : "CodeDeploy"},
]

## branch elements 선택 할 때 사용
branch = [
        {"text" : "master" , "value" : "master"},
        {"text" : "develop" , "value" : "develop"},
        {"text" : "beta" , "value" : "beta"}
]

## 부서 elements 선택 할 때 사용
departments = [
        {"text" : "develop" , "value" : "AI"},
        {"text" : "Devops" , "value" : "Devops"},
        {"text" : "Backend" , "value" : "Backend"},
        {"text" : "Frontend" , "value" : "Frontend"}
]

## yes or no 선택 element
OX = [
        {"text" : "✅" , "value" : "yes"},
        {"text" : "❌" , "value" : "no"},
]

## 용도 선택 element(Dev 인지 Prod 인지)
usage = [
        {"text" : "API" , "value" : "API"},
        {"text" : "Prod" , "value" : "Prod"},
        {"text" : "Dev" , "value" : "Dev"},
        {"text" : "Integration" , "value" : "Integration"}
]

## 운영체제 지정
operatingSystem = [
        {"text" : "Ubuntu 22.04 LTS" , "value" : "22.04"},
        {"text" : "Ubuntu 20.04 LTS" , "value" : "20.04"},
        {"text" : "etc" , "value" : "etc"}
]

## DB 엔진
dbEngine = [
        {"text" : "Amazon Aurora(MySQL)" , "value" : "AAM"},
        {"text" : "Amazon Aurora(PostgreSQL)" , "value" : "AAP"},
        {"text" : "MySQL" , "value" : "MS"},
        {"text" : "MariaDB" , "value" : "MD"},
        {"text" : "PostgreSQL" , "value" : "PS"},
        {"text" : "Oracle" , "value" : "Oracle"},
        {"text" : "Microsoft SQL Server" , "value" : "MSS"}
]

## Opensearch 엔진
opensearchEngine = [
        {"text" : "OpenSearch_2.13" , "value" : "2.13"},
        {"text" : "OpenSearch_2.11" , "value" : "2.11"},
        {"text" : "OpenSearch_2.9" , "value" : "2.9"},
        {"text" : "OpenSearch_2.7" , "value" : "2.7"},
        {"text" : "OpenSearch_2.5" , "value" : "2.5"},
        {"text" : "OpenSearch_2.3" , "value" : "2.3"},
        {"text" : "OpenSearch_1.3" , "value" : "1.3"}
]

## Project
Project = [
        {"text" : "디지몽" , "value" : "dgmongCompany"},
        {"text" : "하마랩" , "value" : "hamalabCompany"},
        {"text" : "쿠발토" , "value" : "cubaltoCompany"},
        {"text" : "유메이" , "value" : "umayCompany"},
        {"text" : "위키포키" , "value" : "wikifokiCompany"},
        {"text" : "신사유람단" , "value" : "sinsaCompany"},
        {"text" : "코리안쌤" , "value" : "koreanssamCompany"},
        {"text" : "씨엠비" , "value" : "cmbCompany"},
        {"text" : "세이프스쿨" , "value" : "safeschoolCompany"},
        {"text" : "매니지온" , "value" : "manageonCompany"},
        {"text" : "아이오엔" , "value" : "ionCompany"},
]

## service
migration_service = [
        {"text" : "RDS" , "value" : "RDS"},
        {"text" : "Repository" , "value" : "Repository"}
]

######################################### 완료, 취소 버튼 element #########################################
## 완료, 취소 버튼 element - input 칸에만 해당
input_back_button = [
        {"text" : "완료" , "value" : "input-button", "action_id" : "input"},
        {"text" : "취소" , "value" : "back-button", "action_id" : "back"}
]

## gitlab 돌아가기 버튼 element
back = [
       {"text" : "돌아가기" , "value" : "back-button", "action_id" : "back"}
]

back_button = [
       {"text" : "돌아가기" , "value" : "back-button", "action_id" : "back_list"}
]

back_aws_button = [
        {"text" : "돌아가기" , "value" : "back-button", "action_id" : "back_aws_list"}
]

input_back_aws_button = [
        {"text" : "완료" , "value" : "input-button", "action_id" : "input"},
        {"text" : "취소" , "value" : "back-button", "action_id" : "back_aws_list"}
]

input_back_gitlab_button = [
        {"text" : "완료" , "value" : "input-button", "action_id" : "input"},
        {"text" : "취소" , "value" : "back-button", "action_id" : "back_gitlab_list"}
]