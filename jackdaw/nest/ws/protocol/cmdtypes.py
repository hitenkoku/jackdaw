import enum

class NestOpCmd(enum.Enum):
	GATHER = 'GATHER'
	KERBEROAST = 'KERBEROAST'
	SMBSESSIONS = 'SMBSESSIONS'
	PATHSHORTEST = 'PATHSHORTEST'
	PATHDA = 'PATHDA'
	GETOBJINFO = 'GETOBJINFO'
	CHANGEAD = 'CHANGEAD'
	LISTADS = 'LISTADS'
	OK = 'OK'
	ERR = 'ERR'
	LOG = 'LOG'
	LISTGRAPHS = 'LISTGRAPHS'
	CHANGEGRAPH = 'CHANGEGRAPH'
	TCPSCAN = 'TCPSCAN'
	TCPSCANRES = 'TCPSCANRES'
	LISTADSRES = 'LISTADSRES'
	PATHRES = 'PATHRES'
	GATHERSTATUS = 'GATHERSTATUS'
	USERRES = 'USERRES'
	COMPUTERRES = 'COMPUTERRES'
	SMBSESSIONRES = 'SMBSESSIONRES'
	SMBSHARERES	= 'SMBSHARERES'
	SMBLOCALGROUPRES = 'SMBLOCALGROUPRES'
	LOADAD = 'LOADAD'
	GROUPRES = 'GROUPRES'
	

