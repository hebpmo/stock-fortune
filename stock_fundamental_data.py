import tushare as ts
import sys
from sqlalchemy import create_engine

ENGINE = create_engine('mysql+pymysql://root:123456@localhost/stockdb?charset=utf8')

#基本面数据
def getbasicdb():
	basic = ts.get_stock_basics()
	print(basic)
	basic.to_sql('basics_data',ENGINE,if_exists='append') #fail,replace

#业绩报告
def getreportdb():
	report_2010_1 = ts.get_report_data(2010,1)
	report_2010_1.to_sql('reports_2010Q1',ENGINE,if_exists='append')
	report_2010_2 = ts.get_report_data(2010,2)
	report_2010_2.to_sql('reports_2010Q2',ENGINE,if_exists='append')
	report_2010_3 = ts.get_report_data(2010,3)
	report_2010_3.to_sql('reports_2010Q3',ENGINE,if_exists='append')
	report_2010_4 = ts.get_report_data(2010,4)
	report_2010_4.to_sql('reports_2010Q4',ENGINE,if_exists='append')

	report_2011_1 = ts.get_report_data(2011,1)
	report_2011_1.to_sql('reports_2011Q1',ENGINE,if_exists='append')
	report_2011_2 = ts.get_report_data(2011,2)
	report_2011_2.to_sql('reports_2011Q2',ENGINE,if_exists='append')
	report_2011_3 = ts.get_report_data(2011,3)
	report_2011_3.to_sql('reports_2011Q3',ENGINE,if_exists='append')
	report_2011_4 = ts.get_report_data(2011,4)
	report_2011_4.to_sql('reports_2011Q4',ENGINE,if_exists='append')

	report_2012_1 = ts.get_report_data(2012,1)
	report_2012_1.to_sql('reports_2012Q1',ENGINE,if_exists='append')
	report_2012_2 = ts.get_report_data(2012,2)
	report_2012_2.to_sql('reports_2012Q2',ENGINE,if_exists='append')
	report_2012_3 = ts.get_report_data(2012,3)
	report_2012_3.to_sql('reports_2012Q3',ENGINE,if_exists='append')
	report_2012_4 = ts.get_report_data(2012,4)
	report_2012_4.to_sql('reports_2012Q4',ENGINE,if_exists='append')

	report_2013_1 = ts.get_report_data(2013,1)
	report_2013_1.to_sql('reports_2013Q1',ENGINE,if_exists='append')
	report_2013_2 = ts.get_report_data(2013,2)
	report_2013_2.to_sql('reports_2013Q2',ENGINE,if_exists='append')
	report_2013_3 = ts.get_report_data(2013,3)
	report_2013_3.to_sql('reports_2013Q3',ENGINE,if_exists='append')
	report_2013_4 = ts.get_report_data(2013,4)
	report_2013_4.to_sql('reports_2013Q4',ENGINE,if_exists='append')

	report_2014_1 = ts.get_report_data(2014,1)
	report_2014_1.to_sql('reports_2014Q1',ENGINE,if_exists='append')
	report_2014_2 = ts.get_report_data(2014,2)
	report_2014_2.to_sql('reports_2014Q2',ENGINE,if_exists='append')
	report_2014_3 = ts.get_report_data(2014,3)
	report_2014_3.to_sql('reports_2014Q3',ENGINE,if_exists='append')
	report_2014_4 = ts.get_report_data(2014,4)
	report_2014_4.to_sql('reports_2014Q4',ENGINE,if_exists='append')

	report_2015_1 = ts.get_report_data(2015,1)
	report_2015_1.to_sql('reports_2015Q1',ENGINE,if_exists='append')
	report_2015_2 = ts.get_report_data(2015,2)
	report_2015_2.to_sql('reports_2015Q2',ENGINE,if_exists='append')
	report_2015_3 = ts.get_report_data(2015,3)
	report_2015_3.to_sql('reports_2015Q3',ENGINE,if_exists='append')
	report_2015_4 = ts.get_report_data(2015,4)
	report_2015_4.to_sql('reports_2015Q4',ENGINE,if_exists='append')

	report_2016_1 = ts.get_report_data(2016,1)
	report_2016_1.to_sql('reports_2016Q1',ENGINE,if_exists='append')
	report_2016_2 = ts.get_report_data(2016,2)
	report_2016_2.to_sql('reports_2016Q2',ENGINE,if_exists='append')
	# report_2016_3 = ts.get_report_data(2016,3)
	# report_2016_3.to_sql('reports_2016Q3',ENGINE,if_exists='append')
	# report_2016_4 = ts.get_report_data(2016,4)
	# report_2016_4.to_sql('reports_2016Q4',ENGINE,if_exists='append')

