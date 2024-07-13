# Foundation Models - LLM(Large language models)
# edgar.makwenda@nicogeneral.com
import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
# langchain -> LLM framework 
load_dotenv()
os.environ["OPENAI_API_KEY"]

llm_model = 'gpt-4'
chat = ChatOpenAI(temperature=0.0,model=llm_model)

email_response = """ 
Please find the following information about our meeting that is scheduled to be done on 18th June 2024, 10 AM at Boadzulu Hotel
"""
job_profile = """
ACTIONAID INTERNATIONAL IN MALAWI
The Organisation:
ActionAid Malawi(AAM) was established in 1990 under the country Agreement signed with the Government of Malawi and in 2007 registered as a local organization under the companies Act. With funding from the Global Fund through the Ministry of Health, ActionAid Malawi (AAM) serves as a Sub Recipient (SR) for the COVID-19 Response Mechanism – Community Engagement two year Grant (January 2024 to December 2025). AAM’s role involves coordinating Community-Led Monitoring (CLM) initiatives to enhance Health and Community Systems Strengthening. This implementation is carried out in partnership with three Sub-Sub Recipients (SSRs): Malawi Network of People Living with HIV/AIDS (MANET+), Creative Center for Community Mobilization (CRECCOM), and the Archdiocese of Lilongwe, Lilongwe Catholic Health Commission (LL-CHC). The C19RM Project is being implemented in 12 CLM districts in Malawi namely Nkhotakota, Rumphi, Mzimba North, Likoma, Zomba, Mwanza, Phalombe, Nsanje, Salima, Dowa, Ntchisi and Mchinji.
AAM seeks to engage the services of a highly motivated Project CLM and M&E Coordinator for a period of 18 months. The Coordinator will work in close collaboration with the C19RM Project team and AAM’s SSRs to lead M&E/CLM interventions for the project entitled “Covid-19 Response Mechanism – Community Engagement in all the targeted 12 CLM districts and at national level. The position will be responsible for developing, updating, and coordinating monitoring and evaluation (M&E) activities and events within the C19RM-CLM Programme, building the capacity of project staff and partners, district partners stakeholders in CLM and M&E, and promoting CLM knowledge transfer internally.
Position : CLM M&E Coordinator.
Duration : 18 months.
Reporting to : Program Manager.
Duty station : Lilongwe.
Report date:  01st July 2023.
Major Duties and responsibilities 
CLM Tool Development and Data Management 
Develop the annual, quarterly, and monthly work plans in collaboration with the Program Manager and Techical Coordinators for alignment with the project objectives.
Guide and supervise SSRs to ensure the proper data management and implementationof project activities in accordance with established procedures and targets.
Coordinate the development/adoption and implementation of a robust project monitoring and evaluation system that will ensure tracking of CLM project indicators at different levels (outputs, outcomes and impact).
Develop/ Adopt project database and ensure accountability through regular data updates and data integrity.
Lead and oversee the development and review of data collection tools for the project in collaboration with the SSRs.
Coordinate timely update and share database updates.
Monitoring and Reporting 
Conduct data collection, monitoring and consolidation, tracking, cleaning, analysis and generate reports for the C19RM project.
Maintain and update the C19RM indicator tracker table based on submissions from peer educators, matrons and other data sources
Carry out routine data quality assessments/ audits regularly to guide decision making and programme management
Provide alert to the programme manager/technical coordinators/ on corrective actions related to data quality, including flagging out issues and risks requiring timely actions.
Coordinate data collection, consolidation, analysis, capacity-building sessions and the preparation of monthly and quarterly reports for submission to the Program Manager/Technical Coordinators.
Prepare and consolidate monthly, quarterly and annual reports for the project.
Lead the Identification, preparation of case studies and change stories with SSRs to showcase project impact.
Guide and supervise SSRs to ensure proper data collection is aligned with approved standard operating procedures.

Assessments, Surveys and Evaluation 
Oversee the development and monitor of an Online Data Collection and Reporting System for CLM Program in the targeted 36 Health Facilities (in the targeted 12 CLM districts).
Liaise with the Project Manager to initiate and develop tools for end of project evaluation as per AAM, Ministry of Health/Global Fund standards.
Ensure that AAM country office learns from the end of project evaluation for decision making and improvement of other project designs.
Lead and/or coordinate all project assessments, and performance monitiring evaluations tasks and other tasks including planning and reporting on the same.
In collaboration with SSRs, update the indicator tracking table and any other project databases.
Coordinate the preparation and review of all project reports to ensure quality and accurate reporting.
Learning, Accountability and Capacity Building 
Prepare relevant evidence-based reports to ensure learning and programme quality improvement.
Build capacity of AAM staff and SSRs on result based monitoring through training to ensure adoption of new data monitoring techniques and data quality standards.
Keep abreast of new approaches and tools on M&E and provide capacity buidling to CLM staff and AAM pasrtners as needed.
Enable staff to monitor and evaluate their own efforts, gather relevant data, analysis and produce required progress reports.
Develop program strategies that are in line with C19RM program priorities and appropriately based on MEAL standards.
Support in the development and implementation of a clear supportive supervision and mentorship tools.
Contribute to the process of knowledge creation and dissemination related to community, district, and national know-how in the areas of CLM.
On other occasions, represent the project during engagements with donors, government, and national and international forums related to CLM when required.
Qualifications and Requirements
Bachelors degree in Statistics, Monitoring & Evaluation; population studies/demography , social sciences or any other related field.
Minimum of 5 years of professional experience in the field of programme/project planning, management, and monitoring and evaluation of large-scale projects
Substantive knowledge and experience in CLM, TB, HIV and Malaria and gender programming.
Demonstrated experience in data processing and management of large-scale projects.
Demonstrated practical experience of statistical packages and/ or data analysis software (e.g. SPSS, Kobo Tool kit, Excel, Epi Info, SMART, STAT 01) and advanced computer skills (word-processing, spread sheets, and databases) are a must.
Knowledge of Sexual Harassment, Exploitation and Abuse (SHEA) and Safeguarding.
How to Apply
Interested individuals should apply by email only to : Recruitment.Malawi@actionaid.org Submission should be made by 5pm, 17 June 2024.
ActionAid Malawi welcomes applications from all sections of community and promotes diversity.All applications will be considered on their individual merit. Suitably qualified candidates, especially women are encouraged to apply.  Due to high volumes of applications received, we can only correspond with short listed applicants.
"""
email_template = """ 
From the following email, extract the following information:
meeting_date: This is the date of the meeting.
meeting_location: This is the location where the meeting is supposed to take place

Format the output as JSON with the following keys:
meeting_date
meeting_location

email:{email}

"""
job_template ="""
From the following job profile , extract the following information:
company_name: This is the company name that is recruiting for the position in the job profile.
position_title: This is the position or the job title
qualification: This is the qualification of the position in the job profile

Format the output as JSON with the following keys:
company_name
position_title
qualification

job profile: {job_profile}
"""

job_prompt = ChatPromptTemplate.from_template(template=job_template)
# prompt = ChatPromptTemplate.from_template(template=email_template)
actual_job_prompt = job_prompt.format_messages(job_profile=job_profile)
#actual_prompt = prompt.format_messages(email=email_response)
# translation_message = prompt_template.format_messages(
#     customer_review = customer_review,
#     language=language
# )
# print(actual_prompt)
# response = chat(actual_prompt)
response = chat(actual_job_prompt)
# response = chat_model(translation_message)
print(response.content)

# description, data job 
# description, m&e 
# description, neitehr data or m&e