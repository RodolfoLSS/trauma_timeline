def main():
	import pypyodbc
	import sys

	# Database connection
	print('Trying to connect to the database...')

	try:
		myConnection = pypyodbc.connect('Driver={SQL Server};'
									'Server=localhost;'
									'Database=Trauma2;'
									'uid=Rodolfo;pwd=Trauma2')
		myCursor = myConnection.cursor()
		print('Connected.')
	except:
		print('Could not connect:', sys.exc_info()[0])

	tableName = input('Table name: ')

	if tableName == 'AcctHist':
		getTuplesFromAcctHist(myCursor)
	elif tableName == 'ADM_INPT':
		getTuplesFromAdm_inpt(myCursor)
	elif tableName == 'BURNS': 
		getTuplesFromBurns(myCursor)
	elif tableName == 'comments': 
		getTuplesFromComments(myCursor) 
	elif tableName == 'CONSULT': 
		getTuplesFromConsult(myCursor)
	elif tableName == 'CULTURE': 
		getTuplesFromCulture(myCursor)
	elif tableName == 'dellog': 
		getTuplesFromDellog(myCursor)
	elif tableName == 'DIAGS': 
		getTuplesFromDiags(myCursor)
	elif tableName == 'EMERG':
	    getTuplesFromEmerg(myCursor)
	elif tableName == 'FINANCE': 
		getTuplesFromFinance(myCursor)
	elif tableName == 'FLDDETAI': 
		getTuplesFromFlddetai(myCursor)
	elif tableName == 'GENMECH': 
		getTuplesFromGenmech(myCursor)
	elif tableName == 'HEMO': 
		getTuplesFromHemo(myCursor)
	elif tableName == 'HOSPREV':
		getTuplesFromHosprev(myCursor)
	elif tableName == 'ICU':
		getTuplesFromIcu(myCursor)
	elif tableName == 'INJDETS':
		getTuplesFromInjdets(myCursor)
	elif tableName == 'INJDIAG':
		getTuplesFromInjdiag(myCursor)
	elif tableName == 'INJMECH':
		getTuplesFromInjmech(myCursor)
	elif tableName == 'LAB':
		getTuplesFromLab(myCursor)
	elif tableName == 'MAINDATA':
		getTuplesFromMaindata(myCursor)
	elif tableName == 'MORTDETS':
		getTuplesFromMortdets(myCursor)
	elif tableName == 'MTOS':
		getTuplesFromMtos(myCursor)
	elif tableName == 'NARRATIV':
		getTuplesFromNarrativ(myCursor)
	elif tableName == 'OPRM':
		getTuplesFromOprm(myCursor)
	elif tableName == 'ORGANS':
		getTuplesFromOrgans(myCursor)
	elif tableName == 'PERHIST':
		getTuplesFromPerhist(myCursor)
	elif tableName == 'POSTHOSP':
		getTuplesFromPosthosp(myCursor)
	elif tableName == 'PRECONDS':
		getTuplesFromPreconds(myCursor)
	elif tableName == 'PROTECT':
		getTuplesFromProtect(myCursor)
	elif tableName == 'QAISSUE':
		getTuplesFromQaissue(myCursor)
	elif tableName == 'RADIOLOG':
		getTuplesFromRadiolog(myCursor)
	elif tableName == 'READMIT':
		getTuplesFromReadmit(myCursor)
	elif tableName == 'STEP':
		getTuplesFromStep(myCursor)
	elif tableName == 'SURG':
		getTuplesFromSurg(myCursor)
	elif tableName == 'sysdefs':
		getTuplesFromSysdefs(myCursor)
	elif tableName == 'TLogComm':
		getTuplesFromTLogComm(myCursor)
	elif tableName == 'TOXIANAL':
		getTuplesFromToxianal(myCursor)
	elif tableName == 'TRA':
		getTuplesFromTra(myCursor)
	elif tableName == 'tranlog':
		getTuplesFromTranlog(myCursor)
	elif tableName == 'TRANSFER':
		getTuplesFromTransfer(myCursor)
	elif tableName == 'TRANSPRT':
		getTuplesFromTransprt(myCursor)
	elif tableName == 'TREATMEN':
		getTuplesFromTreatmen(myCursor)
	elif tableName == 'TRICRIT':
		getTuplesFromTricrit(myCursor)
	elif tableName == 'TRMTEAM':
		getTuplesFromTrmteam(myCursor)
	elif tableName == 'TTDETLS':
		getTuplesFromTtdetls(myCursor)
	elif tableName == 'VITALS':
		getTuplesFromVitals(myCursor)
	elif tableName == 'WARD':
		getTuplesFromWard(myCursor)
	else: 
		print ('Type a valid table name.\n')

	myConnection.close()
	myCursor.close()