#盈利能力数据
def getprofitdb():
	profit_2010Q1 =ts.get_profit_data(2010,1)
	profit_2010Q1.to_sql('profit_2010Q1',ENGINE,if_exists='append')
	profit_2010Q2 =ts.get_profit_data(2010,2)
	profit_2010Q2.to_sql('profit_2010Q2',ENGINE,if_exists='append')
	profit_2010Q3 =ts.get_profit_data(2010,3)
	profit_2010Q3.to_sql('profit_2010Q3',ENGINE,if_exists='append')
	profit_2010Q4 =ts.get_profit_data(2010,4)
	profit_2010Q4.to_sql('profit_2010Q4',ENGINE,if_exists='append')

	profit_2011Q1 =ts.get_profit_data(2011,1)
	profit_2011Q1.to_sql('profit_2011Q1',ENGINE,if_exists='append')
	profit_2011Q2 =ts.get_profit_data(2011,2)
	profit_2011Q2.to_sql('profit_2011Q2',ENGINE,if_exists='append')
	profit_2011Q3 =ts.get_profit_data(2011,3)
	profit_2011Q3.to_sql('profit_2011Q3',ENGINE,if_exists='append')
	profit_2011Q4 =ts.get_profit_data(2011,4)
	profit_2011Q4.to_sql('profit_2011Q4',ENGINE,if_exists='append')

	profit_2012Q1 =ts.get_profit_data(2012,1)
	profit_2012Q1.to_sql('profit_2012Q1',ENGINE,if_exists='append')
	profit_2012Q2 =ts.get_profit_data(2012,2)
	profit_2012Q2.to_sql('profit_2012Q2',ENGINE,if_exists='append')
	profit_2012Q3 =ts.get_profit_data(2012,3)
	profit_2012Q3.to_sql('profit_2012Q3',ENGINE,if_exists='append')
	profit_2012Q4 =ts.get_profit_data(2012,4)
	profit_2012Q4.to_sql('profit_2012Q4',ENGINE,if_exists='append')

	profit_2013Q1 =ts.get_profit_data(2013,1)
	profit_2013Q1.to_sql('profit_2013Q1',ENGINE,if_exists='append')
	profit_2013Q2 =ts.get_profit_data(2013,2)
	profit_2013Q2.to_sql('profit_2013Q2',ENGINE,if_exists='append')
	profit_2013Q3 =ts.get_profit_data(2013,3)
	profit_2013Q3.to_sql('profit_2013Q3',ENGINE,if_exists='append')
	profit_2013Q4 =ts.get_profit_data(2013,4)
	profit_2013Q4.to_sql('profit_2013Q4',ENGINE,if_exists='append')

	profit_2014Q1 =ts.get_profit_data(2014,1)
	profit_2014Q1.to_sql('profit_2014Q1',ENGINE,if_exists='append')
	profit_2014Q2 =ts.get_profit_data(2014,2)
	profit_2014Q2.to_sql('profit_2014Q2',ENGINE,if_exists='append')
	profit_2014Q3 =ts.get_profit_data(2014,3)
	profit_2014Q3.to_sql('profit_2014Q3',ENGINE,if_exists='append')
	profit_2014Q4 =ts.get_profit_data(2014,4)
	profit_2014Q4.to_sql('profit_2014Q4',ENGINE,if_exists='append')

	profit_2015Q1 =ts.get_profit_data(2015,1)
	profit_2015Q1.to_sql('profit_2015Q1',ENGINE,if_exists='append')
	profit_2015Q2 =ts.get_profit_data(2015,2)
	profit_2015Q2.to_sql('profit_2015Q2',ENGINE,if_exists='append')
	profit_2015Q3 =ts.get_profit_data(2015,3)
	profit_2015Q3.to_sql('profit_2015Q3',ENGINE,if_exists='append')
	profit_2015Q4 =ts.get_profit_data(2015,4)
	profit_2015Q4.to_sql('profit_2015Q4',ENGINE,if_exists='append')

	profit_2016Q1 =ts.get_profit_data(2016,1)
	profit_2016Q1.to_sql('profit_2016Q1',ENGINE,if_exists='append')
	profit_2016Q2 =ts.get_profit_data(2016,2)
	profit_2016Q2.to_sql('profit_2016Q2',ENGINE,if_exists='append')
	# profit_2016Q3 =ts.get_profit_data(2016,3)
	# profit_2016Q3.to_sql('profit_2016Q3',ENGINE,if_exists='append')
	# profit_2016Q4 =ts.get_profit_data(2016,4)
	# profit_2016Q4.to_sql('profit_2016Q4',ENGINE,if_exists='append')

