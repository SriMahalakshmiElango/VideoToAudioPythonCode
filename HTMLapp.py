from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
 
st.set_page_config(page_title="Srimahalakshmi Resume",page_icon=":email:",layout="wide")


with st.container():
    st.subheader("Hi, I am Srimahalakshmi Elango :wave:")
    left_column,right_column = st.columns(2)
    with left_column:
            st.title("I am a Data Engineer")
            st.write("I am passionate about writing codes and solving business problems")
            st.write(":iphone: +1(438) 929 5982 :house: Montreal,Quebec,Canada")
            st.write(":email: srimahalakshmi.elango@gmail.com")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ftlw1wbu.json")

with right_column:
    st_lottie(lottie_coding,height=200,key="resume")
    
with st.container():
    st.write("---")
    st.header(":mortar_board: Professional Summary")
    st.write("##")
    st.write(
            """
            \n•	Overall 7+ years of professional IT experience in Insurance and Banking Domains which includes experience in Big Data Ecosystem and Mainframe related technologies   
            \n•	Excellent experience in Hadoop architecture and various component such as HDFS Name Node, Data Node, Resource Manager, Application Master and MapReduce and YARN
            \n•	Good Knowledge on Hadoop Master-Slave architecture and monitoring the cluster 
            \n•	Experience in managing and reviewing Hadoop log files 
            \n•	Experience in importing and exporting data using Sqoop from HDFS to Relational Database systems and vice-versa 
            \n•	Good exposure in Data Warehousing Concepts.
            \n•	Extensive experience with data Extraction, Transformation and Loading (ETL) from multiple data sources 
            \n•	Created multiple Hive tables, implemented static, dynamic partitioning and buckets in Hive for efficient data access
            \n•	Wrote Ad-hoc queries for analysing the data using HIVE QL
            \n•	Experience in handling data with different file formats such as Sequential, Avro, Parquet, RC and ORC 
            \n•	Experienced in developing spark application using Spark Core, Spark SQL and Spark Streaming API's
            \n•	Implemented various frameworks like Data Governance, Data provisioning, Data Wrangling, Data Munging, Data Persistence, Data Enrichment with help of technologies like Bigdata, Spark, Python, Hive etc., 
            \n•	Experience in Agile (SAFe) and Waterfall methodology
            \n•	Excellent interpersonal, communication skills, self-motivated, quick learner and willingness to learn new technologies.

"""
        )
        




img_edu=Image.open("c:/users/murug/Downloads/images/Education.png")
img_de = Image.open("c:/users/murug/Downloads/images/Data Engineer.png")
img_dei = Image.open("c:/users/murug/Downloads/images/Data Engineer Intern.png")
img_ia = Image.open("c:/users/murug/Downloads/images/Infrastructure Analyst.png")
img_ts = Image.open("c:/users/murug/Downloads/images/Technical Skills.png")

with st.container():
    st.header(":school: Educational Summary")
    st.write("##")
    st.image(img_edu)

with st.container():
    st.header(":office: Work Experience")
    st.write("##")
    st.image(img_de)
    st.write("##")
    st.subheader("Responsibilities")
    st.write(
        """ \n•	Data acquisition from internal/external data sources
            \n• Create and maintain optimal data pipeline architecture
            \n• Identify, design, and implement process internal process improvements
            \n•	Migration of data warehouse from SQL server to Hadoop & Hive
            \n•	Analysed the SQL scripts and designed it by using Spark SQL for faster performance
            \n•	Involved in converting Hive/SQL queries into Spark transformations using Spark RDD's
            \n•	Experience in usage of Hadoop distribution like Cloudera, Hortonworks distribution & Amazon AWS
            \n•	Hands on experience with AWS (Amazon Web Services), Elastic Map Reduce (EMR), Storage S3, EC2 instances and Data Warehousing. 

        """
    )
    
    
    
