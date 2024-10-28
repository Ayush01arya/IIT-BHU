import xml.etree.ElementTree as ET

root = ET.Element('Dictionary')

e1 = ET.SubElement(root,'Alphabets')

e1.text = "ॊऀऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻऽािढ़फ़य़ॠॡॢॣॱॲॳॴॵॶॷॸॹॺॻॼॽॾ"

e2 = ET.SubElement(root,'sdefs')
e21 = ET.SubElement(e2,'sdef',n = "n",c="noun")
e22 = ET.SubElement(e2,'sdef',n = 'np',c="proper noun")
e27 = ET.SubElement(e2,'sdef',n = 'subj',c="Subject")
e28 = ET.SubElement(e2,'sdef',n = 'org',c="Organisation")
e29 = ET.SubElement(e2,'sdef',n = 'num',c="Numeral")
e30 = ET.SubElement(e2,'sdef',n = 'dat',c="Dative")
e33 = ET.SubElement(e2,'sdef',n = 'adv',c="Adverb")

def sdef(e2,N,C):
    e = ET.SubElement(e2,'sdefs',n=N,c=C)

sdef(e2,"det","Determiner")
sdef(e2,"e","Emphasis")
sdef(e2,"post","Postposition")
sdef(e2,"vblex","Verb")
sdef(e2,"frm","formal")
sdef(e2,"fam","familiar")
sdef(e2,"pol","Polite")
sdef(e2,"ref","Reflexive pronoun")
sdef(e2,"acc","accusative")
sdef(e2,"ins","Instrumental")
sdef(e2,"loc","Location")
sdef(e2,"rel",'Relative')
sdef(e2,"dem","Demonstrative")
sdef(e2,'ing','Interrogative')
sdef(e2,'obj','Objective')
sdef(e2,'prn','pronoun')
sdef(e2,'f','feminine')
sdef(e2,'m','masculine')
sdef(e2,'mf','masculine/feminine')
sdef(e2,'nt','neuter')
sdef(e2,'vaux','auxiliar verb')
sdef(e2,'sg','singular')
sdef(e2,'pl','plural')
sdef(e2,'sp','singular/plural')
sdef(e2,'nom','nominative')
sdef(e2,'obl','oblique')
sdef(e2,'pos','possessive')
sdef(e2,'qnt','quantitative')
sdef(e2,'ind','indefinite')
sdef(e2,'pr','preposition')
sdef(e2,'1','first person')
sdef(e2,'2','second person')
sdef(e2,'3','third person')
sdef(e2,'inf','infinitive')
sdef(e2,'pres','present tense')
sdef(e2, 'past','past tense')


# creating paradigm definition

pardefs = ET.SubElement(root,'pardefs')

###################################
# PUNCTUATIONS--SECTION
pardef1 = ET.SubElement(pardefs,'pardef',n='numeros')
def def_entry1(re,s,s1):
    e1 = ET.SubElement(pardef1,'e')
    re1 = ET.SubElement(e1,'re')
    re1.text = re
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    r = ET.SubElement(p1,'r')
    s = ET.SubElement(r,'s',n=s)
    s = ET.SubElement(r,'s',n=s1)

def_entry1("[0-9]+",'num','')
def_entry1("[०१२३४५६७८९]+([.,][०१२३४५६७८९]+)?",'num','ord')
def_entry1("[०१२३४५६७८९]+([.,][०१२३४५६७८९]+)?%",'num','percent')

pardef2 = ET.SubElement(pardefs,'pardef',n='separa')
pardef3 = ET.SubElement(pardefs,'pardef',n='guio')
pardef4 = ET.SubElement(pardefs,'pardef',n='coma')
def def_entry2(x,re,s):
    e1 = ET.SubElement(x,'e')
    re1 = ET.SubElement(e1,'re')
    re1.text = re
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    r = ET.SubElement(p1,'r')
    s = ET.SubElement(r,'s',n=s)

def_entry2(pardef2,"[.\?;:!।॥]",'sent')
def_entry2(pardef3,"[—\-]+",'guio')
def_entry2(pardef4,',','cm')

#######################################
# PARADIGM--NOUNS