def getoperationdb():
	operation_2010Q1 = ts.get_operation_data(2010,1)
	operation_2010Q1.to_sql('operation_2010Q1',ENGINE,if_exists='append')
	operation_2010Q2 = ts.get_operation_data(2010,2)
	operation_2010Q2.to_sql('operation_2010Q2',ENGINE,if_exists='append')
	operation_2010Q3 = ts.get_operation_data(2010,3)
	operation_2010Q3.to_sql('operation_2010Q3',ENGINE,if_exists='append')
	operation_2010Q4 = ts.get_operation_data(2010,4)
	operation_2010Q4.to_sql('operation_2010Q4',ENGINE,if_exists='append')

	operation_2011Q1 = ts.get_operation_data(2011,1)
	operation_2011Q1.to_sql('operation_2011Q1',ENGINE,if_exists='append')
	operation_2011Q2 = ts.get_operation_data(2011,2)
	operation_2011Q2.to_sql('operation_2011Q2',ENGINE,if_exists='append')
	operation_2011Q3 = ts.get_operation_data(2011,3)
	operation_2011Q3.to_sql('operation_2011Q3',ENGINE,if_exists='append')
	operation_2011Q4 = ts.get_operation_data(2011,4)
	operation_2011Q4.to_sql('operation_2011Q4',ENGINE,if_exists='append')

	operation_2012Q1 = ts.get_operation_data(2012,1)
	operation_2012Q1.to_sql('operation_2012Q1',ENGINE,if_exists='append')
	operation_2012Q2 = ts.get_operation_data(2012,2)
	operation_2012Q2.to_sql('operation_2012Q2',ENGINE,if_exists='append')
	operation_2012Q3 = ts.get_operation_data(2012,3)
	operation_2012Q3.to_sql('operation_2012Q3',ENGINE,if_exists='append')
	operation_2012Q4 = ts.get_operation_data(2012,4)
	operation_2012Q4.to_sql('operation_2012Q4',ENGINE,if_exists='append')

	operation_2013Q1 = ts.get_operation_data(2013,1)
	operation_2013Q1.to_sql('operation_2013Q1',ENGINE,if_exists='append')
	operation_2013Q2 = ts.get_operation_data(2013,2)
	operation_2013Q2.to_sql('operation_2013Q2',ENGINE,if_exists='append')
	operation_2013Q3 = ts.get_operation_data(2013,3)
	operation_2013Q3.to_sql('operation_2013Q3',ENGINE,if_exists='append')
	operation_2013Q4 = ts.get_operation_data(2013,4)
	operation_2013Q4.to_sql('operation_2013Q4',ENGINE,if_exists='append')

	operation_2014Q1 = ts.get_operation_data(2014,1)
	operation_2014Q1.to_sql('operation_2014Q1',ENGINE,if_exists='append')
	operation_2014Q2 = ts.get_operation_data(2014,2)
	operation_2014Q2.to_sql('operation_2014Q2',ENGINE,if_exists='append')
	operation_2014Q3 = ts.get_operation_data(2014,3)
	operation_2014Q3.to_sql('operation_2014Q3',ENGINE,if_exists='append')
	operation_2014Q4 = ts.get_operation_data(2014,4)
	operation_2014Q4.to_sql('operation_2014Q4',ENGINE,if_exists='append')

	operation_2015Q1 = ts.get_operation_data(2015,1)
	operation_2015Q1.to_sql('operation_2015Q1',ENGINE,if_exists='append')
	operation_2015Q2 = ts.get_operation_data(2015,2)
	operation_2015Q2.to_sql('operation_2015Q2',ENGINE,if_exists='append')
	operation_2015Q3 = ts.get_operation_data(2015,3)
	operation_2015Q3.to_sql('operation_2015Q3',ENGINE,if_exists='append')
	operation_2015Q4 = ts.get_operation_data(2015,4)
	operation_2015Q4.to_sql('operation_2015Q4',ENGINE,if_exists='append')

	operation_2016Q1 = ts.get_operation_data(2016,1)
	operation_2016Q1.to_sql('operation_2016Q1',ENGINE,if_exists='append')
	operation_2016Q2 = ts.get_operation_data(2016,2)
	operation_2016Q2.to_sql('operation_2016Q2',ENGINE,if_exists='append')
	# operation_2016Q3 = ts.get_operation_data(2016,3)
	# operation_2016Q3.to_sql('operation_2016Q3',ENGINE,if_exists='append')
	# operation_2016Q4 = ts.get_operation_data(2016,4)
	# operation_2016Q4.to_sql('operation_2016Q4',ENGINE,if_exists='append')