def getTuplesFromAcctHist(myCursor):
	print ('Testing AcctHist!') 

	# Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TRAUMA2.AcctHist')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[0])
			task = 'AcctHist'
			timestamp = str(row[2])
			otherAttributes = 'acctno = ' + str(row[1]) + ', acttime = ' + str(row[3]) + ', action = ' + str(row[4]) + ', acuser = ' + str(row[5]) + ', acstation = ' + str(row[6])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)
			
	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromAdm_inpt(myCursor):
	print('Testing ADM_INPT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.ADM_INPT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[34])
			task = 'ADM_INPT'
			timestamp = str(row[2])
			otherAttributes =  'PT_LOCAT = ' + str(row[0]) + ', ROOM_NO = ' + str(row[1]) + ', DATE_OUT = ' + str(row[3]) + ', PROVDER_IN = ' + str(row[4]) + ', LOS_IN = ' + str(row[5]) + ', CAREPHASE = ' + str(row[6]) + ', DUMFLD1 = ' + str(row[7]) + ', DUMFLD2 = ' + str(row[8]) + ', DUMFLD3 = ' + str(row[9]) + ', DUMFLD4 = ' + str(row[10]) + ', DUMFLD5 = ' + str(row[11]) + ', DUMFLD6 = ' + str(row[12]) + ', DUMFLD7 = ' + str(row[13]) + ', DUMFLD8 = ' + str(row[14]) + ', DUMFLD9 = ' + str(row[15]) + ', DUMFLD10 = ' + str(row[16]) + ', DUMFLD11 = ' + str(row[17]) + ', DUMFLD12 = ' + str(row[18]) + ', DUMFLD13 = ' + str(row[19]) + ', DUMFLD14 = ' + str(row[20]) + ', DUMFLD15 = ' + str(row[21]) + ', DUMFLD16 = ' + str(row[22]) + ', DUMFLD17 = ' + str(row[23]) + ', DUMFLD18 = ' + str(row[24]) + ', DUMFLD19 = ' + str(row[25]) + ', DUMFLD20 = ' + str(row[26]) + ', INPT_SER = ' + str(row[27]) + ', ACCTNO = ' + str(row[28]) + ', DE_STATUS = ' + str(row[29]) + ', DECOMMFLAG = ' + str(row[30]) + ', PARENTID = ' + str(row[31]) + ', PARENTREC = ' + str(row[32]) + ', COPYNO = ' + str(row[33])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromBurns(myCursor):
	print('Testing BURNS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.BURNS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[30])
			task = 'BURNS'
			timestamp = 'None'
			otherAttributes = 'PART_BURN = ' + str(row[0]) + ', PERC_BURN = ' + str(row[1]) + ', PHASE_COPY = ' + str(row[2]) + ', CAREPHASE = ' + str(row[3]) + ', DUMFLD1 = ' + str(row[4]) + ', DUMFLD2 = ' + str(row[5]) + ', DUMFLD3 = ' + str(row[6]) + ', DUMFLD4 = ' + str(row[7]) + ', DUMFLD5 = ' + str(row[8]) + ', DUMFLD6 = ' + str(row[9]) + ', DUMFLD7 = ' + str(row[10]) + ', DUMFLD8 = ' + str(row[11]) + ', DUMFLD9 = ' + str(row[12]) + ', DUMFLD10 = ' + str(row[13]) + ', DUMFLD11 = ' + str(row[14]) + ', DUMFLD12 = ' + str(row[15]) + ', DUMFLD13 = ' + str(row[16]) + ', DUMFLD14 = ' + str(row[17]) + ', DUMFLD15 = ' + str(row[18]) + ', DUMFLD16 = ' + str(row[19]) + ', DUMFLD17 = ' + str(row[20]) + ', DUMFLD18 = ' + str(row[21]) + ', DUMFLD19 = ' + str(row[22]) + ', DUMFLD20 = ' + str(row[23]) + ', ACCTNO = ' + str(row[24])  + ', DE_STATUS = ' + str(row[25])  + ', DECOMMFLAG = ' + str(row[26]) + ', PARENTID = ' + str(row[27]) + ', PARENTREC = ' + str(row[28])  + ', COPYNO = ' + str(row[29])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromComments(myCursor): # PROBLEM WITH A CHARACTER IN otherAttributes
	print('Testing comments!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.comments')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[1])
			task = 'comments'
			timestamp = 'NULL'
			otherAttributes = 'fileid = ' + str(row[0]) + ', fieldname = ' + str(row[2]) + ', ccomment = ' + str(row[3]) #+ ', cimage = ' + str(results[4]) + ', copyno = ' + str(results[5]) + ', acctno = ' + str(results[6])
			#otherAttributes = 'Teste'
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromConsult(myCursor):
	print('Testing CONSULT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.CONSULT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'CONSULT'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', TIME = ' + str(row[2]) + ', PROBLEMS = ' + str(row[3]) + ', CNSLT_DOC = ' + str(row[4]) + ', SPECIALITY = ' + str(row[5]) + ', REQ_DATE = ' + str(row[6]) + ', DOC_REQ = ' + str(row[7]) + ', MMCALL = ' + str(row[8]) + ', PHNE_RSP = ' + str(row[9]) + ', DEP_TIME = ' + str(row[10]) + ', TT_OTHER = ' + str(row[11]) + ', PHASE_COPY = ' + str(row[12]) + ', DUMFLD1 = ' + str(row[13]) + ', DUMFLD2 = ' + str(row[14]) + ', DUMFLD3 = ' + str(row[15]) + ', DUMFLD4 = ' + str(row[16]) + ', DUMFLD5 = ' + str(row[17]) + ', DUMFLD6 = ' + str(row[18]) + ', DUMFLD7 = ' + str(row[19]) + ', DUMFLD8 = ' + str(row[20]) + ', DUMFLD9 = ' + str(row[21]) + ', DUMFLD10 = ' + str(row[22]) + ', DUMFLD11 = ' + str(row[23]) + ', DUMFLD12 = ' + str(row[24]) + ', DUMFLD13 = ' + str(row[25]) + ', DUMFLD14 = ' + str(row[26]) + ', DUMFLD15 = ' + str(row[27]) + ', DUMFLD16 = ' + str(row[28]) + ', DUMFLD17 = ' + str(row[29]) + ', DUMFLD18 = ' + str(row[30]) + ', DUMFLD19 = ' + str(row[31]) + ', DUMFLD20 = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromCulture(myCursor):
	print('Testing CULTURE!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.CULTURE')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[38])
			task = 'CULTURE'
			timestamp = 'None'
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORD_DATE = ' + str(row[1]) + ', ORD_TIME = ' + str(row[2]) + ', DRAW_DATE = ' + str(row[3]) + ', DRAW_TIME = ' + str(row[4]) + ', ORD_BY = ' + str(row[5]) + ', RESLT_DATE = ' + str(row[6]) + ', RESLT_TIME = ' + str(row[7]) + ', DESCRIPT = ' + str(row[8]) + ', CULT_SITE = ' + str(row[9]) + ', CULT_BUG = ' + str(row[10]) + ', PHASE_COPY = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromDellog(myCursor): # PROBLEM WITH A CHARACTER IN otherAttributes
	print('Testing dellog!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TRAUMA2.dellog')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[0])
			task = 'dellog'
			timestamp = str(row[11])
			otherAttributes = 'acctno = ' + str(row[1]) + ', acc_path = ' + str(row[2]) + ', copyid = ' + str(row[3]) + ', action = ' + str(row[4]) + ', fieldname = ' + str(row[5]) + ', fieldtype = ' + str(row[6]) + ', fieldval = ' + str(row[7]) + ', fieldstat = ' + str(row[8]) + ', memofldval = ' + str(row[9]) + ', genfldval = ' + str(row[10]) + ', trantime = ' + str(row[12]) + ', tranuser = ' + str(row[13]) + ', transtn = ' + str(row[14])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromDiags(myCursor):
	print('Testing DIAGS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.DIAGS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'DIAGS'
			timestamp = 'None'
			otherAttributes = 'DIAG_T_BSA = ' + str(row[0]) + ', CAREPHASE = ' + str(row[1]) + ', TIME = ' + str(row[3]) + ', AIS_FACE = ' + str(row[4]) + ', AIS_HEAD = ' + str(row[5]) + ', AIS_ABD = ' + str(row[6]) + ', AIS_EXTRMY = ' + str(row[7]) + ', AIS_CHEST = ' + str(row[8]) + ', AIS_EXTRNL = ' + str(row[9]) + ', DRG_DX = ' + str(row[10]) + ', PHASE_COPY = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', NISS = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromEmerg(myCursor):
	print('Testing EMERG!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.EMERG')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[69])
			task = 'EMERG'
			timestamp = 'None'
			otherAttributes = 'EM_NOTIFID = ' + str(row[0]) + ', EM_NOTF_DT = ' + str(row[1]) + ', EM_NOTF_TM = ' + str(row[2]) + ', EM_DOA = ' + str(row[3]) + ', EM_MJR = ' + str(row[4]) + ', EM_ENT_DT = ' + str(row[5]) + ', EM_ENT_TM = ' + str(row[6]) + ', EM_EXIT_DT = ' + str(row[7]) + ', EM_EXIT_TM = ' + str(row[8]) + ', EM_ENT_FRM = ' + str(row[9]) + ', EM_EXIT_TO = ' + str(row[10]) + ', EM_ADM_TYP = ' + str(row[11]) + ', EM_ADM_SRC = ' + str(row[12]) + ', EM_DISPO = ' + str(row[13]) + ', EM_LFT_VIA = ' + str(row[14]) + ', EM_REBG_TM = ' + str(row[15]) + ', EM_REEN_TM = ' + str(row[16]) + ', EM_DOCTOR = ' + str(row[17]) + ', EM_SERVICE = ' + str(row[18]) + ', EM_UNCPROB = ' + str(row[19]) + ', EM_LOS = ' + str(row[20]) + ', EM_SUB_CT = ' + str(row[21]) + ', EM_SEV_HD = ' + str(row[22]) + ', TM_CT = ' + str(row[23]) + ', R_TOT_TME = ' + str(row[24]) + ', IVFLUIDS = ' + str(row[25]) + ', BLOODPRO = ' + str(row[26]) + ', AUTOTRANS = ' + str(row[27]) + ', TOTIVBLD = ' + str(row[28]) + ', HEADCTTM = ' + str(row[29]) + ', HEADCTRES = ' + str(row[30]) + ', CSPINETM = ' + str(row[31]) + ', CSPINERES = ' + str(row[32]) + ', ETTTIME = ' + str(row[33]) + ', ERTHORTIME = ' + str(row[34]) + ', DPLTIME = ' + str(row[35]) + ', CHTUBELTM = ' + str(row[36]) + ', CHTUBERTM = ' + str(row[37]) + ', CRICHTIME = ' + str(row[38]) + ', TRACHTIME = ' + str(row[39]) + ', TOX = ' + str(row[40]) + ', SIGNSLIFE = ' + str(row[41]) + ', DUMFLD2 = ' + str(row[42]) + ', DUMFLD3 = ' + str(row[43]) + ', DUMFLD4 = ' + str(row[44]) + ', DUMFLD5 = ' + str(row[45]) + ', DUMFLD6 = ' + str(row[46]) + ', DUMFLD7 = ' + str(row[47]) + ', DUMFLD8 = ' + str(row[48]) + ', DUMFLD9 = ' + str(row[49]) + ', DUMFLD10 = ' + str(row[50]) + ', DUMFLD11 = ' + str(row[51]) + ', DUMFLD12 = ' + str(row[52]) + ', DUMFLD13 = ' + str(row[53]) + ', DUMFLD14 = ' + str(row[54]) + ', DUMFLD15 = ' + str(row[55]) + ', DUMFLD16 = ' + str(row[56]) + ', DUMFLD17 = ' + str(row[57]) + ', DUMFLD18 = ' + str(row[58]) + ', DUMFLD19 = ' + str(row[59]) + ', DUMFLD20 = ' + str(row[60]) + ', E_AR_FROM = ' + str(row[61]) + ', E_TRANSPOR = ' + str(row[62]) + ', ACCTNO = ' + str(row[63]) + ', DE_STATUS = ' + str(row[64]) + ', DECOMMFLAG = ' + str(row[65]) + ', PARENTID = ' + str(row[66]) + ', PARENTREC = ' + str(row[67]) + ', COPYNO = ' + str(row[68])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromFinance(myCursor):
	print('Testing FINANCE!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.FINANCE')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[40])
			task = 'FINANCE'
			timestamp = 'None'
			otherAttributes = 'T_HOS_COST = ' + str(row[0]) + ', T_HOS_CHRG = ' + str(row[1]) + ', T_HOS_BILL = ' + str(row[2]) + ', T_HOS_RECP = ' + str(row[3]) + ', T_PHY_COST = ' + str(row[4]) + ', T_PHY_CHRG = ' + str(row[5]) + ', T_PHY_BILL = ' + str(row[6]) + ', T_PHY_RECP = ' + str(row[7]) + ', CHG_PRLS = ' + str(row[8]) + ', CST_PRLS = ' + str(row[9]) + ', VVC_APP = ' + str(row[10]) + ', TT_REIM = ' + str(row[11]) + ', TT_ADDL = ' + str(row[12]) + ', TT_TOTAL = ' + str(row[13]) + ', DUMFLD1 = ' + str(row[14]) + ', DUMFLD2 = ' + str(row[15]) + ', DUMFLD3 = ' + str(row[16]) + ', DUMFLD4 = ' + str(row[17]) + ', DUMFLD5 = ' + str(row[18]) + ', DUMFLD6 = ' + str(row[19]) + ', DUMFLD7 = ' + str(row[20]) + ', DUMFLD8 = ' + str(row[21]) + ', DUMFLD9 = ' + str(row[22]) + ', DUMFLD10 = ' + str(row[23]) + ', DUMFLD11 = ' + str(row[24]) + ', DUMFLD12 = ' + str(row[25]) + ', DUMFLD13 = ' + str(row[26]) + ', DUMFLD14 = ' + str(row[27]) + ', DUMFLD15 = ' + str(row[28]) + ', DUMFLD16 = ' + str(row[29]) + ', DUMFLD17 = ' + str(row[30]) + ', DUMFLD18 = ' + str(row[31]) + ', DUMFLD19 = ' + str(row[32]) + ', DUMFLD20 = ' + str(row[33]) + ', ACCTNO = ' + str(row[34]) + ', DE_STATUS = ' + str(row[35]) + ', DECOMMFLAG = ' + str(row[36]) + ', PARENTID = ' + str(row[37]) + ', PARENTREC = ' + str(row[38]) + ', COPYNO = ' + str(row[39])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromFlddetai(myCursor):
	print('Testing FLDDETAI!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.FLDDETAI')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'FLDDETAI'
			timestamp = str(row[0])
			otherAttributes = 'FL_ENT_TM = ' + str(row[1]) + ', TRM_LEVEL = ' + str(row[2]) + ', NUM_VICTIM = ' + str(row[3]) + ', PRE_FORM = ' + str(row[4]) + ', FL_EXIT_TO = ' + str(row[5]) + ', DESIG_BY = ' + str(row[6]) + ', TRIAGE = ' + str(row[7]) + ', PT_STATUS = ' + str(row[8]) + ', FL_UNCPROB = ' + str(row[9]) + ', RELFACTOR = ' + str(row[10]) + ', TPS_RATNL = ' + str(row[11]) + ', INTUBATE = ' + str(row[12]) + ', DUMFLD1 = ' + str(row[13]) + ', DUMFLD2 = ' + str(row[14]) + ', DUMFLD3 = ' + str(row[15]) + ', DUMFLD4 = ' + str(row[16]) + ', DUMFLD5 = ' + str(row[17]) + ', DUMFLD6 = ' + str(row[18]) + ', DUMFLD7 = ' + str(row[19]) + ', DUMFLD8 = ' + str(row[20]) + ', DUMFLD9 = ' + str(row[21]) + ', DUMFLD10 = ' + str(row[22]) + ', DUMFLD11 = ' + str(row[23]) + ', DUMFLD12 = ' + str(row[24]) + ', DUMFLD13 = ' + str(row[25]) + ', DUMFLD14 = ' + str(row[26]) + ', DUMFLD15 = ' + str(row[27]) + ', DUMFLD16 = ' + str(row[28]) + ', DUMFLD17 = ' + str(row[29]) + ', DUMFLD18 = ' + str(row[30]) + ', DUMFLD19 = ' + str(row[31]) + ', DUMFLD20 = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromGenmech(myCursor):
	print('Testing GENMECH!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.GENMECH')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[31])
			task = 'GENMECH'
			timestamp = 'None'
			otherAttributes = 'GEN_DSRPT = ' + str(row[0]) + ', ECODE_ICD9 = ' + str(row[1]) + ', MEC_DISCP = ' + str(row[2]) + ', E_ACTIVITY = ' + str(row[3]) + ', DUMFLD2 = ' + str(row[4]) + ', DUMFLD3 = ' + str(row[5]) + ', DUMFLD4 = ' + str(row[6]) + ', DUMFLD5 = ' + str(row[7]) + ', DUMFLD6 = ' + str(row[8]) + ', DUMFLD7 = ' + str(row[9]) + ', DUMFLD8 = ' + str(row[10]) + ', DUMFLD9 = ' + str(row[11]) + ', DUMFLD10 = ' + str(row[12]) + ', DUMFLD11 = ' + str(row[13]) + ', DUMFLD12 = ' + str(row[14]) + ', DUMFLD13 = ' + str(row[15]) + ', DUMFLD14 = ' + str(row[16]) + ', DUMFLD15 = ' + str(row[17]) + ', DUMFLD16 = ' + str(row[18]) + ', DUMFLD17 = ' + str(row[19]) + ', DUMFLD18 = ' + str(row[20]) + ', DUMFLD19 = ' + str(row[21]) + ', DUMFLD20 = ' + str(row[22]) + ', CDC_MOI = ' + str(row[23]) + ', CDC_INT = ' + str(row[24]) + ', ACCTNO = ' + str(row[25])  + ', DE_STATUS = ' + str(row[26])  + ', DECOMMFLAG = ' + str(row[27]) + ', PARENTID = ' + str(row[28]) + ', PARENTREC = ' + str(row[29])  + ', COPYNO = ' + str(row[30])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromHemo(myCursor):
	print('Testing HEMO!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.HEMO')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[56])
			task = 'HEMO'
			timestamp = 'None'
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORD_DATE = ' + str(row[1]) + ', ORD_TIME = ' + str(row[2]) + ', DRAW_DATE = ' + str(row[3]) + ', DRAW_TIME = ' + str(row[4]) + ', ORDER_BY = ' + str(row[5]) + ', RESLT_DATE = ' + str(row[6]) + ', RESLT_TIME = ' + str(row[7]) + ', DESCRIPT = ' + str(row[8]) + ', HEME_STPL = ' + str(row[9]) + ', HEME_STPL = ' + str(row[10]) + ', HEME_SICL = ' + str(row[11]) + ', HEME_RETC = ' + str(row[12]) + ', HEME_SED = ' + str(row[13]) + ', WBC_SEGS = ' + str(row[14]) + ', WBC_BANDS = ' + str(row[15]) + ', WBC_LYMPH = ' + str(row[16]) + ', WBC_MONO = ' + str(row[17]) + ', WBC_EOSIN = ' + str(row[18]) + ', WBC_BASO = ' + str(row[19]) + ', WBC_META = ' + str(row[20]) + ', WBC_MYELO = ' + str(row[21]) + ', WBC_ALYMPH = ' + str(row[22]) + ', HEME_HCT = ' + str(row[23]) + ', HEME_RBC = ' + str(row[24]) + ', HEME_MCV = ' + str(row[25]) + ', HEME_HGB = ' + str(row[26]) + ', HEME_MCH = ' + str(row[27]) + ', HEME_MCHC = ' + str(row[28]) + ', PHASE_COPY = ' + str(row[29]) + ', DUMFLD1 = ' + str(row[30]) + ', DUMFLD2 = ' + str(row[31]) + ', DUMFLD3 = ' + str(row[32]) + ', DUMFLD4 = ' + str(row[33]) + ', DUMFLD5 = ' + str(row[34]) + ', DUMFLD6 = ' + str(row[35]) + ', DUMFLD7 = ' + str(row[36]) + ', DUMFLD8 = ' + str(row[37]) + ', DUMFLD9 = ' + str(row[38]) + ', DUMFLD10 = ' + str(row[39]) + ', DUMFLD11 = ' + str(row[40]) + ', DUMFLD12 = ' + str(row[41]) + ', DUMFLD13 = ' + str(row[42]) + ', DUMFLD14 = ' + str(row[43]) + ', DUMFLD15 = ' + str(row[44]) + ', DUMFLD16 = ' + str(row[45]) + ', DUMFLD17 = ' + str(row[46]) + ', DUMFLD18 = ' + str(row[47]) + ', DUMFLD19 = ' + str(row[48]) + ', DUMFLD20 = ' + str(row[49]) + ', ACCTNO = ' + str(row[50]) + ', DE_STATUS = ' + str(row[51]) + ', DECOMMFLAG = ' + str(row[52]) + ', PARENTID = ' + str(row[53]) + ', PARENTREC = ' + str(row[54]) + ', COPYNO = ' + str(row[55])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

"""
def filter():

def output2File():
"""
if __name__ == '__main__':
	class Tuples:
		def __init__(self, patientId, task, timestamp, otherAttributes):
			self.patientId = patientId
			self.task = task
			self.timestamp = timestamp
			self.otherAttributes = otherAttributes
	main()