def func_noun_entry(x,n1,n2,n3,n4,n5,n6,n7,n8):
    e1 = ET.SubElement(x,'e')
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    r = ET.SubElement(p1,'r')
    s1 = ET.SubElement(r,'s',n=n1)
    s2 = ET.SubElement(r,'s',n=n2)
    s3 = ET.SubElement(r,'s',n=n3)
    s4 = ET.SubElement(r,'s',n=n4)
    s5 = ET.SubElement(r,'s',n=n5)
    s6 = ET.SubElement(r,'s',n=n6)
    s7 = ET.SubElement(r,'s',n=n7)
    s8 = ET.SubElement(r,'s',n=n8)

    xml_string = ET.tostring(e1, encoding='unicode', xml_declaration=True,method='html')

    return xml_string

def func_noun_entry_wleft(x,l_text,n1,n2,n3,n4,n5,n6,n7,n8):
    e1 = ET.SubElement(x,'e')
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    l.text = l_text
    r = ET.SubElement(p1,'r')
    s1 = ET.SubElement(r,'s',n=n1)
    s2 = ET.SubElement(r,'s',n=n2)
    s3 = ET.SubElement(r,'s',n=n3)
    s4 = ET.SubElement(r,'s',n=n4)
    s5 = ET.SubElement(r,'s',n=n5)
    s6 = ET.SubElement(r,'s',n=n6)
    s7 = ET.SubElement(r,'s',n=n7)
    s8 = ET.SubElement(r,'s',n=n8)

    xml_string = ET.tostring(e1, encoding='unicode', method='html',xml_declaration=True)

    return xml_string

#######################################

##-- PARADIGM FILE NOUN_M

pardef5 = ET.SubElement(pardefs,'pardef',n='लड़िका_n_m')
func_noun_entry_wleft(pardef5,'','XX','n','m','sg','3','d','0','0')
func_noun_entry_wleft(pardef5,"न",'XX','n','m','pl','3','d','0','0')
func_noun_entry_wleft(pardef5,"",'XX','n','m','sg','3','o','0','0')
func_noun_entry_wleft(pardef5,"न",'XX','n','m','pl','3','o','0','0')

pardef6 = ET.SubElement(pardefs,'pardef',n='राजा_n_m')
func_noun_entry_wleft(pardef6,'','XX','n','m','sg','3','d','0','0')
func_noun_entry_wleft(pardef6,'','XX','n','m','pl','3','d','0','0')
func_noun_entry_wleft(pardef6,'','XX','n','m','sg','3','o','0','0')
func_noun_entry_wleft(pardef6,"न",'XX','n','m','pl','3','o','0','0')

pardef7 = ET.SubElement(pardefs,'pardef',n='घर_n_m')
func_noun_entry_wleft(pardef7,'','XX','n','m','sg','3','d','0','0')
func_noun_entry_wleft(pardef7,'','XX','n','m','pl','3','d','0','0')
func_noun_entry_wleft(pardef7,'','XX','n','m','sg','3','o','0','0')
func_noun_entry_wleft(pardef7,"न",'XX','n','m','pl','3','o','0','0')

pardef8 = ET.SubElement(pardefs,'pardef',n='खर्च_n_m')
func_noun_entry_wleft(pardef8,"",'XX','n','m','sg','3','d','0','0')
func_noun_entry_wleft(pardef8,"",'XX','n','m','pl','3','d','0','0')
func_noun_entry_wleft(pardef8,"",'XX','n','m','sg','3','o','0','0')
func_noun_entry_wleft(pardef8,"न",'XX','n','m','pl','3','o','0','0')

pardef9 = ET.SubElement(pardefs,'pardef',n='कवि_n_m')
func_noun_entry_wleft(pardef9,"",'XX','n','m','sg','3','d','0','0')
func_noun_entry_wleft(pardef9,"",'XX','n','m','pl','3','d','0','0')
func_noun_entry_wleft(pardef9,"",'XX','n','m','sg','3','o','0','0')
func_noun_entry_wleft(pardef9,"न",'XX','n','m','pl','3','o','0','0')

pardef10 = ET.SubElement(pardefs,'pardef',n='आदमी_n_m')
func_noun_entry_wleft(pardef10,"",'XX','n','m','sg','3','d','0','0')
func_noun_entry_wleft(pardef10,"",'XX','n','m','pl','3','d','0','0')
func_noun_entry_wleft(pardef10,"",'XX','n','m','sg','3','o','0','0')
func_noun_entry_wleft(pardef10,'आदमिन','XX','n','m','pl','3','o','0','0')
#######################################
tree = ET.ElementTree(root)

tree.write('paradigm-hin.xml')