#成长能力数据
def getgrowthdb():
	growth_2010Q1= ts.get_growth_data(2010,1)
	growth_2010Q1.to_sql('growth_2010Q1',ENGINE,if_exists='append')
	growth_2010Q2= ts.get_growth_data(2010,2)
	growth_2010Q2.to_sql('growth_2010Q2',ENGINE,if_exists='append')
	growth_2010Q3= ts.get_growth_data(2010,3)
	growth_2010Q3.to_sql('growth_2010Q3',ENGINE,if_exists='append')
	growth_2010Q4= ts.get_growth_data(2010,4)
	growth_2010Q4.to_sql('growth_2010Q4',ENGINE,if_exists='append')
	
	growth_2011Q1= ts.get_growth_data(2011,1)
	growth_2011Q1.to_sql('growth_2011Q1',ENGINE,if_exists='append')
	growth_2011Q2= ts.get_growth_data(2011,2)
	growth_2011Q2.to_sql('growth_2011Q2',ENGINE,if_exists='append')
	growth_2011Q3= ts.get_growth_data(2011,3)
	growth_2011Q3.to_sql('growth_2011Q3',ENGINE,if_exists='append')
	growth_2011Q4= ts.get_growth_data(2011,4)
	growth_2011Q4.to_sql('growth_2011Q4',ENGINE,if_exists='append')

	growth_2012Q1= ts.get_growth_data(2012,1)
	growth_2012Q1.to_sql('growth_2012Q1',ENGINE,if_exists='append')
	growth_2012Q2= ts.get_growth_data(2012,2)
	growth_2012Q2.to_sql('growth_2012Q2',ENGINE,if_exists='append')
	growth_2012Q3= ts.get_growth_data(2012,3)
	growth_2012Q3.to_sql('growth_2012Q3',ENGINE,if_exists='append')
	growth_2012Q4= ts.get_growth_data(2012,4)
	growth_2012Q4.to_sql('growth_2012Q4',ENGINE,if_exists='append')

	growth_2013Q1= ts.get_growth_data(2013,1)
	growth_2013Q1.to_sql('growth_2013Q1',ENGINE,if_exists='append')
	growth_2013Q2= ts.get_growth_data(2013,2)
	growth_2013Q2.to_sql('growth_2013Q2',ENGINE,if_exists='append')
	growth_2013Q3= ts.get_growth_data(2013,3)
	growth_2013Q3.to_sql('growth_2013Q3',ENGINE,if_exists='append')
	growth_2013Q4= ts.get_growth_data(2013,4)
	growth_2013Q4.to_sql('growth_2013Q4',ENGINE,if_exists='append')

	growth_2014Q1= ts.get_growth_data(2014,1)
	growth_2014Q1.to_sql('growth_2014Q1',ENGINE,if_exists='append')
	growth_2014Q2= ts.get_growth_data(2014,2)
	growth_2014Q2.to_sql('growth_2014Q2',ENGINE,if_exists='append')
	growth_2014Q3= ts.get_growth_data(2014,3)
	growth_2014Q3.to_sql('growth_2014Q3',ENGINE,if_exists='append')
	growth_2014Q4= ts.get_growth_data(2014,4)
	growth_2014Q4.to_sql('growth_2014Q4',ENGINE,if_exists='append')

	growth_2015Q1= ts.get_growth_data(2015,1)
	growth_2015Q1.to_sql('growth_2015Q1',ENGINE,if_exists='append')
	growth_2015Q2= ts.get_growth_data(2015,2)
	growth_2015Q2.to_sql('growth_2015Q2',ENGINE,if_exists='append')
	growth_2015Q3= ts.get_growth_data(2015,3)
	growth_2015Q3.to_sql('growth_2015Q3',ENGINE,if_exists='append')
	growth_2015Q4= ts.get_growth_data(2015,4)
	growth_2015Q4.to_sql('growth_2015Q4',ENGINE,if_exists='append')

	growth_2016Q1= ts.get_growth_data(2016,1)
	growth_2016Q1.to_sql('growth_2016Q1',ENGINE,if_exists='append')
	growth_2016Q2= ts.get_growth_data(2016,2)
	growth_2016Q2.to_sql('growth_2016Q2',ENGINE,if_exists='append')
	# growth_2016Q3= ts.get_growth_data(2016,3)
	# growth_2016Q3.to_sql('growth_2016Q3',ENGINE,if_exists='append')
	# growth_2016Q4= ts.get_growth_data(2016,4)
	# growth_2016Q4.to_sql('growth_2016Q4',ENGINE,if_exists='append')