with st.container():
    st.write("##")
    st.image(img_dei)
    st.write("##")
    st.subheader("Responsibilities")
    st.write(
        """
        \n•	Involved in loading data from Linux File system to HDFS
        \n•	Involved in HDFS maintenance and loading of structured and unstructured data  
        \n•	Involved in Cluster coordination services through Zookeeper 
        \n•	Wrote Hadoop jobs to analyse, process, validate and integrate the data received from different vendors
        \n•	Responsible to manage data coming from different sources
        \n•	Worked on analysing Hadoop cluster and different big data analytic tools including Sqoop and Spark
        \n•	Used Sqoop to extract the data back to relational database for business reporting
        \n•	Extensively worked on creating many SQOOP scripts which involves for full refresh and Change Data Capture (CDC) & Slowly changing Dimension (SDC) functionality
        \n•	Expertise in performance tuning with indexing techniques, table partitioning, bucketing to handle large volume of data
        \n•	Data ingestion pipeline and Source File Management - Developed shell script to pull data from AWS to Edge node and Hadoop location
        \n•	Responsible for developing data ingestion pipeline using Sqoop, MR and Hive to extract the data from weblogs and store the results for downstream consumption
        \n•	Responsible in creating Hive tables, loading data and writing Hive Queries 
        \n•	Worked with HiveQL on big data of logs to perform a trend analysis of user behaviour on various online modules.
        \n•	Good experience in Hive partitioning, bucketing and perform different types of joins on Hive tables and implementing Hive SerDe's like REGEX, JSON and Avro.  

        """)


with st.container():
    st.write("##")
    st.image(img_ia)
    st.subheader("Production Management (Autosys)")
    st.write(""" \n•	Ensuring successful batch completion as per schedules (150+ applications, 90K+ jobs) 
                \n•	Monitoring of jobs running in Unix/Database machine through Customized filters in AutoSys JSC 
                \n•	Capable of imparting AutoSys commands on jobs as per the fix required by developers 
                \n•	Acquired thorough Knowledge in JIL scripts through Deployment of JIL and Calendar files (.Jil /. Cal) for an update or production change. 
                \n•	Validation of AutoSys JIL & calendar scripts through SBM tool 
                \n•	Familiar with administration task such as Force start, kill job, on-ice, off-ice, on-hold, off hold, future send event and so on 
                \n•	Execution of SQL scripts through Rapid SQL to look for errors with the files  
                \n•	Monitoring transactions of files and notifying Third party vendor regarding delays 
                \n•	Developed Expertise in interacting with Clients as Client managers have to be updated on major Production failures
                 """ )
    st.subheader("Mainframe Expediting Services ")
    st.write(
        """
        \n•	Ensuring successful batch completion according to the schedules (50+ applications) 
        \n•	Monitoring the down queue of batch jobs in JOBTRAC to give quick fixes using predefined procedures or reach out to Application support for productions Abends. 
        \n•	Scheduling Jobs, monitoring periodic batch events and modifying Job’s JCL in Jobtrac on Adhoc basis as part of Service Requests within SLA 
        \n•	Monitoring performance of streams and CPU, request performance boost or request assistance from operations 
        \n•	Developed Expertise in implementation of permanent production changes in Jobs/Schedules through Packages in Change man tool.  
        \n•	Capable of tracking the transmission of mainframe files from remote system through Cyber fusion panel upon Production failures. 
        \n•	Taken care of change/ release related activities and Business Continuation Process. 
        \n•	Creating problem/Change tickets using BMC Remedy to log the handled issues or for the implementation of change.
        """)

with st.container():
    st.subheader("Technical Skills")
    st.image(img_ts)
    
with st.container():
    st.header(":newspaper: Certifications")
    st.write(
        """
        \n• IBM Interskill – Mainframe Operator – DB2 Operations 
        \n•	IBM Interskill – Mainframe specialist – File Transfer Foundations 
        \n•	Udemy – Mainframe: The complete JCL course from Beginner to Expert  
        \n•	ITIL Foundations 
        \n•	Essential Programming in Python Programming  

        """
    )

with st.container():
    st.header(":trophy: Achievements")
    st.write(
        """
        \n•	Earned multiple “On the Spot” and “Best Performer” awards at TCS
        \n•	Earned “Analyst of the Month” twice in current Organization for Year 2021
        \n•	Earned badge on completion of Level 2 in Master the Mainframe 2020 contest  

        """
    )