"""show_sentence_guesser.py: show and evaluate a genetic algorithm to predict a sentence"""
import logging
import math
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEngine, SentenceGuesser

LABEL = "The goal of having computers automatically \n" \
        "solve problems is central to artificial \n" \
        "intelligence"
SENTENCE_TO_GUESS = LABEL.replace("\n", "")
SCORE = len(SENTENCE_TO_GUESS)
TOURNAMENT_SIZE = 20
POPULATION_SIZE = 2000
MUTATION_RATE = 0.05

seed(math.log(2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Generate engine:")
    environment = GAEngine(SentenceGuesser(MUTATION_RATE, SENTENCE_TO_GUESS))
    logging.info("Run algorithm:")
    result = environment.run_genetic_algorithm(SCORE, POPULATION_SIZE, log=True, tournament_size=TOURNAMENT_SIZE)
    _, ax = plt.subplots(figsize=(12, 12))
    ax.plot(result.get_generations(), result.get_scores(), "-", label=LABEL)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Maximum Score\n", fontsize=20)
    ax.set_title("Guess sentence\n", fontsize=25)
    ax.legend(fontsize=20)
    ax.grid()
    plt.savefig("../results/sentence_guesser.png")

"""Results on execution:"""

"""
INFO:root:Generate engine:
INFO:root:Run algorithm:
INFO:root:Generation 1
INFO:root:Closed word: .RyZLFZHp,LitoKiogn,FDSUtSqEu h.jagZM  sPy GcaLx jgqHUciKrws.wwxRclkumemgrsYhKHByxjAySIMGKLtYqY
INFO:root:Generation 2
INFO:root:Closed word: cbNo.m.EUQ mZaYSkitMQBktcaqn P,aocttZesN SBkdt AUm evptwshZgOpoHCTgRetHNPveiuZWR wsxnudaEqgCuw 
INFO:root:Generation 3
INFO:root:Closed word: .RyZLFZHp,LitoKiogp,FDSUtmqEu Z.jagZMV sPy GcaLx jdqHUcivrws.wwxXRlkumemgrsYhKHrnlXnnKe.bJXesPK
INFO:root:Generation 4
INFO:root:Closed word: bTds chV o.x aqiXBOH RpwpAylBmIHf,alqMNMlDMcoGleDfaSObpmtp.vYWTnyGlQQOedfqGWprRwbz nnKe.jJXesP.
INFO:root:Generation 5
INFO:root:Closed word: TlpsMoBGYSHlV.vhegrOoXlDzJxsQeuwxraEqMNMlDMcoadeW  oCn.mn YYDWEXCrdUbqx.BcWInKcQOMgJlRIlQfNeGz 
INFO:root:Generation 6
INFO:root:Closed word: iiiugFuItHpahaai.k .dkSUtgbWrbNwGGaEqMNsMy OOlLx jqHDmgOsHWCwctXcraPC .LrnquqLBibz nnhe.lJXesPi
INFO:root:Generation 7
INFO:root:Closed word: TxNdRytrduT ,MCQbg ,FDSUtSqEe S.jxmtM  sPy SolcYQXrlblHmn YYDcXnUPguiDowhEtqpmtielbiwefZZorUaPe
INFO:root:Generation 8
INFO:root:Closed word: ihingFuI SQ hBaiogpelDSUtmqEu S.jlmtq  sPy SolcYQvrlblHmn WCwctXcraJC .LZQquqLBibz nnhe.lJXesPi
INFO:root:Generation 9
INFO:root:Closed word: oad. chV o.x aaiggn,FDSUtgqEu S.jlmtM  Swy SolcYQvrlblHmn YvDm.WtbaVDJt TrtKfGbBaxMAnseLliXenPo
INFO:root:Generation 10
INFO:root:Closed word: TTpvMoXh BfpJaaiXtAMYmpRredO z,aocttpMaMlDMcolcYQvrlblYmn YYDtEXCbaVDJn MrtAfGBBaD nnse.lJXesea
INFO:root:Generation 11
INFO:root:Closed word: TlUvMoVh cf haaiXgn,FnUUtKjC oIsoDaDncXTXy colcYQXrlbLSmn YYDcXnUPguJJn TrtKfGbMax nnse.liXenPo
INFO:root:Generation 12
INFO:root:Closed word: TlpvMoVh cc haaixD zYmpINeBO z,aokT.acXely FolcvQXrlblHmn YYTcXnmraXH qLgrtiWGbBax nnse.lJXesPi
INFO:root:Generation 13
INFO:root:Closed word: ihengFuI PQ hOvhzgreomnUtmxs oISoDaDacXTXy SolvYQBrlblmmn YYDcXnUZglFtoThEttmcPibzsnnEeLliXenOo
INFO:root:Generation 14
INFO:root:Closed word: ihengFul SQ hazixw EYmpRtedC oIsoNaDncXNXy colcYQprHbBSmn YYDcXnePguitoWTrtKfGbWax SnjeLliXensS
INFO:root:Generation 15
INFO:root:Closed word: ihengFul SQ hazixw EYmpRtedC oIsoNaDncXNXy colcYQprHbBSmA YYDcXnePguBtoWTrtKfGbWaj SnjeLliXensS
INFO:root:Generation 16
INFO:root:Closed word: ihengFul SQ hazixw EKmpRtedC oIsoNaDncaCry SolvgQvrobgHHssWLwctXiraVqJt NrtKfobWaC Snhe.liXenPA
INFO:root:Generation 17
INFO:root:Closed word: ihengmul SC hazixw EZmpRtedC oItocaDmcahXy SolvgQfroblSmn YYDcwnUPguitowhJttpGbiel insehliienPg
INFO:root:Generation 18
INFO:root:Closed word: ihWngF,l SQ havixo EYmpYtedC wIIokaticaCryBSoPvgQir blSms .YTcXnHralFtoThrtKfGcMaxfnnse.lVlenPM
INFO:root:Generation 19
INFO:root:Closed word: ihengMul SQ havixw EYmpYteBO zuyoDaticamry zolvqQUrobgHmsHWLwctXbr.wCJo TrtifGCMao nnVeLliXenso
INFO:root:Generation 20
INFO:root:Closed word: ihengMul SQ havixw EYmpYteBO zuyoDavicCCry solvgQvr blims YYKcXnHraPRtoWTrtKfEcMnl GnjeVlinenBo
INFO:root:Generation 21
INFO:root:Closed word: ihengFal nQ haziVw ZYmpRtedC FILovaticaCry SolvgQar blhmx YYTcXnHralFtoThrtnfGciel in.eWliXenzH
INFO:root:Generation 22
INFO:root:Closed word: ihengFxl SB havixw GZmpRtedC oItocaDmcahXy bolvEUproblims WrycKntralH o TrtifGCMao nnieLliXenso
INFO:root:Generation 23
INFO:root:Closed word: ihengVal nQ haziVw DYmpRtedCbaIDovaticaCry bolvEUproblims WEycKntralH o TrtifGCMao nnieLliXenso
INFO:root:Generation 24
INFO:root:Closed word: ihengFdl SQ havixh EYdpBteBs guyoDaticamry zolvgQvr blSms Wr cKntralFtoThrtnfGciWl in.eWliXenzH
INFO:root:Generation 25
INFO:root:Closed word: ihengVal uf havixo EYmpYtede oOIokaticaCra SolvXQvr bldms YC cXn ralOtoThrtGfGciel in.eWligenXg
INFO:root:Generation 26
INFO:root:Closed word: ThengeVj Yf havixw uZmpIteBO BKoomaticaCry solvgQproblSms rr cKntralFtoThrtnfGciKl inVetlicenso
INFO:root:Generation 27
INFO:root:Closed word: ThengeVj Yf havisw uZmpIteBO BKoomaticaCry solvgQproblSms rr cKntralFtoThrtnfOciel in.eWligBnXg
INFO:root:Generation 28
INFO:root:Closed word: Thengusj Yf haviqw uZmpIteBO BKKomaticacry solvgQproblims irycKntrblHto artifGcMal injeWliXRnco
INFO:root:Generation 29
INFO:root:Closed word: ihengFul uf havixo EYmpBteBs guyoDaticairy zolvgQproblims irycKntralHto artifGcMal injeWliXenHo
INFO:root:Generation 30
INFO:root:Closed word: TheNgeVl cf havixw HVmpIteBO NIoomaticaCry solvgQproblZmsE.E cdntralHto artifzcOal injeWliXenco
INFO:root:Generation 31
INFO:root:Closed word: ihergVal qf havixw EYmp terO auyomatmcaCry solvgQproblZmsE.ELcdntralHto artifzcOal inveWliXenco
INFO:root:Generation 32
INFO:root:Closed word: ThengeVj Yf havizw BYmpRterO auyomaticaxry s.lvgQproblSms rr centraMFto TrjifGciel inzeUliXence
INFO:root:Generation 33
INFO:root:Closed word: ThengFul qQ havinw mYmpRterO aujomaticavry solvhIproblims tr centraMFto TrtifGciel inWeWFiYence
INFO:root:Generation 34
INFO:root:Closed word: ThengeQj Yf havizv BYmpZterO auyomaticarry solvgUTroblSms Xe cKntralFto artifHcial insebliwence
INFO:root:Generation 35
INFO:root:Closed word: FhergoalHLf havitw uompRtero aulomaticasry solvgQYroblims irycKntralHto artif,cial insebliwence
INFO:root:Generation 36
INFO:root:Closed word: TheigFul uf havin, zYmpRterO aujomaticakry solvhIproblWms Or cKntralttoHartif,cial insebliwence
INFO:root:Generation 37
INFO:root:Closed word: Fhergoal Uf havinw SqmpRterO auNomaticacry solvTQproblSms rr cKntralHto artifBEial injeWligence
INFO:root:Generation 38
INFO:root:Closed word: The g.Vl Nf havizw fYmpRteNO aItomaticairy solveYproblWms Or cKntrMl tp artif,cial inXelligence
INFO:root:Generation 39
INFO:root:Closed word: ThergoRlHLf havitm uompRtero aulomaticaCoy solveoproblWms O, cKntqalCto artif,cial  ntevligence
INFO:root:Generation 40
INFO:root:Closed word: TheGgoul uf havin, gYmpsterO aujomaticaUry solvTQproblSms Ur cKntral tp artifCcial inXelligence
INFO:root:Generation 41
INFO:root:Closed word: FheTgoalpxf havingQSqmpRterO auyomaticacry solveIproblims D, central tL artifncPal integligence
INFO:root:Generation 42
INFO:root:Closed word: bhergoal ef havinw uoLpRterk auyomaticaCoy solve problWms O, cEntNMl to artiH,cial inXelligence
INFO:root:Generation 43
INFO:root:Closed word: The goalpUf havinw mYMpRtero auvomaticaCry soOveoproblims tr centralMto artif,cial indelligence
INFO:root:Generation 44
INFO:root:Closed word: The goalpUf havinB  ompUterO auyomaticacry soWvq probhEms Nr oentralCto artifvcial intelligence
INFO:root:Generation 45
INFO:root:Closed word: Thergoal Uf havinw BompUterw auyomaticadxy solveoproblWms rr centralMto artif,cial inXegligence
INFO:root:Generation 46
INFO:root:Closed word: The gAal Uf havinE BompUterw auyomaticadxyLsolveoproblXms rr cNntralCto artifvcial intelligence
INFO:root:Generation 47
INFO:root:Closed word: Phe goal Qf havinw  omputerw auyomaticaVry solveoproblEms Nr oentralCto artifvcial intelligence
INFO:root:Generation 48
INFO:root:Closed word: TheLgoal Uf havinw  ompUterO aEyomaticazly solveoproblSms is centrylCto artiftcial int,lligence
INFO:root:Generation 49
INFO:root:Closed word: Thergoal Uf havinw aompsterw aujomatica ry solvq prxblEms is centralCao artifGcial intelligence
INFO:root:Generation 50
INFO:root:Closed word: The goalpUf havinB  ompUterF autonatically solvq problSms is centralCto artifZcial intelligence
INFO:root:Generation 51
INFO:root:Closed word: The goal Uf havinB  ompUterF autonatically solvq problSms is centralCto a.ti.Zcial intelligence
INFO:root:Generation 52
INFO:root:Closed word: The goaO Uf havinB OompUlerF autonatically solvemDroPlSms is central to artiftcial intelligence
INFO:root:Generation 53
INFO:root:Closed word: The goal Uf havinw Bompqterv automatichlly solvebproblSms iL central to artif,cial intelligfnce
INFO:root:Generation 54
INFO:root:Closed word: The goal Uf havEnB  ompUterA autonatically solve problKms is centrAl to artifvnial intelligence
INFO:root:Generation 55
INFO:root:Closed word: The goal of havinx aompsterA autonatically solve problemT is centrAl to artifvnial intElligence
INFO:root:Generation 56
INFO:root:Closed word: The goal of havinB aompsterA autonatically solke problemT is centrAl to artifvnial intElligence
INFO:root:Generation 57
INFO:root:Closed word: The goal of havinB aompsterA autonatically solke problemp is centrAl to artifvcial intelligence
INFO:root:Generation 58
INFO:root:Closed word: The Yoal Uf havinw Bompuser, automatically solve problHms is central to artif,cijl intelligence
INFO:root:Generation 59
INFO:root:Closed word: The goal of havinw computerv autonatically solve problSms is centralCKo artifOcnal intelligence
INFO:root:Generation 60
INFO:root:Closed word: The goal of havinw computerv automatically socvelproblems is centbalrto artificial intnlligence
INFO:root:Generation 61
INFO:root:Closed word: The goal oC havinw iomputerv automaticzlly solve problIms is central to artificial intelligence
INFO:root:Generation 62
INFO:root:Closed word: The goal ofshavinJ computers automatically solve problKmsLis xentral to artificigl intelligence
INFO:root:Generation 63
INFO:root:Closed word: The goal of havinw computerv aMtomaticblly Molve probl,ms is central to artificial intelligence
INFO:root:Generation 64
INFO:root:Closed word: The goal of havinJ computers automatically solve problems is censral toYarwif,cial intelligence
INFO:root:Generation 65
INFO:root:Closed word: The goal of havinH computerC automatically sonve problems is central to artificiaF intelligence
INFO:root:Generation 66
INFO:root:Closed word: The goal of havinJ computers automatLcally solve problKms is central tz artificial intelligence
INFO:root:Generation 67
INFO:root:Closed word: The goal of havinX computerv automatically solve problems is central to artificial inzelligence
INFO:root:Generation 68
INFO:root:Closed word: The goal of havinX computerv automatically solve problems Fs central to artificial intelligence
INFO:root:Generation 69
INFO:root:Closed word: The goal of havinw computerV automatically soIve problOms is central to artificial intelligence
INFO:root:Generation 70
INFO:root:Closed word: The goal of havinw computers gutomatically solve problems is cennral to Nrtificial intelligence
INFO:root:Generation 71
INFO:root:Closed word: The goal,of havinJ computerO automatically solve problems is central lo artificial intelligence
INFO:root:Generation 72
INFO:root:Closed word: The gokl of havinQ computers automatically solve problems is cVntral to artificial intellibence
INFO:root:Generation 73
INFO:root:Closed word: The gokl oe havinQ computers automatically solve problems is central to artificial,intelligence
INFO:root:Generation 74
INFO:root:Closed word: The gokl of havin. cnmputers automatically solve problems is certral to artificial intelligence
INFO:root:Generation 75
INFO:root:Closed word: The goal of havinQ Momputers yutomatically solve problems is centrMl to artificial intelligence
INFO:root:Generation 76
INFO:root:Closed word: The goal ef havinN computerV automatically solve problems is central to artificial intelligence
INFO:root:Generation 77
INFO:root:Closed word: The goal of having computers aut,matically solve problems is central to artificial intelIigeIce
INFO:root:Generation 78
INFO:root:Closed word: The goaB of having computers automatically solve problems is cereral to artificial intelligence
INFO:root:Generation 79
INFO:root:Closed word: The goal of havinJ computers automatically solve problems is central tJ artificial intelliHence
INFO:root:Generation 80
INFO:root:Closed word: The goal of haUing computers autoeatically solve problems is central to aatificial intelligence
INFO:root:Generation 81
INFO:root:Closed word: The goal of having computers automatically solve pUoblems is centrtl to artificial intelligence
INFO:root:Generation 82
INFO:root:Closed word: Thx goal of having computers automatbcalfy solve problemsnis central to artificial intelligence
INFO:root:Generation 83
INFO:root:Closed word: The goal of having computers automatically solve problems As censral to Rrtificial intelligence
INFO:root:Generation 84
INFO:root:Closed word: The goal of having computers automatically solve problems is central to a tificial iLtelligence
INFO:root:Generation 85
INFO:root:Closed word: The goal of having computers automatically solve problems is central to arYificial intelligence
INFO:root:Generation 86
INFO:root:Closed word: Th. goal of having computers automatically solve Hrobloms is central to artificial intelligence
INFO:root:Generation 87
INFO:root:Closed word: Th  goal of having computers automatically solve problets is central to artificial intelligence
INFO:root:Generation 88
INFO:root:Closed word: The goal of Ffving computers automatically solve problems is central Co artificial intelligence
INFO:root:Generation 89
INFO:root:Closed word: The goal of having computers automatically solve proLlets is central to artificial intelligence
INFO:root:Generation 90
INFO:root:Closed word: The goal of having computers automaQically solve problets is central to artifLcial intelligence
INFO:root:Generation 91
INFO:root:Closed word: The goalYof having computers automaticaSly solUe problems is central to artificial intelligence
INFO:root:Generation 92
INFO:root:Closed word: The goal of having computers autoqaticallyXsolve problems is central to artificial intelUigence
INFO:root:Generation 93
INFO:root:Closed word: The goal of having computers automatically solve problems is central,to artificial intelligence
INFO:root:Generation 94
INFO:root:Closed word: Th  goal of having computers automatically solve problems is central,to artificial intelligence
INFO:root:Generation 95
INFO:root:Closed word: The goal of having computerl automatically solve problems is central do artificial intelligence
INFO:root:Generation 96
INFO:root:Closed word: The goal of having computers automatically solve problems is central ko Rrtificial intelligence
INFO:root:Generation 97
INFO:root:Closed word: ThB goal of having computers automGtically solve problems is central to artificial intelligence
INFO:root:Generation 98
INFO:root:Closed word: The Xoal of having computers automatically solve problems is central to artiaLcial intelligence
INFO:root:Generation 99
INFO:root:Closed word: Thezgoal of having computers automatically Aolve problems is central to artificial intelligence
INFO:root:Generation 100
INFO:root:Closed word: The goal of having computers automatically Aolve problems is central to artificialAintelligence
INFO:root:Generation 101
INFO:root:Closed word: The goal of having coQputers automaticUlly solve problems is central to artificial intelligenFe
INFO:root:Generation 102
INFO:root:Closed word: The goal of having computers automatically solvecproblemsUis central to artificial intelligence
INFO:root:Generation 103
INFO:root:Closed word: The goal of having computers automatically solve problems is cFntral to artificial pnteljigence
INFO:root:Generation 104
INFO:root:Closed word: The goal of having computers automatically solve problems is central t, artificFal Kntelligence
INFO:root:Generation 105
INFO:root:Closed word: The goal of having computers automatically solvS problems is central to artificial intexligence
INFO:root:Generation 106
INFO:root:Closed word: The goal of hCving compuxers automatically solve problems is central to artificial intelligence
INFO:root:Generation 107
INFO:root:Closed word: The goal of having computers automatically solve problems is central to artif cial intelligence
INFO:root:Generation 108
INFO:root:Closed word: The goal of having computers automatically solve probleQs is central to artificial intellIgence
INFO:root:Generation 109
INFO:root:Closed word: The goal of having computers automaticallyXsolve problems is central to artificial intelligence
INFO:root:Generation 110
INFO:root:Closed word: Tke goal of having computersDautomatically solve problems is central to artificial intelligence
INFO:root:Generation 111
INFO:root:Closed word: The goal cf haning computersDautomatically solve problems is central to artificial intelligence
INFO:root:Generation 112
INFO:root:Closed word: The goal of having computers automaticallc solve nroblems is central to artificiaA intelligence
INFO:root:Generation 113
INFO:root:Closed word: The goal of haNing computers automatically solve problems is cenAral to trtificial intelligence
INFO:root:Generation 114
INFO:root:Closed word: ThN goal of having computers auHomatically solve problems is central to trtificial intelligence
INFO:root:Generation 115
INFO:root:Closed word: The goal of having computers automatically sqlve problems is central to artificiaP intelligencW
INFO:root:Generation 116
INFO:root:Closed word: Qhe goal of having computers automatically solve probleKs is central to artificial intelligence
INFO:root:Generation 117
INFO:root:Closed word: The goal of hovink computers automatically solve problems is central to artifiBial intelligence
INFO:root:Generation 118
INFO:root:Closed word: The goal of haWing computers automatically solve problems is centrZl to artificial intelligence
INFO:root:Generation 119
INFO:root:Closed word: The goal of having computers autymatically soDve problems is central to artificial intellibence
INFO:root:Generation 120
INFO:root:Closed word: The goal of having computerg xutomatically solve problems Bs central to artificial intelligence
INFO:root:Generation 121
INFO:root:Closed word: The goal of having computers automatiOally Xolve problems is central to arkificial intelligence
INFO:root:Generation 122
INFO:root:Closed word: The goal of having computers automatically solve prdblems is central to artificial intelligencv
INFO:root:Generation 123
INFO:root:Closed word: The goal of having computers automatically soDve problems is centrZl to artificial intelligence
INFO:root:Generation 124
INFO:root:Closed word: The goal of having computers automatiWally solve problems is central to artificial intelliqence
INFO:root:Generation 125
INFO:root:Closed word: The foal oW having computers automatically soOve problems is central to artificial intelligence
INFO:root:Generation 126
INFO:root:Closed word: The goal of having computers automatically solve problems is central ko artificial intePligence
INFO:root:Generation 127
INFO:root:Closed word: The goal of having computers automatically solve problems is ceDtral to artificial intelligence
INFO:root:Generation 128
INFO:root:Closed word: The goai of having computers automatically solve problems is central tV artificial intelligence
INFO:root:Generation 129
INFO:root:Closed word: The goal of having computers automaticallL solve problems is ceDtraljto artificial intelligence
INFO:root:Generation 130
INFO:root:Closed word: The goal of having Domputers automatically solve problems isHcentral to artificial intelligence
INFO:root:Generation 131
INFO:root:Closed word: The goal of haviMg computers automatically solve probleks is central to artJficial intelligence
INFO:root:Generation 132
INFO:root:Closed word: The goal of having computers automatically solve proeloms is central to artificial inGelligence
INFO:root:Generation 133
INFO:root:Closed word: The goal of having computers aftomatically solve problemsVis cenLral to artificial intelligence
INFO:root:Generation 134
INFO:root:Closed word: The goal of having Somputers automatically solve problems is central to artificial intelligence
INFO:root:Generation 135
INFO:root:Closed word: The goal of having Somputers automatically solve problems is central to artificial intelligence
INFO:root:Generation 136
INFO:root:Closed word: The goal of having computers automatically solve problemo is central to artifici.l intelligence
INFO:root:Generation 137
INFO:root:Closed word: The goal of oaving computers automatically solve problems is central to artificial intelligence
INFO:root:Generation 138
INFO:root:Closed word: The goal of having cMmputers automaticallygsolve problems is central to arUificial intelligence
INFO:root:Generation 139
INFO:root:Closed word: The goal of having computers automatXcally solve problems is central to artificial iEtelligence
INFO:root:Generation 140
INFO:root:Closed word: The goal of having cMmputers automatically solve problems is central tH artificial intelligence
INFO:root:Generation 141
INFO:root:Closed word: The goal of having computers automaticalzy solvi prcblems is central to artificial intelligence
INFO:root:Generation 142
INFO:root:Closed word: The goal of having computers automStEcally solve problems is central to arkificial intelligence
INFO:root:Generation 143
INFO:root:Closed word: The goal of having computers automStEcally solve problems is central to artificial intelligence
INFO:root:Generation 144
INFO:root:Closed word: The Doal of having computers Mutomaticall  solve problems is central to artificial intelligence
INFO:root:Generation 145
INFO:root:Closed word: The goal of having c mputers automatically solve problems is ceWtral to artificial intelligegce
INFO:root:Generation 146
INFO:root:Closed word: The goafQof having computers automatically solve problems is central to artificial antelligence
INFO:root:Generation 147
INFO:root:Closed word: The goal of having computers automatically solve problems is ceWtral to artificIal intelligence
INFO:root:Generation 148
INFO:root:Closed word: The goal of having computers automatRcally solve problems is ceWtral to artificIal intelligence
INFO:root:Generation 149
INFO:root:Closed word: The goal of hafing computers automatically solve problems is ceWtral to artificial intelligence
INFO:root:Generation 150
INFO:root:Closed word: The goal of having computers automatically solvefproblems is central to artificIal intelligepce
INFO:root:Generation 151
INFO:root:Closed word: The goal of having computers automatically solvefproblems is central to artificIal intelligence
INFO:root:Generation 152
INFO:root:Closed word: The goal of having computers automOtically solve problems is central to artificial intelPigence
INFO:root:Generation 153
INFO:root:Closed word: The ,oal of having computers automatically solve problems is central to artificial ixtelligence
INFO:root:Generation 154
INFO:root:Closed word: Jhe goal of having computers automatically solve problems is central to artificial ixtelligence
INFO:root:Generation 155
INFO:root:Closed word: The goal of having computers automatically solve problems is central to artificial ixtelligence
INFO:root:Generation 156
INFO:root:Closed word: The goal of having coyputers automatically solve problems is central to artificial ,ntelligence
INFO:root:Generation 157
INFO:root:Closed word: The goal of iaving computeSs automatically solve problems is central toEartificial intelligence
INFO:root:Generation 158
INFO:root:Closed word: The goal of having computers automatically solve probfems is ce tral to artificial iStelligence
INFO:root:Generation 159
INFO:root:Closed word: The goal of havingQcomputers automatically soYve prodlems is central to artificial intelligence
INFO:root:Generation 160
INFO:root:Closed word: The goal of having Zomputers automatically solve probwems is central toEartificial intelligence
INFO:root:Generation 161
INFO:root:Closed word: The goal of having c.mputers automatically solve Troblems is ventral to artificial intelligence
INFO:root:Generation 162
INFO:root:Closed word: The goal of having computers automaticayly solve problems is ceXtral to artificial intelligence
INFO:root:Generation 163
INFO:root:Closed word: The goal oc having compucers automatically solve problems is central to artificial intelligence
INFO:root:Generation 164
INFO:root:Closed word: The goal of having coVputers automaticayly solve problems is central to artificial intelligence
INFO:root:Generation 165
INFO:root:Closed word: The goal of having computerL automatically solve problems is central to a,tificial intelligence
INFO:root:Generation 166
INFO:root:Closed word: The goal of Gaving computers automatically solve problemsZis central to artificial intelligence
INFO:root:Generation 167
INFO:root:Closed word: The goaltop having computers automatically solve problemsZis central to artificial intelligence
INFO:root:Generation 168
INFO:root:Closed word: The goal of having computers automatically solve problemsZis central to arzificial intelligence
INFO:root:Generation 169
INFO:root:Closed word: Thexgoal of havingrcomputers automatically solve problems is central to artificial intelligence
INFO:root:Generation 170
INFO:root:Closed word: The goal of having computers automatically solve problems isNcentral Vo artificial intelligence
INFO:root:Generation 171
INFO:root:Closed word: The goal of having computers automatically solve problems is centrRl to artificial intelligenc,
INFO:root:Generation 172
INFO:root:Closed word: The goal of having czmputers automatically solve problDms is ceBtral to artificial intelligence
INFO:root:Generation 173
INFO:root:Closed word: she goal of having computers automathcally solve proble s is central to artificial intelligence
INFO:root:Generation 174
INFO:root:Closed word: The goal of having computers automatically solve problDms is celtral to artificial intelligence
INFO:root:Generation 175
INFO:root:Closed word: The goal of having computers autNmatically solve problems is central to artificial intelligence
INFO:root:Generation 176
INFO:root:Closed word: The goal of having compuHers automatically solve problems is ceBtral to artificial intelligence
INFO:root:Generation 177
INFO:root:Closed word: The goal of having comWuHers automatically solve problems is central to artificial intelligence
INFO:root:Generation 178
INFO:root:Closed word: The goal of xaving computers automgtically solve problems iszcentral to artificial intelligence
INFO:root:Generation 179
INFO:root:Closed word: The goal of having computers automgtically solve problems iszcentral to artificial intelligence
INFO:root:Generation 180
INFO:root:Closed word: The goal of having compzters automgtically solve problems iszcentral to artificial intelligence
INFO:root:Generation 181
INFO:root:Closed word: The goal of having computers automatically solve probleUs is czntral to artificial innelligence
INFO:root:Generation 182
INFO:root:Closed word: The goal of having computers automatically solve problems is central to artificial intelligence

Process finished with exit code 0
"""