def getdebtpayingdb():
	debtpaying_2010Q1= ts.get_debtpaying_data(2010,1)
	debtpaying_2010Q1.to_sql('debtpaying_2010Q1',ENGINE,if_exists='append')
	debtpaying_2010Q2= ts.get_debtpaying_data(2010,2)
	debtpaying_2010Q2.to_sql('debtpaying_2010Q2',ENGINE,if_exists='append')
	debtpaying_2010Q3= ts.get_debtpaying_data(2010,3)
	debtpaying_2010Q3.to_sql('debtpaying_2010Q3',ENGINE,if_exists='append')
	debtpaying_2010Q4= ts.get_debtpaying_data(2010,4)
	debtpaying_2010Q4.to_sql('debtpaying_2010Q4',ENGINE,if_exists='append')
	
	debtpaying_2011Q1= ts.get_debtpaying_data(2011,1)
	debtpaying_2011Q1.to_sql('debtpaying_2011Q1',ENGINE,if_exists='append')
	debtpaying_2011Q2= ts.get_debtpaying_data(2011,2)
	debtpaying_2011Q2.to_sql('debtpaying_2011Q2',ENGINE,if_exists='append')
	debtpaying_2011Q3= ts.get_debtpaying_data(2011,3)
	debtpaying_2011Q3.to_sql('debtpaying_2011Q3',ENGINE,if_exists='append')
	debtpaying_2011Q4= ts.get_debtpaying_data(2011,4)
	debtpaying_2011Q4.to_sql('debtpaying_2011Q4',ENGINE,if_exists='append')

	debtpaying_2012Q1= ts.get_debtpaying_data(2012,1)
	debtpaying_2012Q1.to_sql('debtpaying_2012Q1',ENGINE,if_exists='append')
	debtpaying_2012Q2= ts.get_debtpaying_data(2012,2)
	debtpaying_2012Q2.to_sql('debtpaying_2012Q2',ENGINE,if_exists='append')
	debtpaying_2012Q3= ts.get_debtpaying_data(2012,3)
	debtpaying_2012Q3.to_sql('debtpaying_2012Q3',ENGINE,if_exists='append')
	debtpaying_2012Q4= ts.get_debtpaying_data(2012,4)
	debtpaying_2012Q4.to_sql('debtpaying_2012Q4',ENGINE,if_exists='append')

	debtpaying_2013Q1= ts.get_debtpaying_data(2013,1)
	debtpaying_2013Q1.to_sql('debtpaying_2013Q1',ENGINE,if_exists='append')
	debtpaying_2013Q2= ts.get_debtpaying_data(2013,2)
	debtpaying_2013Q2.to_sql('debtpaying_2013Q2',ENGINE,if_exists='append')
	debtpaying_2013Q3= ts.get_debtpaying_data(2013,3)
	debtpaying_2013Q3.to_sql('debtpaying_2013Q3',ENGINE,if_exists='append')
	debtpaying_2013Q4= ts.get_debtpaying_data(2013,4)
	debtpaying_2013Q4.to_sql('debtpaying_2013Q4',ENGINE,if_exists='append')

	debtpaying_2014Q1= ts.get_debtpaying_data(2014,1)
	debtpaying_2014Q1.to_sql('debtpaying_2014Q1',ENGINE,if_exists='append')
	debtpaying_2014Q2= ts.get_debtpaying_data(2014,2)
	debtpaying_2014Q2.to_sql('debtpaying_2014Q2',ENGINE,if_exists='append')
	debtpaying_2014Q3= ts.get_debtpaying_data(2014,3)
	debtpaying_2014Q3.to_sql('debtpaying_2014Q3',ENGINE,if_exists='append')
	debtpaying_2014Q4= ts.get_debtpaying_data(2014,4)
	debtpaying_2014Q4.to_sql('debtpaying_2014Q4',ENGINE,if_exists='append')

	debtpaying_2015Q1= ts.get_debtpaying_data(2015,1)
	debtpaying_2015Q1.to_sql('debtpaying_2015Q1',ENGINE,if_exists='append')
	debtpaying_2015Q2= ts.get_debtpaying_data(2015,2)
	debtpaying_2015Q2.to_sql('debtpaying_2015Q2',ENGINE,if_exists='append')
	debtpaying_2015Q3= ts.get_debtpaying_data(2015,3)
	debtpaying_2015Q3.to_sql('debtpaying_2015Q3',ENGINE,if_exists='append')
	debtpaying_2015Q4= ts.get_debtpaying_data(2015,4)
	debtpaying_2015Q4.to_sql('debtpaying_2015Q4',ENGINE,if_exists='append')

	debtpaying_2016Q1= ts.get_debtpaying_data(2016,1)
	debtpaying_2016Q1.to_sql('debtpaying_2016Q1',ENGINE,if_exists='append')
	debtpaying_2016Q2= ts.get_debtpaying_data(2016,2)
	debtpaying_2016Q2.to_sql('debtpaying_2016Q2',ENGINE,if_exists='append')
	# debtpaying_2016Q3= ts.get_debtpaying_data(2016,3)
	# debtpaying_2016Q3.to_sql('debtpaying_2016Q3',ENGINE,if_exists='append')
	# debtpaying_2016Q4= ts.get_debtpaying_data(2016,4)
	# debtpaying_2016Q4.to_sql('debtpaying_2016Q4',ENGINE,if_exists='append')

def getcashflowdb():
	cashflow_2010Q1= ts.get_cashflow_data(2010,1)
	cashflow_2010Q1.to_sql('cashflow_2010Q1',ENGINE,if_exists='append')
	cashflow_2010Q2= ts.get_cashflow_data(2010,2)
	cashflow_2010Q2.to_sql('cashflow_2010Q2',ENGINE,if_exists='append')
	cashflow_2010Q3= ts.get_cashflow_data(2010,3)
	cashflow_2010Q3.to_sql('cashflow_2010Q3',ENGINE,if_exists='append')
	cashflow_2010Q4= ts.get_cashflow_data(2010,4)
	cashflow_2010Q4.to_sql('cashflow_2010Q4',ENGINE,if_exists='append')
	
	cashflow_2011Q1= ts.get_cashflow_data(2011,1)
	cashflow_2011Q1.to_sql('cashflow_2011Q1',ENGINE,if_exists='append')
	cashflow_2011Q2= ts.get_cashflow_data(2011,2)
	cashflow_2011Q2.to_sql('cashflow_2011Q2',ENGINE,if_exists='append')
	cashflow_2011Q3= ts.get_cashflow_data(2011,3)
	cashflow_2011Q3.to_sql('cashflow_2011Q3',ENGINE,if_exists='append')
	cashflow_2011Q4= ts.get_cashflow_data(2011,4)
	cashflow_2011Q4.to_sql('cashflow_2011Q4',ENGINE,if_exists='append')

	cashflow_2012Q1= ts.get_cashflow_data(2012,1)
	cashflow_2012Q1.to_sql('cashflow_2012Q1',ENGINE,if_exists='append')
	cashflow_2012Q2= ts.get_cashflow_data(2012,2)
	cashflow_2012Q2.to_sql('cashflow_2012Q2',ENGINE,if_exists='append')
	cashflow_2012Q3= ts.get_cashflow_data(2012,3)
	cashflow_2012Q3.to_sql('cashflow_2012Q3',ENGINE,if_exists='append')
	cashflow_2012Q4= ts.get_cashflow_data(2012,4)
	cashflow_2012Q4.to_sql('cashflow_2012Q4',ENGINE,if_exists='append')

	cashflow_2013Q1= ts.get_cashflow_data(2013,1)
	cashflow_2013Q1.to_sql('cashflow_2013Q1',ENGINE,if_exists='append')
	cashflow_2013Q2= ts.get_cashflow_data(2013,2)
	cashflow_2013Q2.to_sql('cashflow_2013Q2',ENGINE,if_exists='append')
	cashflow_2013Q3= ts.get_cashflow_data(2013,3)
	cashflow_2013Q3.to_sql('cashflow_2013Q3',ENGINE,if_exists='append')
	cashflow_2013Q4= ts.get_cashflow_data(2013,4)
	cashflow_2013Q4.to_sql('cashflow_2013Q4',ENGINE,if_exists='append')

	cashflow_2014Q1= ts.get_cashflow_data(2014,1)
	cashflow_2014Q1.to_sql('cashflow_2014Q1',ENGINE,if_exists='append')
	cashflow_2014Q2= ts.get_cashflow_data(2014,2)
	cashflow_2014Q2.to_sql('cashflow_2014Q2',ENGINE,if_exists='append')
	cashflow_2014Q3= ts.get_cashflow_data(2014,3)
	cashflow_2014Q3.to_sql('cashflow_2014Q3',ENGINE,if_exists='append')
	cashflow_2014Q4= ts.get_cashflow_data(2014,4)
	cashflow_2014Q4.to_sql('cashflow_2014Q4',ENGINE,if_exists='append')

	cashflow_2015Q1= ts.get_cashflow_data(2015,1)
	cashflow_2015Q1.to_sql('cashflow_2015Q1',ENGINE,if_exists='append')
	cashflow_2015Q2= ts.get_cashflow_data(2015,2)
	cashflow_2015Q2.to_sql('cashflow_2015Q2',ENGINE,if_exists='append')
	cashflow_2015Q3= ts.get_cashflow_data(2015,3)
	cashflow_2015Q3.to_sql('cashflow_2015Q3',ENGINE,if_exists='append')
	cashflow_2015Q4= ts.get_cashflow_data(2015,4)
	cashflow_2015Q4.to_sql('cashflow_2015Q4',ENGINE,if_exists='append')

	cashflow_2016Q1= ts.get_cashflow_data(2016,1)
	cashflow_2016Q1.to_sql('cashflow_2016Q1',ENGINE,if_exists='append')
	cashflow_2016Q2= ts.get_cashflow_data(2016,2)
	cashflow_2016Q2.to_sql('cashflow_2016Q2',ENGINE,if_exists='append')
	# cashflow_2016Q3= ts.get_cashflow_data(2016,3)
	# cashflow_2016Q3.to_sql('cashflow_2016Q3',ENGINE,if_exists='append')
	# cashflow_2016Q4= ts.get_cashflow_data(2016,4)
	# cashflow_2016Q4.to_sql('cashflow_2016Q4',ENGINE,if_exists='append')

#存款利率
def getdepositdb():
	deposit=ts.get_deposit_rate()
	#print(deposit, sep=' ', end='\n', file=sys.stdout, flush=False)
	deposit.to_sql('deposit_data',ENGINE,if_exists='append')

#贷款利率
def getloanratedb():
	loanrate = ts.get_loan_rate()
	loanrate.to_sql('loanrate_data',ENGINE,if_exists='append')

#存款准备金率
def getrrrdb():
	rrr = ts.get_rrr()
	rrr.to_sql('rrr_data',ENGINE,if_exists='append')

#货币供应量
def getmoneysupplydb():
	moneysupply = ts.get_money_supply()
	moneysupply.to_sql('moneysupply_data',ENGINE,if_exists='append')

#货币供应量年底余额
def getmoneysupplybaldb():
	moneysupplybal = ts.get_money_supply_bal()
	moneysupplybal.to_sql('moneysupplybal_data',ENGINE,if_exists='append')

#国内生产总值-年度
def getgdpyeardb():
	gdpyear = ts.get_gdp_year()
	gdpyear.to_sql('gdpyear_db',ENGINE,if_exists='append')

#国内生产总值(季度)
def getgdpquarterdb():
	gdpquarter = ts.get_gdp_quarter()
	gdpquarter.to_sql('gdpquarter_data',ENGINE,if_exists='append')

#三大需求对GDP贡献
def getgdpfordb():
	gdpfor = ts.get_gdp_for()
	gdpfor.to_sql('gdpfor_data',ENGINE,if_exists='append')

def getgdppulldb():
	gdppull = ts.get_gdp_pull()
	gdppull.to_sql('gdppull_data',ENGINE,if_exists='append')

#三大产业贡献率
def getgdpcontribdb():
	gdpcontrib = ts.get_gdp_contrib()
	gdpcontrib.to_sql('gdpcontrib_data',ENGINE,if_exists = 'append')

#居民消费价格指数
def getcpidb():
	cpi = ts.get_cpi()
	cpi.to_sql('cpi_data',ENGINE,if_exists = 'append')

#工业品出厂价格指数
def getppidb():
	ppi = ts.get_ppi()
	ppi.to_sql('ppi_data',ENGINE,if_exists = 'append')

#基本面数据
if __name__ == '__main__':
	#沪深股票列表
	#getbasicdb()
	#业绩报告
	# getreportdb()
	#盈利能力数据
	# getprofitdb()
	#运营能力数据
	#getoperationdb()
	#成长能力数据
	# getgrowthdb()
	#偿债能力
	#getdebtpayingdb()
	#现金流
	# getcashflowdb()
	#存款利率
	#getdepositdb()
	#贷款利率
	#getloanratedb()
	#存款准备金率
	#getrrrdb()
	#货币供应量
	# getmoneysupplydb()
	#货币供应量（年底余额）
	# getmoneysupplybaldb()
	#国内生产总值-年度
	#getgdpyeardb()
	#国内生产总值-季度
	# getgdpquarterdb()
	#三大需求对GDP贡献
	# getgdpfordb()
	#三大产业对GDP拉动
	# getgdppulldb()
	#三大产业贡献率
	# getgdpcontribdb()
	#居民消费价格指数
	# getcpidb()
	#工业品出厂价格指数
	# getppidb()
