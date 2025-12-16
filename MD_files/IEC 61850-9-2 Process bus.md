<!-- image -->

®

## INTERNATIONAL STANDARD

## NORME INTERNATIONALE

Communication networks and systems for power utility automation Part 9-2: Specific communication service mapping (SCSM) - Sampled values over ISO/IEC 8802-3

Réseaux et systèmes de communication pour l'automatisation des systèmes électriques -

Partie 9-2: Mise en correspondance des services de communication spécifiques (SCSM) - Valeurs échantillonnées sur ISO/CEI 8802-3

<!-- image -->

Edition 2.0 2011-09

<!-- image -->

## THIS PUBLICATION IS COPYRIGHT PROTECTED Copyright © 2011 IEC, Geneva, Switzerland

All rights reserved. Unless otherwise specified, no part of this publication may be reproduced or utilized in any form or by any means, electronic or mechanical, including photocopying and microfilm, without permission in writing from either IEC or IEC's member National Committee in the country of the requester.

If you have any questions about IEC copyright or have an enquiry about obtaining additional rights to this publication, please contact the address below or your local IEC member National Committee for further information.

Droits de reproduction réservés. Sauf indication contraire, aucune partie de cette publication ne peut être reproduite ni utilisée sous quelque forme que ce soit et par aucun procédé, électronique ou mécanique, y compris la photocopie et les microfilms, sans l'accord écrit de la CEI ou du Comité national de la CEI du pays du demandeur.

Si  vous  avez  des  questions  sur  le  copyright  de  la  CEI  ou  si  vous  désirez  obtenir  des  droits  supplémentaires  sur  cette publication, utilisez les coordonnées ci-après ou contactez le Comité national de la CEI de votre pays de résidence.

IEC Central Office 3, rue de Varembé CH-1211 Geneva 20 Switzerland

Email: inmail@iec.ch

Web: www.iec.ch

## About the IEC

The  International  Electrotechnical  Commission  (IEC)  is  the  leading  global  organization  that  prepares  and  publishes International Standards for all electrical, electronic and related technologies.

## About IEC publications

The technical content of IEC publications is kept under constant review by the IEC. Please make sure that you have the latest edition, a corrigenda or an amendment might have been published.

-  Catalogue of IEC publications: www.iec.ch/searchpub

The IEC on-line Catalogue enables you to search by a variety of criteria (reference number, text, technical committee,…). It also gives information on projects, withdrawn and replaced publications.

-  IEC Just Published: www.iec.ch/online\_news/justpub

Stay up to date on all new IEC publications. Just Published details twice a month all new publications released. Available on-line and also by email.

-  Electropedia: www.electropedia.org

The world's leading online dictionary of electronic and electrical terms containing more than 20 000 terms and definitions in  English  and  French,  with  equivalent  terms  in  additional languages.  Also  known  as  the  International  Electrotechnical Vocabulary online.

-  Customer Service Centre: www.iec.ch/webstore/custserv

If  you  wish  to  give  us  your  feedback  on  this  publication  or  need  further  assistance,  please  visit  the  Customer  Service Centre FAQ or contact us:

Email: csc@iec.ch

Tel.: +41 22 919 02 11

Fax: +41 22 919 03 00

## A propos de la CEI

La  Commission  Electrotechnique  Internationale  (CEI)  est  la  première  organisation  mondiale  qui  élabore  et  publie  des normes internationales pour tout ce qui a trait à l'électricité, à l'électronique et aux technologies apparentées.

## A propos des publications CEI

Le  contenu  technique  des  publications  de  la  CEI  est  constamment  revu.  Veuillez  vous  assurer  que  vous  possédez l'édition la plus récente, un corrigendum ou amendement peut avoir été publié.

-  Catalogue des publications de la CEI: www.iec.ch/searchpub/cur\_fut-f.htm

Le Catalogue en-ligne de la CEI vous permet d'effectuer des recherches en utilisant différents critères (numéro de référence, texte, comité d'études,…). Il donne aussi des informations sur les projets et les publications retirées ou remplacées.

-  Just Published CEI: www.iec.ch/online\_news/justpub

Restez  informé  sur  les  nouvelles  publications  de  la  CEI.  Just  Published  détaille  deux  fois  par  mois  les  nouvelles publications parues. Disponible en-ligne et aussi par email.

-  Electropedia: www.electropedia.org

Le premier dictionnaire en ligne au monde de termes électroniques et électriques. Il contient plus de 20 000 termes et définitions en anglais et en français, ainsi que les termes équivalents dans les langues additionnelles. Egalement appelé Vocabulaire Electrotechnique International en ligne.

-  Service Clients: www.iec.ch/webstore/custserv/custserv\_entry-f.htm

Si vous désirez nous donner des commentaires sur cette publication ou si vous avez des questions, visitez le FAQ du Service clients ou contactez-nous:

Email: csc@iec.ch

Tél.: +41 22 919 02 11

Fax: +41 22 919 03 00

<!-- image -->

®

## INTERNATIONAL STANDARD

## NORME INTERNATIONALE

Communication networks and systems for power utility automation Part 9-2: Specific communication service mapping (SCSM) - Sampled values over ISO/IEC 8802-3

Réseaux et systèmes de communication pour l'automatisation des systèmes électriques -

Partie 9-2: Mise en correspondance des services de communication spécifiques (SCSM) - Valeurs échantillonnées sur ISO/CEI 8802-3

INTERNATIONAL ELECTROTECHNICAL COMMISSION

COMMISSION ELECTROTECHNIQUE INTERNATIONALE

ICS 33.200

Edition 2.0 2011-09

PRICE CODE CODE PRIX

V

<!-- image -->

ISBN 978-2-88912-631-6

## CONTENTS

|       | FOREWORD...........................................................................................................................4 INTRODUCTION.....................................................................................................................6   | FOREWORD...........................................................................................................................4 INTRODUCTION.....................................................................................................................6   | FOREWORD...........................................................................................................................4 INTRODUCTION.....................................................................................................................6   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Scope...............................................................................................................................7                                                                                                                                     | Scope...............................................................................................................................7                                                                                                                                     | Scope...............................................................................................................................7                                                                                                                                     |
| 2     | Normative references........................................................................................................7                                                                                                                                             | Normative references........................................................................................................7                                                                                                                                             | Normative references........................................................................................................7                                                                                                                                             |
| 3     | Terms and definitions .......................................................................................................9                                                                                                                                            | Terms and definitions .......................................................................................................9                                                                                                                                            | Terms and definitions .......................................................................................................9                                                                                                                                            |
| 4     | Abbreviations....................................................................................................................9                                                                                                                                        | Abbreviations....................................................................................................................9                                                                                                                                        | Abbreviations....................................................................................................................9                                                                                                                                        |
| 5     | Communication stack......................................................................................................10                                                                                                                                               | Communication stack......................................................................................................10                                                                                                                                               | Communication stack......................................................................................................10                                                                                                                                               |
| 5     | 5.1                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |
| 5     | 5.2                                                                                                                                                                                                                                                                       | Overview of the protocol usage..............................................................................10                                                                                                                                                            | Overview of the protocol usage..............................................................................10                                                                                                                                                            |
| 5     | 5.2                                                                                                                                                                                                                                                                       | 5.2.1                                                                                                                                                                                                                                                                     | Client/server services and communication profiles .................................................11 Client/server services ................................................................................11                                                           |
| 5     | 5.2                                                                                                                                                                                                                                                                       | 5.2.2                                                                                                                                                                                                                                                                     | A-Profile ....................................................................................................12                                                                                                                                                          |
| 5     | 5.2                                                                                                                                                                                                                                                                       | 5.2.3                                                                                                                                                                                                                                                                     | TCP/IP T-Profile ........................................................................................13                                                                                                                                                               |
| 5     | 5.3                                                                                                                                                                                                                                                                       | SV service and communication profile ....................................................................13                                                                                                                                                               | SV service and communication profile ....................................................................13                                                                                                                                                               |
| 5     | 5.3                                                                                                                                                                                                                                                                       | 5.3.1                                                                                                                                                                                                                                                                     | SV mapping overview .................................................................................13                                                                                                                                                                   |
| 5     | 5.3                                                                                                                                                                                                                                                                       | 5.3.2                                                                                                                                                                                                                                                                     | A-Profile ....................................................................................................14                                                                                                                                                          |
| 5     | 5.3                                                                                                                                                                                                                                                                       | 5.3.3                                                                                                                                                                                                                                                                     | T-Profile ....................................................................................................14                                                                                                                                                          |
| 5     | 5.4                                                                                                                                                                                                                                                                       | Restrictions                                                                                                                                                                                                                                                              | ...........................................................................................................17                                                                                                                                                             |
| 6     | Mapping of IEC 61850-7-2 and IEC 61850-7-3 data attributes .........................................17                                                                                                                                                                    | Mapping of IEC 61850-7-2 and IEC 61850-7-3 data attributes .........................................17                                                                                                                                                                    | Mapping of IEC 61850-7-2 and IEC 61850-7-3 data attributes .........................................17                                                                                                                                                                    |
| 7     | Mapping of IEC 61850-7-2 classes and services .............................................................17                                                                                                                                                             | Mapping of IEC 61850-7-2 classes and services .............................................................17                                                                                                                                                             | Mapping of IEC 61850-7-2 classes and services .............................................................17                                                                                                                                                             |
| 7     | 7.1                                                                                                                                                                                                                                                                       | Classes of SV data sets .........................................................................................17                                                                                                                                                       | Classes of SV data sets .........................................................................................17                                                                                                                                                       |
| 7     | 7.2                                                                                                                                                                                                                                                                       | Definition of SV data sets .......................................................................................17                                                                                                                                                      | Definition of SV data sets .......................................................................................17                                                                                                                                                      |
| 8     | Mapping of the model for the transmission of sampled values .........................................18                                                                                                                                                                   | Mapping of the model for the transmission of sampled values .........................................18                                                                                                                                                                   | Mapping of the model for the transmission of sampled values .........................................18                                                                                                                                                                   |
| 8     | 8.1                                                                                                                                                                                                                                                                       | Overview ...............................................................................................................18                                                                                                                                                | Overview ...............................................................................................................18                                                                                                                                                |
| 8     | 8.2                                                                                                                                                                                                                                                                       | Mapping of the multicast sampled value control block class and services ...............18                                                                                                                                                                                 | Mapping of the multicast sampled value control block class and services ...............18                                                                                                                                                                                 |
| 8     | 8.2                                                                                                                                                                                                                                                                       | 8.2.1                                                                                                                                                                                                                                                                     | Multicast sampled value control block definition .........................................18                                                                                                                                                                              |
| 8     | 8.2                                                                                                                                                                                                                                                                       | 8.2.2 SV                                                                                                                                                                                                                                                                  | M Services.............................................................................................19                                                                                                                                                                 |
| 8     | 8.3                                                                                                                                                                                                                                                                       | Mapping of the                                                                                                                                                                                                                                                            | unicast sampled value control block class and services ..................20                                                                                                                                                                                               |
| 8     |                                                                                                                                                                                                                                                                           | 8.3.1 Unicast sampled value control block definition............................................20                                                                                                                                                                        | 8.3.1 Unicast sampled value control block definition............................................20                                                                                                                                                                        |
| 8     |                                                                                                                                                                                                                                                                           | 8.3.2 USV Services .............................................................................................21                                                                                                                                                        |                                                                                                                                                                                                                                                                           |
| 8     | 8.4                                                                                                                                                                                                                                                                       | Mapping of the update of the sampled value buffer.................................................21                                                                                                                                                                      | Mapping of the update of the sampled value buffer.................................................21                                                                                                                                                                      |
| 8     | 8.5                                                                                                                                                                                                                                                                       | Additional definitions for the transmission of sampled values..................................21                                                                                                                                                                         | Additional definitions for the transmission of sampled values..................................21                                                                                                                                                                         |
| 8     | 8.5                                                                                                                                                                                                                                                                       | 8.5.1                                                                                                                                                                                                                                                                     | Application layer functionality .....................................................................21                                                                                                                                                                   |
| 8     | 8.5                                                                                                                                                                                                                                                                       | 8.5.2                                                                                                                                                                                                                                                                     | Presentation layer functionality...................................................................22                                                                                                                                                                     |
| 9     | 8.6 Definitions for basic data types - Presentation layer functionality ...........................24 Conformance..................................................................................................................24                                     | 8.6 Definitions for basic data types - Presentation layer functionality ...........................24 Conformance..................................................................................................................24                                     | 8.6 Definitions for basic data types - Presentation layer functionality ...........................24 Conformance..................................................................................................................24                                     |
| 9     | 9.1                                                                                                                                                                                                                                                                       | Notation.................................................................................................................24                                                                                                                                               | Notation.................................................................................................................24                                                                                                                                               |
| 9     | 9.2                                                                                                                                                                                                                                                                       | PICS ......................................................................................................................24                                                                                                                                             | PICS ......................................................................................................................24                                                                                                                                             |
| 9     | 9.2                                                                                                                                                                                                                                                                       | 9.2.1                                                                                                                                                                                                                                                                     | Profile conformance...................................................................................24                                                                                                                                                                  |
| 9     | 9.2                                                                                                                                                                                                                                                                       | 9.2.2                                                                                                                                                                                                                                                                     | SV Services ...............................................................................................25                                                                                                                                                             |
| 10    | Substation configuration language (SCL).........................................................................25                                                                                                                                                        | Substation configuration language (SCL).........................................................................25                                                                                                                                                        |                                                                                                                                                                                                                                                                           |
| 11    |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |
|       | SCSM specific address element definitions .....................................................................26                                                                                                                                                         | SCSM specific address element definitions .....................................................................26                                                                                                                                                         |                                                                                                                                                                                                                                                                           |
| Annex | A (informative) ISO/IEC 8802-3 frame format and ASN.1 basic encoding rules............27                                                                                                                                                                                  | A (informative) ISO/IEC 8802-3 frame format and ASN.1 basic encoding rules............27                                                                                                                                                                                  |                                                                                                                                                                                                                                                                           |
| Annex | B (informative) Multicast address selection ................................................................32                                                                                                                                                            | B (informative) Multicast address selection ................................................................32                                                                                                                                                            |                                                                                                                                                                                                                                                                           |

| Figure 1 - OSI reference model and profiles..........................................................................11            |                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Figure 2 - Structure of the tag header ...................................................................................15       |                                                                                                               |
| Figure 3 - Reserved 1...........................................................................................................16 |                                                                                                               |
| Figure 4 - Concatenation of several ASDU's into one frame                                                                          | ..................................................22                                                          |
| Figure A.1 - ISO/IEC 8802-3 frame format - No link redundancy...........................................27                         |                                                                                                               |
| Figure A.2 - ISO/IEC 8802-3 frame format - Link redundancy: HSR                                                                    | ......................................28                                                                      |
| Figure A.3 - ISO/IEC 8802-3 frame format - Link redundancy: PRP                                                                    | ......................................29                                                                      |
| Figure A.4 - Basic encoding rules format ..............................................................................30          |                                                                                                               |
| Figure A.5 - Format of the tag octets                                                                                              | ....................................................................................30                        |
| Figure A.6 - Example for an ASN.1 coded APDU frame structure............................................31                         |                                                                                                               |
| Table 1 - Service requiring client/server communication profile                                                                    | .............................................12                                                               |
| Table 2 - Service and protocols for client/server communication A-Profile                                                          | .............................12                                                                               |
| Table 3 - Service and protocols for peer TCP/IP T-Profile                                                                          | .....................................................13                                                       |
| Table 4 - Service requiring SV communication profile                                                                               | ............................................................13                                                |
| Table 5 - Service and protocols for SV communication A-Profile                                                                     | ............................................14                                                                |
| Table 6 - SV T-Profile                                                                                                             | ...........................................................................................................14 |
| Table 7 - Default Virtual LAN IDs and priorities......................................................................15           |                                                                                                               |
| Table 8 - Assigned Ethertype values                                                                                                | .....................................................................................16                       |
| Table 9 - MMS TypeDescription definition for MSVCB MMS structure.......................................18                          |                                                                                                               |
| Table 10 - DstAddress structure                                                                                                    | ...........................................................................................19                 |
| Table 11 - Mapping of multicast sampled value services                                                                             | .......................................................19                                                     |
| Table 12 - MMS TypeDescription definition for USVCB MMS structure .....................................20                          |                                                                                                               |
| Table 13 - Mapping of unicast sampled value services                                                                               | ..........................................................21                                                  |
| Table 14 - Encoding for the transmission of the sampled value buffer                                                               | ...................................22                                                                         |
| Table 15 - Encoding for the basic data types.........................................................................24            |                                                                                                               |
| Table 16 - PICS for A-Profile support.....................................................................................25       |                                                                                                               |
| Table 17 - PICS for T-Profile support.....................................................................................25       |                                                                                                               |
| Table 18 - SV conformance statement...................................................................................25           |                                                                                                               |
| Table 19 - Definitions for SV SCL..........................................................................................26      |                                                                                                               |
| Table B.1 - Recommended multicast addressing example.....................................................32                        |                                                                                                               |

## INTERNATIONAL ELECTROTECHNICAL COMMISSION

\_\_\_\_\_\_\_\_\_\_\_\_

## COMMUNICATION NETWORKS AND SYSTEMS FOR POWER UTILITY AUTOMATION -

## Part 9-2: Specific communication service mapping (SCSM) Sampled values over ISO/IEC 8802-3

## FOREWORD

- 1) The International Electrotechnical Commission (IEC) is a worldwide organization for standardization comprising all national electrotechnical committees  (IEC National Committees). The  object of IEC  is to  promote international co-operation on all questions concerning standardization in the electrical and electronic fields. To this  end  and  in  addition  to  other  activities,  IEC  publishes  International  Standards,  Technical  Specifications, Technical Reports, Publicly Available Specifications (PAS) and Guides  (hereafter referred to as 'IEC Publication(s)'). Their preparation is entrusted to technical committees; any IEC National Committee interested in  the  subject  dealt  with  may  participate  in  this  preparatory  work.  International,  governmental  and  nongovernmental  organizations  liaising  with  the  IEC  also  participate  in  this  preparation.  IEC  collaborates  closely with  the  International  Organization  for  Standardization  (ISO)  in  accordance  with  conditions  determined  by agreement between the two organizations.
- 2) The formal decisions or agreements of IEC on technical matters express, as nearly as possible, an international consensus  of  opinion  on  the  relevant  subjects  since  each  technical  committee  has  representation  from  all interested IEC National Committees.
- 3) IEC  Publications  have  the  form  of  recommendations  for  international  use  and  are  accepted  by  IEC  National Committees  in  that  sense.  While  all  reasonable  efforts  are  made  to  ensure  that  the  technical  content  of  IEC Publications  is  accurate,  IEC  cannot  be  held  responsible  for  the  way  in  which  they  are  used  or  for  any misinterpretation by any end user.
- 4) In  order  to  promote  international  uniformity,  IEC  National  Committees  undertake  to  apply  IEC  Publications transparently  to  the  maximum  extent  possible  in  their  national  and  regional  publications.  Any  divergence between any IEC Publication and the corresponding national or regional publication shall be clearly indicated in the latter.
- 5) IEC  itself  does  not  provide  any  attestation  of  conformity.  Independent  certification  bodies  provide  conformity assessment  services  and,  in  some  areas,  access  to  IEC  marks  of  conformity.  IEC  is  not  responsible  for  any services carried out by independent certification bodies.
- 6) All users should ensure that they have the latest edition of this publication.
- 7) No liability  shall  attach  to  IEC  or  its  directors,  employees,  servants  or  agents  including  individual  experts  and members of its technical committees and IEC National Committees for any personal injury, property damage or other  damage  of  any  nature  whatsoever,  whether  direct  or  indirect,  or  for  costs  (including  legal  fees)  and expenses  arising  out  of  the  publication,  use  of,  or  reliance  upon,  this  IEC  Publication  or  any  other  IEC Publications.
- 8) Attention  is  drawn  to  the  Normative  references  cited  in  this  publication.  Use  of  the  referenced  publications  is indispensable for the correct application of this publication.
- 9) Attention  is  drawn  to  the  possibility  that  some  of  the  elements  of  this  IEC  Publication  may  be  the  subject  of patent rights. IEC shall not be held responsible for identifying any or all such patent rights.

International  Standard  IEC 61850-9-2  has  been  prepared  by  IEC technical  committee  57: Power systems management and associated information exchange.

The text of this standard is based on the following documents:

| FDIS         | Report on voting   |
|--------------|--------------------|
| 57/1133/FDIS | 57/1161/RVD        |

Full  information  on  the  voting  for  the  approval  of  this  standard  can  be  found  in  the  report  on voting indicated in the above table.

This second edition cancels and replaces the first edition published in 2004 and constitutes a technical revision.

Main changes with respect to the first edition are:

- addition of an optional Link redundancy layer (Tables 3 to 6);
- redefinition of 'reserved' fields in link layer (5.3.3.4);
- evolution of USVCB and MSVCB components (Tables 9, 10, 12);
- evolution of encoding for the transmission of the sampled value buffer (Table 14).

This publication has been drafted in accordance with the ISO/IEC Directives, Part 2.

A list of all parts of the IEC 61850 series, under the general title: Communication networks and systems for power utility automation, can be found on the IEC website.

The committee has decided that the contents of this publication will remain unchanged until the stability date indicated on the IEC web site under "http://webstore.iec.ch" in the data related to the specific publication. At this date, the publication will be

- reconfirmed,
- withdrawn,
- replaced by a revised edition, or
- amended.

## INTRODUCTION

This part of IEC 61850 defines the SCSM for  sampled values over ISO/IEC 8802-3. The intent of this SCSM definition is to include the complete mapping of the sampled value model.

This  part  of  IEC 61850  applies  to  electronic  current  and  voltage  transformers  ( ECT and EVT having a digital output), merging units, and intelligent electronic devices, for example protection units, bay controllers and meters, or sensors.

Process  bus  communication  structures  can  be  arranged  in  different  ways  as  described  in IEC/TR 61850-1. In addition to the transmission of sampled value data sets, which are directly connected  to  ISO/IEC 8802-3,  a  selection  of  IEC 61850-8-1  services  is  necessary  to  support the  access  to  the SV control  block.  References  to  the  relevant  IEC 61850-8-1  services  are provided  in  this SCSM .  For  less  complex  devices  (for  example  merging  units),  the  sampled value  control  block  can  be  pre-configured,  in  which  case  there  is  no  need  to  implement IEC 61850-8-1 services based on the MMS -Stack.

This  document  defines  the  mapping  of  sampled  value  class  model  (IEC 61850-7-2)  to ISO/IEC 8802-3. This SCSM , in combination  with IEC 61850-7  and  IEC 61850-6,  allows interoperability between devices from different manufacturers.

This standard does not specify individual implementations or products, nor does it constrain the implementation of entities and interfaces within a computer system. This standard specifies the externally visible functionality of implementations together with conformance requirements for such functionalities.

Reading guide:

- This  document  is  an  extended  mapping  specification  of  IEC 61850-8-1  to  cover  sampled value transmission over ISO/IEC 8802-3.
- This document can best be understood if the reader is thoroughly familiar with IEC 61850-7-1, IEC 61850-7-2, IEC 61850-7-3 and IEC 61850-7-4.
- The ACSI services defined in IEC 61850-7-2 are not explained in this part of IEC 61850.

## COMMUNICATION NETWORKS AND SYSTEMS FOR POWER UTILITY AUTOMATION -

## Part 9-2: Specific communication service mapping (SCSM) Sampled values over ISO/IEC 8802-3

## 1 Scope

This  part  of  IEC 61850  defines  the  specific  communication  service  mapping  ( SCSM )  for  the transmission of sampled values according to the abstract specification in IEC 61850-7-2. The mapping  is that of the abstract model  on  a mixed  stack using direct access  to an ISO/IEC 8802-3 link for the transmission of the samples in combination with IEC 61850-8-1.

Each SCSM consists of three parts:

- -a specification of the communication stack being used,
- -the mapping of the abstract specifications of IEC 61850-7 series on the real elements of the stack being used, and
- -the  implementation  specification  of  functionality,  which  is  not  covered  by  the  stack  being used.

## 2 Normative references

The following referenced documents are indispensable for the application of this document. For dated  references,  only  the  edition  cited  applies.  For  undated  references,  the  latest  edition  of the referenced document (including any amendments) applies.

IEC 60874-10-1, Connectors for optical fibres  and  cables  -  Part  10-1:  Detail  specification  for fibre optic connector type BFOC/2,5 terminated to multimode fibre type A1 (withdrawn)

IEC 60874-10-2, Connectors for optical fibres  and  cables  -  Part  10-2:  Detail  specification  for fibre optic connector type BFOC/2,5 terminated to single-mode fibre type B1 (withdrawn)

IEC 60874-10-3, Connectors for optical fibres  and  cables  -  Part  10-3:  Detail  specification  for fibre optic adaptor type BFOC/2,5 for single and multimode fibre (withdrawn)

IEC/TR 61850-1, Communication networks and systems for power utility automation  - Part 1: Introduction and overview

IEC/TS 61850-2, Communication networks and systems for power utility automation - Part 2: Glossary

IEC 61850-6, Communication  networks  and  systems  for  power  utility  automation  -  Part  6: Configuration description language for communication in electrical substations related to IEDs

IEC 61850-7-1, Communication networks and systems for power utility automation - Part 7-1: Basic communication structure - Part 7-1: Principles and models

IEC 61850-7-2, Communication networks and systems for power utility automation - Part 7-2: Basic  information  and  communication  structure  -  Abstract  communication  service  interface (ACSI)

IEC 61850-7-3, Communication networks and systems for power utility automation - Part 7-3: Basic communication structure - Common data classes

IEC 61850-7-4, Communication networks and systems for power utility automation - Part 7-4: Basic communication structure - Compatible logical node classes and data object classes

IEC 61850-8-1, Communication networks and systems for power utility automation - Part 8-1: Specific  Communication  Service  Mapping  (SCSM)  -  Mappings  to  MMS  (ISO  9506-1  and ISO 9506-2) and to ISO/IEC 8802-3

IEC/TS 62351-6, Power  systems  management  and  associated  information  exchange  -  Data and communications security - Part 6: Security for IEC 61850

IEC 62439-3:2010, Industrial  communication networks - High availability automation networks Part 3: Parallel Redundancy Protocol (PRP) and High-availability Seamless Redundancy (HSR) Amendment 1 1

ISO/IEC 7498-1:1994, Information technology -Open  Systems  Interconnection -Basic Reference Model: The Basic Model

ISO/IEC 8326:1996, Information technology - Open Systems Interconnection - Session service definition

ISO/IEC 8327-1:1996, Information technology - Open Systems Interconnection - Connectionoriented session protocols: Protocol specification

ISO/IEC 8649:1996, Information technology -Open  Systems  Interconnection -Service definition for the Associated Control Service Element

ISO/IEC 8650-1:1996, Information technology - Open Systems Interconnection - Connectionoriented protocol for the Association Control Service Element: Protocol specification

ISO/IEC 8802-3:2000, Information technology - Telecommunications and information exchange between  systems  -  Local  and  metropolitan  area  networks  -  Specific  requirements  -  Part  3: Carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specifications

ISO/IEC 8822:1994, Information  technology  -  Open  Systems  Interconnection  -  Presentation service definition

ISO/IEC 8823-1:1994, Information technology - Open Systems Interconnection - Connectionoriented presentation protocol: Protocol specification

ISO/IEC 8824-1:2008, Information  technology  -  Abstract  Syntax  Notation  One  (ASN.  1): Specification of basic notation

ISO/IEC 8825-1, Information technology  -  ASN.1  encoding  rules:  Specification  of  Basic Encoding  Rules  (BER),  Canonical  Encoding  Rules  (CER)  and  Distinguished  Encoding  Rules (DER)

ISO 9506-1:2003, Industrial  automation  systems  -  Manufacturing  Message  Specification  Part 1: Service definition

-------

1 To be published.

ISO 9506-2:2003, Industrial  automation  systems  -  Manufacturing  Message  Specification  Part 2: Protocol specification

IEEE 754:1985, IEEE Standard for Binary Floating-Point Arithmetic

IEEE 802.1Q:1998 , IEEE Standards for Local and Metropolitan Area Networks: Virtual Bridged Local Area Networks

RFC 791, Internet Protocol; IETF, available at http://www.ietf.org [cited on 2011-03-18]

RFC  792, Internet  Control  Message  Protocol;  IETF,  available  at  http://www.ietf.org [cited  on 2011-03-18]

RFC  793, Transmission  Control  Procedure;  IETF,  available  at  http://www.ietf.org [cited  on 2011-03-18]

RFC 826, Ethernet Address Resolution Protocol or Converting Network Protocol Addresses to 48.bit Ethernet Address for Transmission on Ethernet Hardware; IETF, available at http://www.ietf.org [cited on 2011-03-18]

RFC  894, A  Standard  for  the  Transmission  of  IP  Datagrams  over  Ethernet  Networks;  IETF, available at http://www.ietf.org [cited on 2011-03-18]

RFC  919, Broadcasting  Internet  Datagrams;  IETF,  available  at  http://www.ietf.org [cited  on 2011-03-18]

RFC 1006 ISO transport services on top of TCP: Version 3; IETF, available at http://www.ietf.org [cited on 2011-03-18]

RFC 1112, Host Extensions for IP multicasting; IETF, available at http://www.ietf.org [cited on 2011-03-18]

## 3 Terms and definitions

For the purposes of this document, the terms and definitions given in IEC/TS 61850-2 apply.

## 4 Abbreviations

| ACSI   | Abstract communication service interface                                          |
|--------|-----------------------------------------------------------------------------------|
| ASDU   | Application service data unit                                                     |
| ASN.1  | Abstract syntax notation number one                                               |
| APCI   | Application protocol control information                                          |
| APDU   | Application protocol data unit                                                    |
| APPID  | Application identifier                                                            |
| AUI    | Attachment unit interface                                                         |
| BER    | ASN.1 basic encoding rules                                                        |
| BS     | Bitstring                                                                         |
| c      | Conditional support. The item shall be implemented if the stated condition exists |
| CFI    | Canonical format identifier                                                       |

| CSMA/CD   | Carrier sense multiple access/collision detection                                     |
|-----------|---------------------------------------------------------------------------------------|
| DF        | Data frame                                                                            |
| DO        | Data object                                                                           |
| ECT       | Electronic current transformer                                                        |
| EVT       | Electronic voltage transformer                                                        |
| F/S       | Functional standard                                                                   |
| GOOSE     | Generic object oriented substation event                                              |
| GSSE      | Generic substation status event                                                       |
| i         | Out-of-scope: The implementation of the item is not within the scope of this standard |
| ICD       | IED configuration description                                                         |
| IED       | Intelligent electronic device                                                         |
| LSDU      | Link layer service data unit                                                          |
| m         | Mandatory support. The item shall be implemented                                      |
| MAC       | Media access control                                                                  |
| MAU       | Medium attachment unit                                                                |
| MMS       | Manufacturing message specification (ISO 9506)                                        |
| MSVCB     | Multicast sampled value control block                                                 |
| MU        | Merging unit                                                                          |
| o         | Optional support. The implementor may decide to implement the item                    |
| PDU       | Protocol data unit                                                                    |
| PICS      | Protocol implementation conformance statement                                         |
| SCSM      | Specific communication services mapping                                               |
| r         | readable                                                                              |
| SV        | Sampled value                                                                         |
| TCI       | Tag control information                                                               |
| TPID      | Tag protocol identifier                                                               |
| USVCB     | Unicast sampled value control block                                                   |
| VID       | VLAN identifier                                                                       |
| VLAN      | Virtual local area network                                                            |
| VMD       | Virtual manufacturing device                                                          |
| w         | Writeable                                                                             |
| x         | Excluded: The implementor shall not implement this item                               |
| XML       | Extensible markup language                                                            |

## 5 Communication stack

## 5.1 Overview of the protocol usage

The  OSI  reference  model  (ISO/IEC 7498-1)  defines  a  model  based  upon  the  concept  of layering of communication functions. The model includes 7 layers and specifies the functional requirements  for  each  layer  to  achieve  a  robust  communication  system.  The  model  does  not

specify the protocols to be used to achieve the functionality, nor does it restrict the solution to a single set of protocols.

Figure 1 - OSI reference model and profiles

<!-- image -->

The  use  of  ISO  application  (A-Profile)  and  transport  (T-Profile)  profiles  (see  Figure  1) describes  the  various  stack  profiles.  An  ISO  A-Profile  is  the  set  of  specifications  and agreements relating to the upper three (3) layers of the ISO OSI reference model (for example the application, presentation, and session layers). An ISO T-Profile is the set of specifications and  agreements  relating  to  the  lower  four  (4)  layers  of  the  ISO  OSI  reference  model  (for example the transport, network, datalink and physical layers).

Two combinations of A-Profiles and T-Profiles are defined in order to support the transmission of  sampled  values  including  the  access  to  the  associated SV control  block,  as  specified  in IEC 61850-7-2. The two different combinations are used for:

- client/server services based on MMS in accordance to IEC 61850-8-1;
- SV services based on datalink layer.

## 5.2 Client/server services and communication profiles

## 5.2.1 Client/server services

This  client/server  communication  profile  shall  be  used  in  addition  to  the SV communication profile  according to 5.3  if  an  access to the sampled value control block via client is required. This  profile  shall  be  used  for  any  implementation  claiming  conformance  to  this  standard  and declaring support for one of the following IEC 61850-7-2 services in Table 1.

Table 1 - Service requiring client/server communication profile

| IEC 61850-7-2 model   | IEC 61850-7-2 service     |
|-----------------------|---------------------------|
| Server                | GetServerDirectory        |
| Association           | Associate                 |
|                       | Abort                     |
|                       | Release                   |
| Logical device        | GetLogicalDeviceDirectory |
| Logical node          | GetLogicalNodeDirectory   |
|                       | Get AllD ataValues        |
| Data                  | GetDataValues             |
|                       | SetDataValues             |
|                       | GetDataDirectory          |
|                       | GetDataDefinition         |
| Data set              | GetDataSetValues          |
|                       | SetDataSetValues          |
|                       | CreateDataSet             |
|                       | DeleteDataSet             |
|                       | GetDataSetDirectory       |
| SV class model        | Get MSVCB Values          |
|                       | Set MSVCB Values          |
|                       | Get USVCB Values          |
|                       | Set USVCB Values          |

## 5.2.2 A-Profile

Table 2 shows services and protocols of the A-Profile client/server.

Table 2 - Service and protocols for client/server communication A-Profile

|                 | Specification                       | Specification         | Specification          |     |
|-----------------|-------------------------------------|-----------------------|------------------------|-----|
| OSI model layer | Name                                | Service specification | Protocol specification | m/o |
| Application     | Manufacturing message specification | ISO 9506-1:2000       | ISO 9506-2:2000        | m   |
| Application     | Association control service element | ISO/IEC 8649:1996     | ISO/IEC 8650-1:1996    | m   |
| Presentation    | Connection oriented presentation    | ISO/IEC 8822:1994     | ISO/IEC 8823-1:1994    | m   |
| Presentation    | Abstract syntax                     | ISO/IEC 8824-1:2008   | ISO/IEC 8825-1         | m   |
| Session         | Connection oriented session         | ISO/IEC 8326:1996     | ISO/IEC 8327-1:1996    | m   |

There is only one T-Profile (TCP/IP) that may be used by the client/server A-Profile.

## 5.2.3 TCP/IP T-Profile

Table 3 shows services and protocols of the TCP/IP T-Profile client/server.

Table 3 - Service and protocols for peer TCP/IP T-Profile

| OSI model layer                                        | Specification                                                                      | Specification                                          | Specification                                          |                                                        |
|--------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| OSI model layer                                        | Name                                                                               | Service specification                                  | Protocol specification                                 | m/o                                                    |
| Transport                                              | ISO transport on top of TCP                                                        | RFC 1006                                               |                                                        | m                                                      |
| Transport                                              | Internet control message protocol (ICMP)                                           | RFC 792                                                |                                                        | m                                                      |
| Transport                                              | Transmission control protocol (TCP)                                                | RFC 793                                                |                                                        | m                                                      |
| Network                                                | Internet protocol                                                                  | RFC 791                                                |                                                        |                                                        |
| Network                                                | Converting network protocol address                                                | RFC 826 (Address resolution protocol: ARP)             | RFC 826 (Address resolution protocol: ARP)             | m                                                      |
| Network                                                | Broadcasting internet datagrams                                                    | RFC 919                                                |                                                        | m                                                      |
| Network                                                | Host extensions for IP multicasting                                                | RFC 1112                                               |                                                        | m                                                      |
| Link Redundancy                                        | Parallel redundancy protocol and high availability seamless ring                   | IEC 62439-3, Amendment 1                               | IEC 62439-3, Amendment 1                               | o                                                      |
| DataLink                                               | Standard for the transmission of IP datagrams over Ethernet networks               | RFC 894                                                |                                                        | m                                                      |
| DataLink                                               | Carrier sense multiple access with collision detection ( CSMA/CD )                 | ISO/IEC 8802-3:2000                                    | ISO/IEC 8802-3:2000                                    | m                                                      |
| Physical                                               | Fibre optic transmission system 100Base-FX                                         | ISO/IEC 8802-3:2000                                    | ISO/IEC 8802-3:2000                                    | c1                                                     |
| Physical                                               | Basic optical fibre connector NOTE This is the specification for the ST connector. | IEC 60874-10-1, IEC 60874-10-2 and IEC 60874-10-3      | IEC 60874-10-1, IEC 60874-10-2 and IEC 60874-10-3      | c1                                                     |
| c1 - Recommended, but future technology could be used. | c1 - Recommended, but future technology could be used.                             | c1 - Recommended, but future technology could be used. | c1 - Recommended, but future technology could be used. | c1 - Recommended, but future technology could be used. |

## 5.3 SV service and communication profile

## 5.3.1 SV mapping overview

This SV communication profile shall be used for any implementation claiming conformance to this standard and declaring support for one of the following IEC 61850-7-2 services in Table 4.

Table 4 - Service requiring SV communication profile

| Model                               | IEC 61850-7-2 service   |
|-------------------------------------|-------------------------|
| Multicast sampled value class model | Multicast SV message    |
| Unicast sampled value class model   | Unicast SV message      |

## 5.3.2 A-Profile

Table 5 shows services and protocols of the A-Profile SV .

Table 5 - Service and protocols for SV communication A-Profile

| OSI model layer   | Specification   | Specification         | Specification          | m/o   |
|-------------------|-----------------|-----------------------|------------------------|-------|
| OSI model layer   | Name            | Service specification | Protocol specification | m/o   |
| Application       | SV service      |                       |                        | m     |
| Presentation      | Abstract syntax | ISO/IEC 8824-1:2008   | ISO/IEC 8825-1         | m     |
| Session           |                 |                       |                        |       |

Presentation layer: see additional definitions in 8.5.

Application layer: see additional definitions in 8.5.

## 5.3.3 T-Profile

The T-Profile for SV services is shown in Table 6.

Table 6 SV T-Profile

|                 | Specification                                                                      | Specification                                     | Specification                                     |     |
|-----------------|------------------------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------|-----|
| OSI model layer | Name                                                                               | Service specification                             | Protocol specification                            | m/o |
| Transport       |                                                                                    |                                                   |                                                   |     |
| Network         |                                                                                    |                                                   |                                                   |     |
| Link Redundancy | Parallel redundancy protocol and high availability seamless ring                   | IEC 62439-3, Amendment 1                          | IEC 62439-3, Amendment 1                          | o   |
| DataLink        | Priority tagging/ VLAN                                                             | IEEE 802.1Q                                       | IEEE 802.1Q                                       | m   |
| DataLink        | Carrier sense multiple access with collision detection ( CSMA/CD )                 | ISO/IEC 8802-3:2000                               | ISO/IEC 8802-3:2000                               | m   |
| Physical        | Fibre optic transmission system 100Base-FX                                         | ISO/IEC 8802-3:2000                               | ISO/IEC 8802-3:2000                               | c1  |
| Physical        | Basic optical fibre connector NOTE This is the specification for the ST connector. | IEC 60874-10-1, IEC 60874-10-2 and IEC 60874-10-3 | IEC 60874-10-1, IEC 60874-10-2 and IEC 60874-10-3 | c1  |

## 5.3.3.1 Physical layer: Specifications for the medium attachment unit ( MAU )

The optical fibre transmission system 100Base-FX according to ISO/IEC 8802-3 is recommended  as  indicated  above  because  of  requirements  relating  to  the  electromagnetic environment.

## 5.3.3.2 Link layer: Ethernet addresses

The  destination  ISO/IEC 8802-3  multicast/unicast  address  has  to  be  configured  for  the transmission  of  sampled  values.  A  unique  ISO/IEC 8802-3  source  address  shall  be  used. Recommendations of multicast address range assignments are given in Annex B.

## 5.3.3.3 Link layer: Priority tagging/virtual LAN

Priority tagging according to IEEE 802.1Q is used to separate time critical and high priority bus traffic for protection-relevant applications from low priority busload.

See Figure 2 for the structure of the tag header.

Figure 2 - Structure of the tag header

<!-- image -->

TPID (tag  protocol  identifier)  field:  Indicates  the  Ethernet  type  assigned  for  802.1Q  Ethernet encoded frames. This value shall be 0x8100.

TCI  ( tag  control  information)  fields:  User  priority:  BS3;  User  priority  value  shall  be  set  by configuration  to  separate  sampled  values  from  low  priority  busload.  If  the  priority  is  not configured, then the default values of Table 7 shall be used.

CFI (canonical format indicator): BS1 [0]; A single bit flag value. For this standard, the CFI bit value shall be reset (value = 0).

NOTE 1 If  set  (value  =  1),  an  embedded  resource identification field (E-RIF) follows the Length/Type field in the ISO/IEC 8802-3 tagged frame.

VID :  Virtual  LAN support is optional. If this mechanism will be used, the VLAN identifier ( VID ) shall be set by configuration, if it is not used, it shall be set to zero (0).

NOTE 2 As IEEE 802.1Q allows implementation with a restricted set of priorities, the higher priority frames should have a priority of 4 to 7 and the lower priority should have a priority of 1 to 3. The value 1 is the priority of untagged frames thus 0 should be avoided as it may cause unpredictable delay due to normal traffic.

Additionally,  since  sampled  values  need  to  have  potentially its own bandwidth allocation, their configured VID will be different from GOOSE and GSSE .

The default values for priority and VID shall be as defined in Table 7.

Table 7 - Default Virtual LAN IDs and priorities

| Service        |   Default VID |   Default priority |
|----------------|---------------|--------------------|
| Sampled Values |             0 |                  4 |

The general ISO/IEC 8802-3 frame structure for sampled values can be found in Annex A.

## 5.3.3.4 Link layer: Ethertype and other header information

## 5.3.3.4.1 Ethertype

Ethertypes  based  on  ISO/IEC 8802-3 MAC -sublayer  are  registered  by  the  IEEE  authority registration. GSE management,  G OOSE and  samples  values  shall  be  directly  mapped  to  the reserved Ethertype(s) and the Ethertype PDU . The assigned values are found in Table 8.

Table 8 - Assigned Ethertype values

| Use                          | Ethertype value (hexadecimal)   | APPID type   |
|------------------------------|---------------------------------|--------------|
| IEC 61850-8-1 GOOSE          | 88-B8                           | 0 0          |
| IEC 61850-8-1 GSE Management | 88-B9                           | 0 0          |
| IEC 61850-9-2 Sampled Values | 88-BA                           | 0 1          |

The Ethertype PDU and APDU octets shall be as defined in Annex A.

## 5.3.3.4.2 APPID

Application identifier. The APPID is  used to select ISO/IEC 8802-3 frames containing sampled value messages and to distinguish the application association.

The value of APPID is  the  combination of the APPID type,  defined as the two most significant bits of the value (as defined in Table 8), and the actual ID .

The reserved value range for sampled values is 0x4000 to 0x7FFF. If no APPID is configured, the default value shall be 0x4000.  The  default value is reserved  to indicate lack of configuration. It is strongly recommended to have unique, source orientated SV APPID within a system, in order to enable a filter on link layer. The configuration of APPID should be enforced by the configuration system.

## 5.3.3.4.3 Length

Number of octets including the Ethertype PDU header starting at APPID, and the length of the APDU (Application Protocol Data Unit). Therefore, the value of Length shall be 8 + m, where m is  the length of the APDU and m is less than 1493. Frames with inconsistent or invalid length field shall be discarded.

## 5.3.3.4.4 Reserved 1

The structure of the Reserved 1 is defined in Figure 3.

Figure 3 - Reserved 1

<!-- image -->

- S: Simulate. When this flag is set, the SampledValue telegram has been issued by a publisher located  in  a  test  device  and  not  by  the  publisher  as  specified  in  the  configuration  file  of  the device.
- R: Reserved. The three bits are reserved for future standardized application and shall be set to 0 as default.

Reserved security: See reserved 2 below.

## 5.3.3.4.5 Reserved 2

The  Reserved  2  field  and  the  'reserved  security'  of  Reserved  1  field  form  a  28  bits  word defined by the security standard IEC/TS 62351-6. It shall be used as defined  when SampledValue telegram with security is transmitted, otherwise it shall be set to 0.

## 5.4 Restrictions

This mapping is restricted to the mapping of the ACSI model for the transmission of sampled values.  The  model  applies  to  data  sets.  To  get  full  benefit  of  IEC 61850,  additional ACSI models need to be supported in accordance to IEC 61850-8-1. As an example, to enable the transmission  of  sampled  value  buffer,  the  associated  control  block  attribute  'SvEna'  shall  be written. However, if the client will read a list of available data sets or the contents of the data set, further models (for example logical device, logical node or data set) need to be supported.

Data sets for sampled values will be specified by using the XML language on engineering level in accordance with IEC 61850-6 to ensure interoperability.

For  the  transmission  of  sampled  value  data  sets,  the ASN.1 basic  encoding  rules  ( BER )  will be used  in  combination  with  tags  notation  harmonised  with  the MMS grammar  used  in IEC 61850-8-1.

## 6 Mapping of IEC 61850-7-2 and IEC 61850-7-3 data attributes

The mapping of attributes and common data attributes to MMS are specified in IEC 61850-8-1.

For  the  transmission  of  sampled  values  the ASN.1 ,  the  basic  encoding  rules  ( BER )  and  the common data classes defined in IEC 61850-7-3 apply.

## 7 Mapping of IEC 61850-7-2 classes and services

## 7.1 Classes of SV data sets

If  a  client/server association based on MMS is  used in addition to the transmission of SV data sets, the definitions of IEC 61850-8-1 apply for the following classes:

- -server class model;
- -association model;
- -logical device model;
- -logical node model;
- -data class model;
- -data set class model.

## 7.2 Definition of SV data sets

For the transmission of sampled values, the data sets are defined in logical node " LLN0 ".  All sampled value data sets specification are part of the IED configuration description ( ICD) .

NOTE It is assumed that the data sets used for the transmission of sampled values may include data objects from more than one logical node and are therefore allocated in LLN0 .

## 8 Mapping of the model for the transmission of sampled values

## 8.1 Overview

To ensure interoperability, the data sets for sampled values are specified in XML according to the definition in IEC 61850-6.

The sampled value class model provides reporting of sampled value data sets in an organised and  time  controlled  way,  so  that  transfer  is  very  fast  and  time  of  transfer  is  kept  constant. Sampled value control block for unicast and multicast defines the transmission characteristics of the data set they refer to. A detailed description is given in IEC 61850-7-2.

## 8.2 Mapping of the multicast sampled value control block class and services

## 8.2.1 Multicast sampled value control block definition

The  sampled  value  control  block,  as  defined  in  IEC 61850-7-2,  shall  be  pre-defined  by configuration or shall be mapped to an MMS Multicast sampled value control block ( MSVCB ) as defined in Table 9. All MSVCB components shall be of the functional constraint 'MS'.

Table 9 MMS TypeDescription definition for MSVCB MMS structure

| MMS component   | name                 | MMS TypeDescription   | r/w   | m/o   | Condi- tion Comments                                                                                                                                                                 |
|-----------------|----------------------|-----------------------|-------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MsvCBNam        | MsvCBNam             | Identifier            | r     | m     | MMS Identifier of the structure of the MsvCBName within the MMS object named: LLN0$MV e.g. LLN0$MS$<MsvCBNam>                                                                        |
| MsvCBRef        | MsvCBRef             | Visible-string        | r     | m     | T he value of this component shall contain the IEC Reference of the MsvCB. e.g. <MMSDomain>/LLN0$MS$<MsvCBNam>                                                                       |
| SvEna           | SvEna                | Boolean               | r/w   | m     | TRUE = transmission of sampled value buffer is activated. FALSE = transmission of sampled value buffer is deactivated.                                                               |
| MsvID           | MsvID                | Visible-string        | r     | m     | System-wide unique identification.                                                                                                                                                   |
| DatSet          | DatSet               | Visible-string        | r     | m     | T he value of this component shall contain the IEC reference of the DataSet conveyed by the MsvCB. This ObjectReference shall be limited to VMD or Domain scoped NamedVariableLists. |
| ConfRev         | ConfRev              | Integer               | r     | m     | Count of configuration changes regard to MSVCB.                                                                                                                                      |
| SmpRate         | SmpRate              | Integer               | r     | m     | Amount of samples (default per nominal period, see SmpMod).                                                                                                                          |
| OptFlds         | OptFlds              | BitString             |       |       |                                                                                                                                                                                      |
|                 | refresh-time         | Boolean               | r     | m     | TRUE = SV buffer contains the attribute 'RefrTm'. FALSE = attribute 'RefrTm' is not available in the SV buffer.                                                                      |
|                 | sample- synchronised | Boolean               | r     | m     | Value will be ignored. Kept to ensure backward compatibility to IEC 61850-9-2 edition 1.0                                                                                            |
|                 | sample-rate          | Boolean               | r     | m     | TRUE = SV buffer contains the attribute 'SmpRate'. FALSE = attribute 'SmpRate' is not available in the SV buffer.                                                                    |

| MMS component name   | MMS component name   | MMS TypeDescription   | r/w   | m/o   | Condi- tion   | Comments                                                                                                                                                                  |
|----------------------|----------------------|-----------------------|-------|-------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | data-set             | Boolean               | r     | m     |               | TRUE = SV buffer contains the attribute 'DatSet'. FALSE = attribute 'DatSet' is not available in the SV buffer.                                                           |
|                      | security             | Boolean               | r     | M     |               | Mapping specific attribute. TRUE = SV buffer contains the attribute 'Security'. FALSE = attribute 'Security' is not available in the SV buffer.                           |
| SmpMod               | SmpMod               | Enumerated            | r     | O     |               | smpMod specifies 0 = samples per nominal period (DEFAULT) 1 = samples per second 2 = seconds per sample If not available (backward compatibility) the default value is 0. |
| DstAddress           | DstAddress           | See Table 10          |       | M     |               | Mapping specific attribute.                                                                                                                                               |
| noASDU               | noASDU               | Integer               | r     | M     |               | Mapping specific attribute. Number of ASDU concatenated into one APDU.                                                                                                    |

Table 10 - DstAddress structure

| MMS component name   | MMS TypeDescription   | r/w   | m/o   | Condi- tion   | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|-----------------------|-------|-------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Addr                 | OCTET-STRING          | r     | M     |               | Length is 6 octets and contains the value of the destination media access control (MAC) address to which the SV message is to be sent. If DstAddress is member of a MSVCB, the address shall be an Ethernet address that has the multicast bit set to TRUE. In order to facilitate the network traffic filtering, it is recommended to use different Ethernet addresses for each DstAddress. If DstAddress is member of a USVCB, the address shall be the Ethernet address of the SV subscriber. See Annex B for multicast addressing recommendations |
| PRIORITY             | Unsigned8             | r     | M     |               | Range of values shall be limited from 0 to 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VID                  | Unsigned16            | r/w   | M     |               | Range of values shall be limited from 0 to 4095.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| APPID                | Unsigned16            | r     | M     |               | As defined in 5.3.3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## 8.2.2 M SV Services

See Table 11.

Table 11 - Mapping of multicast sampled value services

| Services of MSVCB Class   | Service                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------|
| SendM SV Message          | Transmission of MSV messages is mapped directly on data link layer as defined in 8.4 and 8.5 |
| Get MSVCB Value           | Mapped to MMS read service                                                                   |
| Set MSVCB Value           | Mapped to MMS write service                                                                  |

## 8.3 Mapping of the unicast sampled value control block class and services

## 8.3.1 Unicast sampled value control block definition

The  sampled  value  control  block,  as  defined  in  IEC 61850-7-2,  shall  be  pre-defined  by configuration  or  shall  be  mapped  to  an MMS unicast  sampled value control block ( USVCB )  as defined in Table 12. All USVCB components shall be of the functional constraint 'US'.

Table 12 MMS TypeDescription definition for USVCB MMS structure

| MMS component name   | MMS component name   | MMS type description   | r/w   | m/o   | Condi- tion   | Comments                                                                                                                                                                            |
|----------------------|----------------------|------------------------|-------|-------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsvCBNam             | UsvCBNam             | Identifier             | r     | M     |               | MMS Identifier of the structure of the UsvCBName within the MMS object named: LLN0$MV e.g. LLN0$US$<UsvCBNam>                                                                       |
| UsvCB Ref            | UsvCB Ref            | Visible-string         | r     | M     |               | The value of this component shall contain the IEC Reference of the UsvCB. e.g. '<MMSDomain>/LLN0$US$<UsvCBNam>'                                                                     |
| SvEna                | SvEna                | Boolean                | r/w   | M     |               | TRUE = transmission of sampled value buffer is activated. FALSE = transmission of sampled value buffer is deactivated.                                                              |
| Resv                 | Resv                 | Boolean                | r/w   | M     |               | TRUE = USVCB is exclusively reserved for the client that has set this value to TRUE.                                                                                                |
| UsvID                | UsvID                | Visible-string         | r     | M     |               | System-wide unique identification.                                                                                                                                                  |
| DatSet               | DatSet               | Visible-string         | r     | M     |               | The value of this component shall contain the IEC Reference of the DataSet conveyed by the UsvCB. This ObjectReference shall be limited to VMD or Domain scoped NamedVariableLists. |
| ConfRev              | ConfRev              | Integer                | r     | M     |               | Count of configuration changes regard to USVCB.                                                                                                                                     |
| SmpRate              | SmpRate              | Integer                | r     | M     |               | Amount of samples (default per nominal period see SmpMod).                                                                                                                          |
| OptFlds              | OptFlds              | BitString              |       |       |               |                                                                                                                                                                                     |
|                      | refresh-time         | Boolean                | r     | M     |               | TRUE = SV buffer contains the attribute 'RefrTm'. FALSE = attribute 'RefrTm' is not available in the SV buffer.                                                                     |
|                      | sample- synchronised | Boolean                | r     | M     |               | Value will be ignored. Kept to ensure backward compatibility to IEC 61850-9-2 edition 1.0                                                                                           |
|                      | sample-rate          | Boolean                | r     | M     |               | TRUE = SV buffer contains the attribute 'SmpRate'. FALSE = attribute 'SmpRate' is not available in the SV buffer.                                                                   |
|                      | data-set             | Boolean                | r     | M     |               | TRUE = SV buffer contains the attribute 'DatSet'. FALSE = attribute 'DatSet' is not available in the SV buffer.                                                                     |
|                      | security             | Boolean                | r     | M     |               | Mapping specific attribute. TRUE = SV buffer contains the attribute 'Security'. FALSE = attribute 'Security' is not available in the SV buffer.                                     |

| MMS component name   | MMS type description   | r/w   | m/o   | Condi- tion   | Comments                                                                                                                                                                  |
|----------------------|------------------------|-------|-------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SmpMod               | Enumerated             | r     | O     |               | smpMod specifies 0 = samples per nominal period (DEFAULT) 1 = samples per second 2 = seconds per sample If not available (backward compatibility) the default value is 0. |
| DstAddress           | See Table 10           |       | M     |               | Mapping specific attribute.                                                                                                                                               |
| noASDU               | Integer                | r     | M     |               | Mapping specific attribute. Number of ASDU concatenated into one APDU.                                                                                                    |

## 8.3.2 USV Services

See Table 13.

Table 13 - Mapping of unicast sampled value services

| Services of USVCB class   | Service                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------|
| Send USV Message          | Transmission of USV messages is mapped directly on data link layer as defined in 8.4 and 8.5 |
| Get USVCB Value           | Mapped to MMS read service                                                                   |
| Set USVCB Value           | Mapped to MMS write service                                                                  |

## 8.4 Mapping of the update of the sampled value buffer

As specified in IEC 61850-7-2, the communication system is responsible to update the buffer of the subscriber.

The update is directly mapped to an ethertype reserved for IEC 61850 applications based on ISO/IEC 8802-3 MAC - Sublayer.

The communication stack used does not provide the following functionality.

- -Initiating and checking the update of the sampled value buffer over the communication link. Optionally concatenating the update of more than one buffer into the same link layer frame. This is application layer functionality.
- -Encoding the abstract data types. This is presentation layer functionality.
- -Concatenating  the  update  of  more  than  one  transmission  buffer  into  the  same  link  layer frame as transport layer functionality is not supported. The opposite, to segment the update of  one  buffer  to  several  link  layer  frames  is  not  considered,  since  the  maximum  frame length of the link layer protocols is sufficient.
- -Translating the logical address of the subscriber in a physical MAC address.

Therefore, the additional definitions of 8.5 apply.

## 8.5 Additional definitions for the transmission of sampled values

## 8.5.1 Application layer functionality

The mapping provides the capability to concatenate more than one ASDU into one APDU before the APDU is  posted  into  the  transmission  buffer.  The  numbers  of ASDU s  which  will  be concatenated into one APDU are configurable and related to the sample rate. The

concatenation of ASDU s  is  not  dynamically  changeable in order to reduce the implementation complexity.  When  concatenating  several ASDU s  into  one  frame,  the ASDU with  the  oldest samples is the first one in the frame.

Details are shown in Figure 4.

Figure 4 - Concatenation of several ASDU's into one frame

<!-- image -->

ASN.1 grammar in relation with the basic encoding rules (BER) is used to encode the sampled value messages for transmission on ISO/IEC 8802-3.

## 8.5.2 Presentation layer functionality

For the transmission, the sampled value buffer is encoded as specified in the Table 14.

Table 14 - Encoding for the transmission of the sampled value buffer

IEC61850 DEFINITIONS ::= BEGIN IMPORTS Data FROM ISO-IEC-9506-2 IEC 61850-9-2 Specific Protocol ::= CHOICE { savPdu          [APPLICATION 0] IMPLICIT SavPdu,

| Abstract buffer format according to IEC 61850-7-2   | Abstract buffer format according to IEC 61850-7-2   | Coding in IEC 61850-9-2                                | Comments                                                                               |
|-----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------|
| Attribute name                                      | Attribute type                                      | ASN.1 basic encoding rules (BER) SavPdu ::= SEQUENCE { |                                                                                        |
|                                                     |                                                     | noASDU [0] IMPLICIT INTEGER (1..65535),                | Mapping specific attribute. Number of ASDUs, which will be concatenated into one APDU. |
|                                                     |                                                     | security [1] ANY OPTIONAL,                             | Mapping specific attribute. Reserved for future definition (e.g. digital signature).   |
|                                                     |                                                     | asdu [2] IMPLICIT SEQUENCE OF ASDU }                   | 1 to n number of ASDUs as specified before.                                            |
|                                                     |                                                     | ASDU ::= SEQUENCE {                                    |                                                                                        |
| MsvID or UsvID                                      | VISIBLE STRING                                      | svID [0] IMPLICIT VisibleString,                       | Should be a system-wide unique identification.                                         |
| DatSet                                              | ObjectReference                                     | datset [1] IMPLICIT VisibleString OPTIONAL,            | Value from the MSVCB or USVCB                                                          |

| Abstract buffer format according to IEC 61850-7-2                                                                                                                                                                      | Abstract buffer format according to IEC 61850-7-2                                                                                                                                                                      | Coding in IEC 61850-9-2                                                                                                                                                                                                | Comments                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute name                                                                                                                                                                                                         | Attribute type                                                                                                                                                                                                         | ASN.1 basic encoding rules (BER) SavPdu ::= SEQUENCE {                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SmpCnt                                                                                                                                                                                                                 | INT16U                                                                                                                                                                                                                 | smpCnt [2] IMPLICIT OCTET STRING (SIZE(2)),                                                                                                                                                                            | Will be incremented each time a new sampling value is taken. The counter shall be set to zero if the sampling is synchronised by clock signal and the synchronising signal occurs. When sync pulses are used to synchronise merging units, the counter shall be set to zero with every sync pulse. The value 0 shall be given to the data set where the sampling of the primary current coincides with the sync pulse. |
| ConfRev                                                                                                                                                                                                                | INT32U                                                                                                                                                                                                                 | confRev [3] IMPLICIT OCTET STRING (SIZE(4)),                                                                                                                                                                           | Value from the MSVCB or USVCB. The OCTET STRING is interpreted as INT32U as defined in Table 15.                                                                                                                                                                                                                                                                                                                       |
| RefrTm                                                                                                                                                                                                                 | TimeStamp                                                                                                                                                                                                              | refrTm [4] IMPLICIT UtcTime OPTIONAL,                                                                                                                                                                                  | RefrTm contains the refresh time of the SV buffer.                                                                                                                                                                                                                                                                                                                                                                     |
| SmpSynch                                                                                                                                                                                                               | INT8U                                                                                                                                                                                                                  | smpSynch [5] IMPLICIT OCTET STRING (SIZE(1)),                                                                                                                                                                          | 0= SV are not synchronised by an external clock signal. 1= SV are synchronised by a clock signal from an unspecified local area clock. 2= SV are synchronised by a global area clock signal (time traceable). 5 to 254= SV are synchronised by a clock signal from a local area clock identified by this value. 3;4;255= Reserved values - Do not use.                                                                 |
| SmpRate                                                                                                                                                                                                                | INT16U                                                                                                                                                                                                                 | smpRate [6] IMPLICIT OCTET STRING (SIZE(2)) OPTIONAL,                                                                                                                                                                  | Value from the MSVCB or USVCB. The OCTET STRING is interpreted as INT16U as defined in Table 15.                                                                                                                                                                                                                                                                                                                       |
| Sample [1..n]                                                                                                                                                                                                          | Type depends on the CDC defined in IEC 61850-7-3.                                                                                                                                                                      | sample [7] IMPLICIT OCTET STRING (SIZE(n))                                                                                                                                                                             | List of data values related to the data set definition. For the encoding of the Data, the rules for the encoding of the basic data types shall apply as defined in Table 15. The SIZE (n) is the cumulated size of all the data conveyed as defined in the DataSet.                                                                                                                                                    |
| SmpMod                                                                                                                                                                                                                 | INT16U                                                                                                                                                                                                                 | smpMod [8] IMPLICIT OCTET STRING (SIZE(2)) OPTIONAL }                                                                                                                                                                  | Value from the MSVCB or USVCB. The OCTET STRING is interpreted as INT16U as defined in Table 15.                                                                                                                                                                                                                                                                                                                       |
| NOTE The usage of the OptFlds attribute according to IEC 61850-7-2 is not necessary, because the relating attributes RefrTm, security, SmpRate and DatSet will be signed as optional via the ASN.1 attribute directly. | NOTE The usage of the OptFlds attribute according to IEC 61850-7-2 is not necessary, because the relating attributes RefrTm, security, SmpRate and DatSet will be signed as optional via the ASN.1 attribute directly. | NOTE The usage of the OptFlds attribute according to IEC 61850-7-2 is not necessary, because the relating attributes RefrTm, security, SmpRate and DatSet will be signed as optional via the ASN.1 attribute directly. | NOTE The usage of the OptFlds attribute according to IEC 61850-7-2 is not necessary, because the relating attributes RefrTm, security, SmpRate and DatSet will be signed as optional via the ASN.1 attribute directly.                                                                                                                                                                                                 |

... }

For the tag definition of basic data types, see 8.6.

## 8.6 Definitions for basic data types - Presentation layer functionality

Table 15 shows the encoding for the basic data types used for the Data values referenced by the data set members.

Table 15 - Encoding for the basic data types

| Data types according to IEC 61850-7-2   | Encoding in data set                         | Comments   |
|-----------------------------------------|----------------------------------------------|------------|
| BOOLEAN                                 | 8 Bit set to 0 FALSE; anything else = TRUE   |            |
| INT8                                    | 8 Bit Big Endian                             | signed     |
| INT16                                   | 16 Bit Big Endian                            | signed     |
| INT32                                   | 32 Bit Big Endian                            | signed     |
| INT64                                   | 64 Bit Big Endian                            | signed     |
| INT8U                                   | 8 Bit Big Endian                             | unsigned   |
| INT16U                                  | 16 Bit Big Endian                            | unsigned   |
| INT24U                                  | 24 Bit Big Endian                            | unsigned   |
| INT32U                                  | 32 Bit Big Endian                            | unsigned   |
| FLOAT32                                 | 32 Bit IEEE Floating Point (IEEE 754)        |            |
| FLOAT64                                 | 64 Bit IEEE Floating Point (IEEE 754)        |            |
| ENUMERATED                              | 32 Bit Big Endian                            |            |
| CODED ENUM                              | 32 Bit Big Endian                            |            |
| OCTET STRING                            | 20 Bytes ASCII Text, Null terminated         |            |
| VISIBLE STRING                          | 35 Bytes ASCII Text, Null terminated         |            |
| UNICODE STRING                          | 20 Bytes ASCII Text, Null terminated         |            |
| ObjectName                              | 20 Bytes ASCII Text, Null terminated         |            |
| ObjectReference                         | 20 Bytes ASCII Text, Null terminated         |            |
| TimeStamp                               | 64 Bit Timestamp as defined in IEC 61850-8-1 |            |
| EntryTime                               | 48 Bit Timestamp as defined in IEC 61850-8-1 |            |
| Data types according to IEC 61850-8-1   | Encoding in data set                         | Comments   |
| BITSTRING                               | 32 Bit Big Endian                            |            |

## 9 Conformance

## 9.1 Notation

For Subclause 9.2 to Clause 11, see the abbreviations given in Clause 4.

## 9.2 PICS

## 9.2.1 Profile conformance

Table 16 and Table 17 define the basic conformance statement.

Table 16 PICS for A-Profile support

|    |                         | Client   | Server   | Value/comment   |
|----|-------------------------|----------|----------|-----------------|
|    |                         | F/S      | F/S      |                 |
| A1 | Client/Server A-Profile | c1       | c1       | Refer to 5.2    |
| A2 | SV A-Profile            | c2       | c2       | Refer to 5.3    |

c1 - Shall be 'm' if support for any service specified in Table 1 is declared within the ACSI basic conformance statement.

c2 - Shall be 'm' if support for any service specified in Table 4 is declared within the ACSI basic conformance statement.

Table 17 PICS for T-Profile support

|    |                  | Client   | Server   | Value/comment   |
|----|------------------|----------|----------|-----------------|
|    |                  | F/S      | F/S      |                 |
| T1 | TCP/IP T-Profile | c1       | c1       |                 |
| T2 | SV T-Profile     | c2       | c2       |                 |

c1 - Shall be 'm' if support for A1 is declared. Otherwise, shall be 'i'

c2 - Shall be 'm' if support for A2 is declared. Otherwise, shall be 'i'.

## 9.2.2 SV Services

This  subclause  describes  the  protocol  implementation  conformance  statement  for  sampled values services based on the IEC 61850-7-2 basic conformance statement. See Table 18.

Table 18 SV conformance statement

| Services         | Client/ subscriber   | Server/ publisher   | Value/comment   |
|------------------|----------------------|---------------------|-----------------|
| Multicast        |                      |                     |                 |
| SendM SV Message | c1                   | c1                  |                 |
| Get MSVCB Values | c2                   | c2                  |                 |
| Set MSVCB Values | c3                   | c3                  |                 |
| Unicast          |                      |                     |                 |
| Send USV Message | c1                   | c1                  |                 |
| Get USVCB Values | c2                   | c2                  |                 |
| Set USVCB Values | c3                   | c3                  |                 |

c1 - Shall declare 'm' for at least one ( MSV or USV ) as declared within ACSI basic conformance statement.

c2 - Shall be 'o' as declared within ACSI basic conformance statement. See IEC 61850-8-1, Table 117 'Read Conformance Statement'.

c3 - Shall be 'o' as declared within ACSI basic conformance statement. See IEC 61850-8-1, Table 118 'Write Conformance Statement'.

## 10  Substation configuration language (SCL)

Conforming implementations shall support the substation configuration language as defined in IEC 61850-6 for exchange between engineering tools.

## 11  SCSM specific address element definitions

This  clause  defines  the  xs:string  types  that  are  allowed  for  the SV addressing  as  type parameters of the P element of the Address element. The values and character restrictions are defined in Table 19.

Table 19 - Definitions for SV SCL

| P-type designation                                  | Description                                         | m/o                                                 | Restrictions/comments                                                                                                 |
|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| MAC-Address                                         | Media Access Address value                          | m                                                   | Shall be 6 groups of 2 visible characters separated by hyphens (-). Characters shall be limited to 0 to 9 and A to F. |
| APPID                                               | Application Identifier                              | o                                                   | Shall be 4 characters. Characters shall be limited to 0 to 9 and A to F.                                              |
| VLAN-PRIORITY                                       | VLAN User Priority                                  | c1                                                  | Shall be a single character. Characters shall be limited to 0 to 7.                                                   |
| VLAN-ID                                             | VLAN ID                                             | o                                                   | Shall be 3 characters. Characters shall be limited to 0 to 9 and A to F.                                              |
| c1 - Shall only be present if VLAN is also present. | c1 - Shall only be present if VLAN is also present. | c1 - Shall only be present if VLAN is also present. | c1 - Shall only be present if VLAN is also present.                                                                   |

## Annex A

(informative)

## ISO/IEC 8802-3 frame format and ASN.1 basic encoding rules

## A.1 ISO/IEC 8802-3 frame format

See Figures A.1, A.2 and A.3.

<!-- image -->

IEC   1790/11

Figure A.1 - ISO/IEC 8802-3 frame format - No link redundancy

<!-- image -->

IEC   1791/11

Figure A.2 - ISO/IEC 8802-3 frame format - Link redundancy: HSR

<!-- image -->

IEC   1792/11

Figure A.3 - ISO/IEC 8802-3 frame format - Link redundancy: PRP

## A.2 ASN.1 basic encoding rules (BER)

ASN.1 basic  encoding  rules  (as  specified  in  ISO/IEC 8825-1)  will  be  used  for  encoding  and decoding of sampled values. The main encoding principles are shown as an overview.

The BER transfer syntax has the format of a triplet TLV (Type, Length, Value) or (Tag, Length, Value) as shown in Figure A.4.

All  fields  (T,  L,  V)  are  series  of  octets.  The  value  V  can  be  a  triplet  TLV  itself,  if  it  is constructed.

The  transfer  syntax  is  octet-based  and  'big  endian'-oriented.  The  length  field  L  defines  the length of each TLV triplet.

Figure A.4 - Basic encoding rules format

<!-- image -->

The tag octets correspond to the encoding of the tag of the value type. Figure A.5 shows the two formats of the tag octets T.

Figure A.5 - Format of the tag octets

<!-- image -->

## A.3 Example for an ASN.1 coded APDU frame structure

The example in Figure A.6 shows the APDU frame structure with 4 concatenated ASDU s.

<!-- image -->

ASN.1

Tag

L = Length

Figure A.6 - Example for an ASN.1 coded APDU frame structure

IEC   1795/11

## Annex B

(informative)

## Multicast address selection

In  order  to  increase  the  overall  performance  of  multicast  message  reception  (for  example GOOSE , GSSE , and Sampled Values), it is preferable to have the media access controller ( MAC ) hardware perform the filtering. The hash algorithms in the various integrated circuits do vary. It is  recommended,  as  a  system  integrator,  to  evaluate  the  impact  of  these  algorithms  when assigning destination multicast addresses.

Vendors  of  IEC 61850-8-1  or  IEC 61850-9-2  implementations  that  send  these  types  of messages  should  provide  recommendations  of  addressing  based  upon  the MAC IC's  hash algorithms. One such recommendation might appear as follows:

The multicast addresses (octet string of size 6) used within this standard will have the following structure.

- -The first three octets are assigned by IEEE with 01-0C-CD.
- -The fourth octet will be 01 for GOOSE , 02 for GSSE , and 04 for multicast sampled values.
- -The  last  two  octets  will  be  used  as  individual  addresses  assigned  by  range  defined  in Table B.1.

Table B.1 - Recommended multicast addressing example

|                          | Recommended address range assignments   | Recommended address range assignments   |
|--------------------------|-----------------------------------------|-----------------------------------------|
| Service                  | Starting address (hexadecimal)          | Ending address (hexadecimal)            |
| GOOSE                    | 01-0C-CD-01-00-00                       | 01-0C-CD-01-01-FF                       |
| GSSE                     | 01-0C-CD-02-00-00                       | 01-0C-CD-02-01-FF                       |
| Multicast sampled values | 01-0C-CD-04-00-00                       | 01-0C-CD-04-01-FF                       |

\_\_\_\_\_\_\_\_\_\_\_

## SOMMAIRE

| AVANT-PROPOS..................................................................................................................36   | AVANT-PROPOS..................................................................................................................36                                                                   | AVANT-PROPOS..................................................................................................................36                                                                                                              | AVANT-PROPOS..................................................................................................................36                                                                                                              |                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                    |                                                                                                                                                                                                    |                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                               | INTRODUCTION...................................................................................................................38  |
| 1                                                                                                                                  | Domaine d'application.....................................................................................................39                                                                       | Domaine d'application.....................................................................................................39                                                                                                                  | Domaine d'application.....................................................................................................39                                                                                                                  |                                                                                                                                    |
| 2                                                                                                                                  | Références normatives ...................................................................................................39                                                                        | Références normatives ...................................................................................................39                                                                                                                   | Références normatives ...................................................................................................39                                                                                                                   |                                                                                                                                    |
| 3                                                                                                                                  | Termes et définitions ......................................................................................................41                                                                     | Termes et définitions ......................................................................................................41                                                                                                                | Termes et définitions ......................................................................................................41                                                                                                                |                                                                                                                                    |
| 4                                                                                                                                  | Abréviations....................................................................................................................42                                                                 | Abréviations....................................................................................................................42                                                                                                            | Abréviations....................................................................................................................42                                                                                                            |                                                                                                                                    |
|                                                                                                                                    | 5.1                                                                                                                                                                                                | Vue                                                                                                                                                                                                                                           | Vue                                                                                                                                                                                                                                           |                                                                                                                                    |
|                                                                                                                                    | 5.2                                                                                                                                                                                                | d'ensemble de l'utilisation du protocole ...........................................................43 Services client/serveur et profils de communication................................................44                                  | d'ensemble de l'utilisation du protocole ...........................................................43 Services client/serveur et profils de communication................................................44                                  |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 5.2.1                                                                                                                                                                                                                                         | Services client/serveur...............................................................................44                                                                                                                                      |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 5.2.2                                                                                                                                                                                                                                         | "A-Profile"..................................................................................................44                                                                                                                               |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 5.2.3                                                                                                                                                                                                                                         | "T-Profile" TCP/IP......................................................................................45                                                                                                                                    |                                                                                                                                    |
|                                                                                                                                    | 5.3                                                                                                                                                                                                | Service SV et profil de communication....................................................................45                                                                                                                                   | Service SV et profil de communication....................................................................45                                                                                                                                   |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 5.3.1                                                                                                                                                                                                                                         | Présentation générale de la mise en correspondance SV                                                                                                                                                                                         | ............................45                                                                                                     |
|                                                                                                                                    |                                                                                                                                                                                                    | 5.3.2                                                                                                                                                                                                                                         | "A-Profile"..................................................................................................46                                                                                                                               |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 5.3.3                                                                                                                                                                                                                                         | "T-Profile"                                                                                                                                                                                                                                   | ..................................................................................................46                               |
|                                                                                                                                    | 5.4                                                                                                                                                                                                | Restrictions ...........................................................................................................49                                                                                                                    | Restrictions ...........................................................................................................49                                                                                                                    |                                                                                                                                    |
| 6                                                                                                                                  | Mise en correspondance des attributs de données CEI 61850-7-2 et CEI 61850-7-3........49                                                                                                           | Mise en correspondance des attributs de données CEI 61850-7-2 et CEI 61850-7-3........49                                                                                                                                                      | Mise en correspondance des attributs de données CEI 61850-7-2 et CEI 61850-7-3........49                                                                                                                                                      |                                                                                                                                    |
| 7                                                                                                                                  | Mise en correspondance des classes et des services CEI 61850-7-2...............................50                                                                                                  | Mise en correspondance des classes et des services CEI 61850-7-2...............................50                                                                                                                                             | Mise en correspondance des classes et des services CEI 61850-7-2...............................50                                                                                                                                             |                                                                                                                                    |
|                                                                                                                                    | 7.1                                                                                                                                                                                                | Classes des ensembles de données de valeurs échantillonnées ( SV data sets)......................................................................................................................50                                           | Classes des ensembles de données de valeurs échantillonnées ( SV data sets)......................................................................................................................50                                           |                                                                                                                                    |
|                                                                                                                                    | 7.2                                                                                                                                                                                                | Définition des ensembles de données de valeurs échantillonnées ( SV data sets)......................................................................................................................50                                        | Définition des ensembles de données de valeurs échantillonnées ( SV data sets)......................................................................................................................50                                        |                                                                                                                                    |
| 8                                                                                                                                  | Mise en correspondance du modèle pour la transmission des valeurs échantillonnées...............................................................................................................50 | Mise en correspondance du modèle pour la transmission des valeurs échantillonnées...............................................................................................................50                                            | Mise en correspondance du modèle pour la transmission des valeurs échantillonnées...............................................................................................................50                                            |                                                                                                                                    |
|                                                                                                                                    | 8.1                                                                                                                                                                                                | Présentation générale............................................................................................50                                                                                                                           | Présentation générale............................................................................................50                                                                                                                           |                                                                                                                                    |
|                                                                                                                                    | 8.2                                                                                                                                                                                                | Mise en correspondance de classes et de services du bloc de contrôle des valeurs échantillonnées multidiffusion ....................................................................50                                                        | Mise en correspondance de classes et de services du bloc de contrôle des valeurs échantillonnées multidiffusion ....................................................................50                                                        |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 8.2.1                                                                                                                                                                                                                                         | Définition du bloc de contrôle des valeurs échantillonnées multidiffusion .............................................................................................50                                                                     |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 8.2.2                                                                                                                                                                                                                                         | Services MSV                                                                                                                                                                                                                                  | .............................................................................................52                                    |
|                                                                                                                                    | 8.3                                                                                                                                                                                                | Mise en correspondance de classes et de services du bloc de contrôle des valeurs échantillonnées envoi individuel .................................................................52                                                         | Mise en correspondance de classes et de services du bloc de contrôle des valeurs échantillonnées envoi individuel .................................................................52                                                         |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 8.3.1 Définition                                                                                                                                                                                                                              | du bloc de contrôle des valeurs échantillonnées envoi individuel ...................................................................................................52                                                                        |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 8.3.2                                                                                                                                                                                                                                         | Services USV .............................................................................................54                                                                                                                                  |                                                                                                                                    |
|                                                                                                                                    | 8.4                                                                                                                                                                                                | Mise en correspondance de la mise à jour de la mémoire tampon des valeurs échantillonnées .....................................................................................................54                                             | Mise en correspondance de la mise à jour de la mémoire tampon des valeurs échantillonnées .....................................................................................................54                                             |                                                                                                                                    |
|                                                                                                                                    | 8.5                                                                                                                                                                                                | Définitions supplémentaires pour la transmission des valeurs échantillonnées........54                                                                                                                                                        | Définitions supplémentaires pour la transmission des valeurs échantillonnées........54                                                                                                                                                        |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 8.5.1                                                                                                                                                                                                                                         | Fonctionnalité de la couche application ......................................................54                                                                                                                                              |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    | 8.5.2                                                                                                                                                                                                                                         | Fonctionnalité de la couche présentation....................................................55                                                                                                                                                |                                                                                                                                    |
| 9                                                                                                                                  | 8.6                                                                                                                                                                                                | Définitions relatives aux types de données de base - Fonctionnalité de la couche présentation ..............................................................................................57                                                | Définitions relatives aux types de données de base - Fonctionnalité de la couche présentation ..............................................................................................57                                                |                                                                                                                                    |
|                                                                                                                                    |                                                                                                                                                                                                    |                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                               | Conformité......................................................................................................................58 |
|                                                                                                                                    | 9.1                                                                                                                                                                                                | Notation.................................................................................................................58                                                                                                                   | Notation.................................................................................................................58                                                                                                                   |                                                                                                                                    |
|                                                                                                                                    | 9.2                                                                                                                                                                                                | PICS ......................................................................................................................58 9.2.1 Conformité des profils ................................................................................58 | PICS ......................................................................................................................58 9.2.1 Conformité des profils ................................................................................58 |                                                                                                                                    |

|                                                                                                                                                                                                                                      | 9.2.2 Services SV                                                                                                                                                                                                                    | ...............................................................................................59   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 10                                                                                                                                                                                                                                   | Langage de configuration de poste (SCL)........................................................................59                                                                                                                    |                                                                                                     |
| 11                                                                                                                                                                                                                                   | Définitions d'éléments d'adresses spécifiques SCSM ......................................................59                                                                                                                          |                                                                                                     |
| Annexe A (informative) Format de la trame ISO/CEI 8802-3 et règles de codage de base ASN.1 ...........................................................................................................................60             | Annexe A (informative) Format de la trame ISO/CEI 8802-3 et règles de codage de base ASN.1 ...........................................................................................................................60             |                                                                                                     |
| Annexe B (informative) Sélection d'adresse multidiffusion (multicast) ...................................65                                                                                                                          | Annexe B (informative) Sélection d'adresse multidiffusion (multicast) ...................................65                                                                                                                          |                                                                                                     |
| Figure 1 - Modèle de référence OSI et profils........................................................................43                                                                                                              | Figure 1 - Modèle de référence OSI et profils........................................................................43                                                                                                              |                                                                                                     |
| Figure 2 - Structure de l'entête de l'étiquette                                                                                                                                                                                      | Figure 2 - Structure de l'entête de l'étiquette                                                                                                                                                                                      | .........................................................................47                         |
| Figure 3 - "Reserved 1" ........................................................................................................49                                                                                                   | Figure 3 - "Reserved 1" ........................................................................................................49                                                                                                   |                                                                                                     |
| Figure 4 - Concaténation de plusieurs ASDU en une trame ...................................................55                                                                                                                        | Figure 4 - Concaténation de plusieurs ASDU en une trame ...................................................55                                                                                                                        |                                                                                                     |
| Figure A.1 - Format de la trame ISO/CEI 8802-3 - Pas de redondance de liaison..................60                                                                                                                                    | Figure A.1 - Format de la trame ISO/CEI 8802-3 - Pas de redondance de liaison..................60                                                                                                                                    |                                                                                                     |
| Figure A.2 - Format de la trame ISO/CEI 8802-3 - Redondance de liaison: HSR...................61                                                                                                                                     | Figure A.2 - Format de la trame ISO/CEI 8802-3 - Redondance de liaison: HSR...................61                                                                                                                                     |                                                                                                     |
| Figure A.3 - Format de la trame ISO/CEI 8802-3 - Redondance de liaison: PRP ...................62                                                                                                                                    | Figure A.3 - Format de la trame ISO/CEI 8802-3 - Redondance de liaison: PRP ...................62                                                                                                                                    |                                                                                                     |
| Figure A.4 - Format des règles de codage de base ...............................................................63                                                                                                                   | Figure A.4 - Format des règles de codage de base ...............................................................63                                                                                                                   |                                                                                                     |
| Figure A.5 - Format des octets "Tag" (étiquette) ...................................................................63                                                                                                               | Figure A.5 - Format des octets "Tag" (étiquette) ...................................................................63                                                                                                               |                                                                                                     |
| Figure A.6 - Exemple de structure de trame APDU codée ASN.1 ............................................64                                                                                                                           | Figure A.6 - Exemple de structure de trame APDU codée ASN.1 ............................................64                                                                                                                           |                                                                                                     |
| Tableau 1 - Service exigeant un profil de communication client/serveur ................................44                                                                                                                            | Tableau 1 - Service exigeant un profil de communication client/serveur ................................44                                                                                                                            |                                                                                                     |
| Tableau 2 - Services et protocoles relatifs au profil de communication client/serveur du "A-Profile" .............................................................................................................................44 | Tableau 2 - Services et protocoles relatifs au profil de communication client/serveur du "A-Profile" .............................................................................................................................44 |                                                                                                     |
| Tableau 3 - Services et protocoles relatifs au "T-Profile" TCP/IP ...........................................45                                                                                                                      | Tableau 3 - Services et protocoles relatifs au "T-Profile" TCP/IP ...........................................45                                                                                                                      |                                                                                                     |
| Tableau 4 - Services exigeant un profil de communication SV ...............................................46                                                                                                                        | Tableau 4 - Services exigeant un profil de communication SV ...............................................46                                                                                                                        |                                                                                                     |
| Tableau 5 - Services et protocoles relatifs au profil de communication SV du "A-Profile"........46                                                                                                                                   | Tableau 5 - Services et protocoles relatifs au profil de communication SV du "A-Profile"........46                                                                                                                                   |                                                                                                     |
| Tableau 6 - "T-Profile" SV .....................................................................................................46                                                                                                   | Tableau 6 - "T-Profile" SV .....................................................................................................46                                                                                                   |                                                                                                     |
| Tableau 7 - Valeurs par défaut des ID "Virtual LAN" et des priorités......................................48                                                                                                                         | Tableau 7 - Valeurs par défaut des ID "Virtual LAN" et des priorités......................................48                                                                                                                         |                                                                                                     |
| Tableau 8 - Valeurs Ethertype assignées ..............................................................................48                                                                                                             | Tableau 8 - Valeurs Ethertype assignées ..............................................................................48                                                                                                             |                                                                                                     |
| Tableau 9 - Définition MMS TypeDescription pour structure MSVCB MMS ...............................51                                                                                                                                | Tableau 9 - Définition MMS TypeDescription pour structure MSVCB MMS ...............................51                                                                                                                                |                                                                                                     |
| Tableau 10 - Structure DstAddress .......................................................................................52                                                                                                          | Tableau 10 - Structure DstAddress .......................................................................................52                                                                                                          |                                                                                                     |
| Tableau 11 - Mise en correspondance des services des valeurs échantillonnées multidiffusion ........................................................................................................................52               | Tableau 11 - Mise en correspondance des services des valeurs échantillonnées multidiffusion ........................................................................................................................52               |                                                                                                     |
| Tableau 12 - Définition MMS TypeDescription pour structure USVCB MMS ..............................53                                                                                                                                | Tableau 12 - Définition MMS TypeDescription pour structure USVCB MMS ..............................53                                                                                                                                |                                                                                                     |
| Tableau 13 - Mise en correspondance des services des valeurs échantillonnées envoi individuel ..............................................................................................................................54       | Tableau 13 - Mise en correspondance des services des valeurs échantillonnées envoi individuel ..............................................................................................................................54       |                                                                                                     |
| Tableau 14 - Encodage relatif à la transmission de la mémoire tampon des valeurs échantillonnées .....................................................................................................................55             | Tableau 14 - Encodage relatif à la transmission de la mémoire tampon des valeurs échantillonnées .....................................................................................................................55             |                                                                                                     |
| Tableau 15 - Encodage relatif aux types de données de base ...............................................57                                                                                                                         | Tableau 15 - Encodage relatif aux types de données de base ...............................................57                                                                                                                         |                                                                                                     |
| Tableau 16 - PICS prenant en charge le "A-Profile" ...............................................................58                                                                                                                 | Tableau 16 - PICS prenant en charge le "A-Profile" ...............................................................58                                                                                                                 |                                                                                                     |
| Tableau 17 - PICS prenant en charge le "T-Profile"................................................................58                                                                                                                 | Tableau 17 - PICS prenant en charge le "T-Profile"................................................................58                                                                                                                 |                                                                                                     |
| Tableau 18 - Déclaration de conformité SV ............................................................................59                                                                                                             | Tableau 18 - Déclaration de conformité SV ............................................................................59                                                                                                             |                                                                                                     |
| Tableau 19 - Définitions relatives au SCL SV .........................................................................59                                                                                                             | Tableau 19 - Définitions relatives au SCL SV .........................................................................59                                                                                                             |                                                                                                     |
| Tableau B.1 - Exemple d'adressage multidiffusion recommandé ...........................................65                                                                                                                            | Tableau B.1 - Exemple d'adressage multidiffusion recommandé ...........................................65                                                                                                                            |                                                                                                     |

## COMMISSION ÉLECTROTECHNIQUE INTERNATIONALE

\_\_\_\_\_\_\_\_\_\_\_\_

## RÉSEAUX ET SYSTÈMES DE COMMUNICATION POUR L'AUTOMATISATION DES SYSTÈMES ÉLECTRIQUES -

## Partie 9-2: Mise en correspondance des services de communication spécifiques (SCSM) Valeurs échantillonnées sur ISO/CEI 8802-3

## AVANT-PROPOS

- 1) La Commission Electrotechnique Internationale (CEI) est une organisation mondiale de normalisation composée de l'ensemble des comités électrotechniques nationaux (Comités nationaux de la CEI). La CEI a pour objet de favoriser  la  coopération  internationale  pour  toutes  les  questions  de  normalisation  dans  les  domaines  de l'électricité et de l'électronique. A cet effet, la CEI - entre autres activités - publie des Normes internationales, des Spécifications techniques, des Rapports techniques, des Spécifications accessibles au public (PAS) et des Guides  (ci-après  dénommés  "Publication(s)  de  la  CEI").  Leur  élaboration  est  confiée  à  des  comités  d'études, aux  travaux  desquels  tout  Comité  national  intéressé  par  le  sujet  traité  peut  participer.  Les  organisations internationales, gouvernementales et non gouvernementales, en liaison avec la CEI, participent également aux travaux.  La  CEI  collabore  étroitement  avec  l'Organisation  Internationale  de  Normalisation  (ISO),  selon  des conditions fixées par accord entre les deux organisations.
- 2) Les décisions ou accords officiels de la CEI concernant les questions techniques représentent, dans la mesure du  possible,  un  accord  international  sur  les  sujets  étudiés,  étant  donné  que  les  Comités  nationaux  de  la  CEI intéressés sont représentés dans chaque comité d'études.
- 3) Les  Publications  de  la  CEI  se  présentent  sous  la  forme  de  recommandations  internationales  et  sont  agréées comme telles par les Comités nationaux de la CEI. Tous les efforts raisonnables sont entrepris afin que la CEI s'assure de l'exactitude du contenu technique de ses publications; la CEI ne peut pas être tenue responsable de l'éventuelle mauvaise utilisation ou interprétation qui en est faite par un quelconque utilisateur final.
- 4) Dans le but d'encourager l'uniformité internationale, les Comités nationaux de la CEI s'engagent, dans toute la mesure  possible,  à  appliquer  de  façon  transparente  les  Publications  de  la  CEI  dans  leurs  publications nationales  et  régionales.  Toutes  divergences  entre  toutes  Publications  de  la  CEI  et  toutes  publications nationales ou régionales correspondantes doivent être indiquées en termes clairs dans ces dernières.
- 5) La  CEI  elle-même  ne  fournit  aucune  attestation  de  conformité.  Des  organismes  de  certification  indépendants fournissent  des  services  d'évaluation  de  conformité  et,  dans  certains  secteurs,  accèdent  aux  marques  de conformité  de  la  CEI.  La  CEI  n'est  responsable  d'aucun  des  services  effectués  par  les  organismes  de certification indépendants.
- 6) Tous les utilisateurs doivent s'assurer qu'ils sont en possession de la dernière édition de cette publication.
- 7) Aucune  responsabilité  ne  doit  être imputée  à  la CEI, à ses  administrateurs,  employés,  auxiliaires  ou mandataires,  y  compris  ses  experts  particuliers  et  les  membres  de  ses  comités  d'études  et  des  Comités nationaux  de  la  CEI,  pour  tout  préjudice  causé  en  cas  de  dommages  corporels  et  matériels,  ou  de  tout  autre dommage de quelque nature que ce soit, directe ou indirecte, ou pour supporter les coûts (y compris les frais de justice)  et  les  dépenses  découlant de la publication ou de l'utilisation de cette Publication de la CEI ou de toute autre Publication de la CEI, ou au crédit qui lui est accordé.
- 8) L'attention  est  attirée  sur  les  références  normatives  citées  dans  cette  publication.  L'utilisation  de  publications référencées est obligatoire pour une application correcte de la présente publication.
- 9) L'attention  est  attirée  sur  le  fait  que  certains  des  éléments  de  la  présente  Publication  de  la  CEI  peuvent  faire l'objet de droits de brevet. La CEI ne saurait être tenue pour responsable de ne pas avoir identifié de tels droits de brevets et de ne pas avoir signalé leur existence.

La  Norme  internationale  CEI 61850-9-2  a  été  établie  par  le  comité  d'études  57  de  la  CEI: Gestion des systèmes de puissance et échanges d'informations associés.

Le texte de cette norme est issu des documents suivants:

| FDIS         | Rapport de vote   |
|--------------|-------------------|
| 57/1133/FDIS | 57/1161/RVD       |

Le rapport de vote indiqué dans le tableau ci-dessus donne toute information sur le vote ayant abouti à l'approbation de cette norme.

Cette  deuxième  édition  annule  et  remplace  la  première  édition  publiée  en  2004  et  constitue une révision technique.

Les modifications principales par rapport à la première édition sont les suivantes:

- l'adjonction d'une couche optionnelle de redondance de liaison (Tableaux 3 à 6);
- la redéfinition des champs "reserved" dans la couche de liaison (5.3.3.4);
- l'évolution des composants USVCB et MSVCB (Tableaux 9, 10, 12);
- l'évolution  de  l'encodage  relatif  à  la  transmission  de  la  mémoire  tampon  des  valeurs échantillonnées (Tableau 14).

Cette publication a été rédigée selon les Directives ISO/CEI, Partie 2.

Une  liste  de  toutes  les  parties  de  la  série  CEI 61850,  sous  le  titre  général: Réseaux  et systèmes de communication  pour l'automatisation  des  système s électriques, peut être consultée sur le site web de la CEI.

Le comité a décidé que le contenu de cette publication ne sera pas modifié avant la date de stabilité  indiquée  sur  le  site  web  de  la  CEI  sous  "http://webstore.iec.ch"  dans  les  données relatives à la publication recherchée. A cette date, la publication sera

- reconduite,
- supprimée,
- remplacée par une édition révisée, ou
- amendée.

## INTRODUCTION

La  présente  partie  de  la  CEI 61850  définit  le SCSM pour  les  valeurs  échantillonnées  sur ISO/CEI 8802-3.  Le  but  de  cette  définition  du SCSM est  d'inclure  la  mise  en  correspondance complète du modèle de valeurs échantillonnées.

La présente partie de la CEI 61850 s'applique aux transformateurs électroniques de courant et de tension (ECT et EVT ayant une sortie numérique), aux unités de fusion de données et aux dispositifs électroniques intelligents, par exemple unités de protection, contrôleurs et compteurs de cellule, ou capteurs.

Les  structures  du  bus  de  communication  de  procédé  peuvent  être  organisées  de  plusieurs manières différentes, comme cela est décrit dans la CEI 61850-1. En plus de la transmission des  ensembles  de  données  de  valeurs  échantillonnées,  directement  liés  à  l'ISO/CEI 8802-3, une sélection  de  services  suivant  la  CEI 61850-8-1  est  nécessaire  pour  permettre  l'accès  au bloc de contrôle des valeurs échantillonnées (SV control block). Des références aux services appropriés  de  la  CEI 61850-8-1  sont  fournies  dans  ce SCSM .  Pour  les  dispositifs  moins complexes  (par  exemple    unités  de  fusion),  le  bloc  de  contrôle  des  valeurs  échantillonnées peut  être  préconfiguré,  auquel  cas  il  n'est  pas  nécessaire  d'implémenter  les  services  de  la CEI 61850-8-1 basés sur " MMS -Stack".

Ce document définit la mise en correspondance du modèle de classe de valeurs échantillonnées (CEI 61850-7-2) avec l'ISO/CEI 8802-3. Le présent SCSM , en conjonction avec la  CEI 61850-7  et  la  CEI 61850-6,  permet  l'interopérabilité  entre  des  dispositifs  de  différents fabricants.

La  présente  norme  ne  spécifie  pas  d'implémentations  individuelles  ou  des  produits,  elle n'impose pas non plus la mise en œuvre  d'entités et d'interfaces dans un  système informatique.  La  présente  norme  spécifie  les  fonctionnalités  des  implémentations  visibles  en externe, ainsi que les exigences de conformité relatives à ces fonctionnalités.

Guide de lecture:

- Le présent document est une spécification de mise en correspondance étendue de la CEI 61850-8-1,  destinée  à  couvrir  la  transmission  des  valeurs  échantillonnées  sur l'ISO/CEI 8802-3.
- Le  présent  document  peut  être  mieux  compris  si  le  lecteur  est  totalement  familiarisé avec les CEI 61850-7-1, CEI 61850-7-2, CEI 61850-7-3 et CEI 61850-7-4.
- Les  services ACSI définis  dans  la  CEI 61850-7-2  ne  sont  pas  explicités  dans  la présente partie de la CEI 61850.

## RÉSEAUX ET SYSTÈMES DE COMMUNICATION POUR L'AUTOMATISATION DES SYSTÈMES ÉLECTRIQUES -

## Partie 9-2: Mise en correspondance des services de communication spécifiques (SCSM) Valeurs échantillonnées sur ISO/CEI 8802-3

## 1 Domaine d'application

La  présente  partie  de  la  CEI 61850  définit  la  mise  en  correspondance  des  services  de communication spécifiques ( SCSM ) pour la transmission des valeurs échantillonnées, conformément à la spécification abstraite (abstract specification) de la CEI 61850-7-2. La mise en correspondance est celle du modèle abstrait (abstract model) sur une pile mélangée (mixed stack), utilisant l'accès direct à une liaison ISO/CEI 8802-3 pour la transmission des échantillons, en conjonction avec la CEI/TR 61850-8-1.

Chaque SCSM comporte trois parties:

- -une spécification de la pile de communication utilisée,
- -la  mise  en  correspondance  des  spécifications  abstraites  de  la  série  CEI 61850-7  sur  les éléments réels de la pile utilisée, et
- -la spécification d'implémentation de la fonctionnalité, non couverte par la pile utilisée.

## 2 Références normatives

Les  documents  de  référence  suivants  sont  indispensables  pour  l'application  du  présent document. Pour les références datées, seule l'édition citée s'applique. Pour les références non datées,  la  dernière  édition  du  document  de  référence  s'applique  (y  compris  les  éventuels amendements).

CEI 60874-10-1, Connectors for optical fibres  and  cables  -  Part  10-1:  Detail  specification  for fibre optic connector type BFOC/2,5 terminated to multimode fibre type A1 (retirée)

CEI 60874-10-2, Connectors for optical fibres  and  cables  -  Part  10-2:  Detail  specification  for fibre optic connector type BFOC/2,5 terminated to single-mode fibre type B1 (retirée)

CEI 60874-10-3, Connectors for optical fibres  and  cables  -  Part  10-3:  Detail  specification  for fibre optic adaptor type BFOC/2,5 for single and multimode fibre (retirée)

CEI/TR 61850-1, Réseaux  et  systèmes  de  communication  dans  les  postes  -  Partie  1: Introduction et vue d'ensemble (disponible en anglais seulement)

CEI/TS 61850-2, Communication networks and systems for power utility automation - Part 2: Glossary

CEI 61850-6, Communication  networks  and  systems  for  power  utility  automation  -  Part  6: Configuration  description  language  for  communication  in  electrical  substationsrelated  to  IEDs (disponible en anglais seulement)

CEI 61850-7-1, Réseaux  et  systèmes  de  communication  pour  l'automatisation  des  systèmes électriques -  Partie 7-1: Structure de communication de base -  Principes et modèles

CEI 61850-7-2, Communication networks and systems for power utility automation - Part 7-2: Basic  information  and  communication  structure  -  Abstract  communication  service  interface (ACSI) (disponible en anglais seulement)

CEI 61850-7-3, Réseaux  et  systèmes  de  communication  pour  l'automatisation  des  systèmes électriques  -  Partie  7-3:  Structure  de  communication  de  base  -  Classes  de  données communes

CEI 61850-7-4, Communication networks and systems for power utility automation - Part 7-4: Basic  communication  structure  -  Compatible  logical  node  classes  and  data  object  classes (disponible en anglais seulement)

CEI 61850-8-1, Réseaux  et  systèmes  de  communication  pour  l'automatisation  des  systèmes électriques -  Partie 8-1: mise en correspondance des services de communication specifiques (SCSM)  -  Mises  en  correspondance  pour  MMS    (ISO  9506-1  et  iISO  9506-2)  et  pour l'ISO/CEI 8802-3

CEI/TS 62351-6, Power  systems  management  and  associated  information  exchange  -  Data and  communications  security  -  Part  6:  Security  for  IEC  61850 (disponible en  anglais seulement)

CEI 62439-3:2010, Industrial  communication networks - High availability automation networks -  Part  3:  Parallel  Redundancy  Protocol  (PRP)  and  High-availability  Seamless  Redundancy (HSR) (disponible en anglais seulement) Amendement 1 1

ISO/CEI 7498-1:1994, Technologies  de  l'information  -  Interconnexion  de  systèmes  ouverts (OSI) - Modèle de référence de base: Le modèle de base

ISO/CEI 8326:1996, Technologies de l'information - Interconnexion de systèmes ouverts (OSI) - Définition du service de session

ISO/CEI 8327-1:1996, Technologies  de  l'information  -  Interconnexion  de  systèmes  ouverts (OSI) - Protocole de session en mode connexion: Spécification du protocole

ISO/CEI 8649:1996, Information technology -Open  Systems  Interconnection -Service definition for the Association Control Service Element (disponible en anglais seulement)

ISO/CEI 8650-1:1996, Technologies  de  l'information  -  Interconnexion  de  systèmes  ouverts (OSI) -Protocole en mode  connexion applicable à l'élément de service de contrôle d'association: Spécification du protocole

ISO/CEI 8802-3:2000, Information technology - Telecommunications and information exchange between  systems  -  Local  and  metropolitan  area  networks  -  Specific  requirements  -  Part  3: Carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specifications (disponible en anglais seulement)

ISO/CEI 8822:1994, Technologies de l'information - Interconnexion de systèmes ouverts (OSI) - Définition du service de présentation

ISO/CEI 8823-1:1994, Technologies  de  l'information  -  Interconnexion  de  systèmes  ouverts (OSI) - Protocole de présentation en mode connexion: Spécification du protocole

-------

1 A publier.

ISO/CEI 8824-1:2008 , Information technology -Abstract Syntax Notation One  (ASN.1): Specification of basic notation (disponible en anglais seulement)

ISO/CEI 8825-1, Technologies  de  l'information  -  Règles  de  codage  ASN.1:Spécification  des règles  de  codage  de  base  (BER),  des  règles  decodage  canoniques  (CER)  et  des  règles  de codage distinctives (DER) (disponible en anglais seulement)

ISO 9506-1:2003, Systèmes d'automatisation industrielle -Spécification de messagerie industrielle - Partie 1: Définition des services

ISO 9506-2:2003, Systèmes d'automatisation industrielle -Spécification de messagerie industrielle - Partie 2: Spécification de protocole

IEEE 754:1985, IEEE Standard for Binary Floating-Point Arithmetic

IEEE 802.1Q:1998 , IEEE Standards for Local and Metropolitan Area Networks: Virtual Bridged Local Area Networks

RFC 791, Internet Protocol; IETF,  disponible  sur  le site  Web  http://www.ietf.org [citée le 2011-03-18]

RFC 792, Internet Control Message Protocol; IETF, disponible sur le site Web http://www.ietf.org [citée le 2011-03-18]

RFC 793, Transmission Control Procedure; IETF, disponible sur le site Web http://www.ietf.org [citée le 2011-03-18]

RFC 826, Ethernet Address Resolution Protocol or Converting Network Protocol Addresses to 48.bit  Ethernet  Address  for  Transmission  on  Ethernet  Hardware;  IETF,  disponible  sur  le  site Web http://www.ietf.org [citée le 2011-03-18]

RFC 894, A  Standard  for  the  Transmission  of  IP  Datagrams  over  Ethernet  Networks;  IETF, disponible sur le site Web http://www.ietf.org [citée le 2011-03-18]

RFC 919, Broadcasting Internet Datagrams; IETF, disponible sur le site Web http://www.ietf.org [citée le 2011-03-18]

RFC 1006 ISO transport services on top of TCP: Version 3; IETF, disponible sur le site Web http://www.ietf.org [citée le 2011-03-18]

RFC 1112, Host Extensions for IP multicasting; IETF, disponible sur le site Web http://www.ietf.org [citée le 2011-03-18]

## 3 Termes et définitions

Pour les besoins du présent document, les termes et définitions donnés dans la CEI/TS 61850-2 s'appliquent.

## 4 Abréviations

ACSI

Abstract communication service interface

ASDU

Application service data unit

ASN.1

Abstract syntax notation number one

APCI

Application protocol control information

APDU

Application protocol data unit

APPID

Application identifier

AUI

Attachment unit interface

BER

ASN.1

basic encoding rules

BS

Bitstring

c

Conditional support. L'élément doit être mis en application si la condition établie existe

CFI

Canonical format identifier

CSMA/CD

Carrier sense multiple access/collision detection

DF

Data frame

DO

Data object

ECT

Electronic current transformer

EVT

Electronic voltage transformer

F/S

Functional standard

GOOSE

Generic object oriented substation event

GSSE

Generic substation status event

i

Out-of-scope: La mise en application de l'élément ne fait pas partie du domaine d'application de la présente norme

ICD

IED

configuration description

IED

Intelligent electronic device

LSDU

Link layer service data unit

m

Mandatory support. L'élément doit être mis en application

MAC

Media access control

MAU

Medium attachment unit

MMS

Manufacturing message specification (ISO 9506)

MSVCB

Multicast sampled value control block

MU

Merging unit

o

Optional support. L'exécuteur peut décider de mettre en application l'élément

PDU

Protocol data unit

PICS

Protocol implementation conformance statement

SCSM

Specific communication services mapping

r

readable

SV

Sampled value

TCI

Tag control information

TPID

Tag protocol identifier

| USVCB   | Unicast sampled value control block                                 |
|---------|---------------------------------------------------------------------|
| VID     | VLAN identifier                                                     |
| VLAN    | Virtual local area network                                          |
| VMD     | Virtual manufacturing device                                        |
| w       | Writeable                                                           |
| x       | Excluded: L'exécuteur ne doit pas mettre en application cet élément |
| XML     | Extensible markup language                                          |

## 5 Pile de communication

## 5.1 Vue d'ensemble de l'utilisation du protocole

Le modèle de référence d'interconnexion de systèmes ouverts (OSI) (ISO/CEI 7498-1) définit un modèle basé sur le concept de couches de fonctions de communication. Le modèle inclut 7 couches  et  spécifie  les  exigences  fonctionnelles  pour  chaque  couche,  afin  de  réaliser  un système de communication robuste. Le modèle ne spécifie pas les protocoles à utiliser pour réaliser  la  fonctionnalité;  il  ne  restreint  pas  non  plus  la  solution  à  un  ensemble  unique  de protocoles.

Figure 1 - Modèle de référence OSI et profils

<!-- image -->

Les  profils  ISO  application  ("A-Profile")  et  transport  ("T-Profile")  (voir  Figure 1)  décrivent  les divers  profils  de  pile.  Un  "A-Profile"  ISO  est  l'ensemble  des  spécifications  et  des  accords concernant les trois (3) couches supérieures du modèle de référence OSI ISO (par exemple, les  couches  "application",  "presentation"  et  "session").  Un  "T-Profile"  ISO  est  l'ensemble  des spécifications  et  des  accords  concernant  les  quatre  (4)  couches  inférieures  du  modèle  de référence OSI ISO (par exemple, les couches "transport", "network", "datalink" et "pysical").

Deux  combinaisons  des  "A-Profiles"  et  des  "T-Profiles"  sont  définies  afin  de  permettre  la transmission des valeurs échantillonnées comprenant l'accès au bloc de contrôle des valeurs échantillonnées ( SV control block) associé, comme cela est spécifié par la CEI 61850-7-2. Les deux combinaisons distinctes sont utilisées pour:

- les services client/serveur basés sur la MMS (spécification de messagerie industrielle), conformément à la CEI 61850-8-1;
- les services SV basés sur la couche "datalink" (liaison de données).

## 5.2 Services client/serveur et profils de communication

## 5.2.1 Services client/serveur

Ce profil de communication client/serveur doit être utilisé, en plus du profil de communication SV ,  conformément  à  5.3,  si  un  accès  au  bloc  de  contrôle  des  valeurs  échantillonnées,  par l'intermédiaire  du  client,  est  exigé.  Ce  profil  doit  être  utilisé  pour  toute  implémentation prétendant être en conformité avec la présente norme et déclarant supporter l'un des services de la CEI 61850-7-2 suivants, donnés par le Tableau 1.

Tableau 1 - Service exigeant un profil de communication client/serveur

| Modèle CEI 61850-7-2   | Service CEI 61850-7-2     |
|------------------------|---------------------------|
| Server                 | GetServerDirectory        |
| Association            | Associate                 |
|                        | Abort                     |
|                        | Release                   |
| Logical device         | GetLogicalDeviceDirectory |
| Logical node           | GetLogicalNodeDirectory   |
|                        | Get AllD ataValues        |
| Data                   | GetDataValues             |
|                        | SetDataValues             |
|                        | GetDataDirectory          |
|                        | GetDataDefinition         |
| Data set               | GetDataSetValues          |
|                        | SetDataSetValues          |
|                        | CreateDataSet             |
|                        | DeleteDataSet             |
|                        | GetDataSetDirectory       |
| SV class model         | Get MSVCB Values          |
|                        | Set MSVCB Values          |
|                        | Get USVCB Values          |
|                        | Set USVCB Values          |

## 5.2.2 "A-Profile"

Le Tableau 2 présente les services et les protocoles client/serveur du "A-Profile".

Tableau 2 - Services et protocoles relatifs au profil de communication client/serveur du "A-Profile"

|                      | Spécification                       | Spécification            | Spécification              | m/o 2   |
|----------------------|-------------------------------------|--------------------------|----------------------------|---------|
| Couche du modèle OSI | Nom                                 | Spécification du service | Spécification du protocole |         |
| Application          | Manufacturing message specification | ISO 9506-1:2003          | ISO 9506-2:2003            | m       |

-------

2 Anglais: m/o (mandatory/optional)   français: obligatoire/optionnel

|                      | Spécification                       | Spécification            | Spécification              | m/o 2   |
|----------------------|-------------------------------------|--------------------------|----------------------------|---------|
| Couche du modèle OSI | Nom                                 | Spécification du service | Spécification du protocole |         |
|                      | Association control service element | ISO/IEC 8649:1996        | ISO/IEC 8650-1:1996        | m       |
| Presentation         | Connection oriented presentation    | ISO/IEC 8822:1994        | ISO/IEC 8823-1:1994        | m       |
|                      | Abstract syntax                     | ISO/IEC 8824-1:2008      | ISO/IEC 8825-1             | m       |
| Session              | Connection oriented session         | ISO/IEC 8326:1996        | ISO/IEC 8327-1:1996        | m       |

Il  n'existe  qu'un  "T-Profile"  (TCP/IP)  pouvant  être  utilisé  par  le  profil  client/serveur  du  "AProfile".

## 5.2.3 "T-Profile" TCP/IP

Le Tableau 3 présente les services et les protocoles client/serveur du "T-Profile" TCP/IP.

Tableau 3 - Services et protocoles relatifs au "T-Profile" TCP/IP

| Couche du modèle OSI   | Spécification                                                                      | Spécification                                    | Spécification                                    |     |
|------------------------|------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|-----|
| Couche du modèle OSI   | Nom                                                                                | Spécification du service                         | Spécification du protocole                       | m/o |
| Transport              | ISO transport on top of TCP                                                        | RFC 1006                                         |                                                  | m   |
| Transport              | Internet control message protocol (ICMP)                                           | RFC 792                                          |                                                  | m   |
| Transport              | Transmission control protocol (TCP)                                                | RFC 793                                          |                                                  | m   |
| Network                | Internet protocol                                                                  | RFC 791                                          |                                                  |     |
| Network                | Converting network protocol address                                                | RFC 826 (Address resolution protocol: ARP)       | RFC 826 (Address resolution protocol: ARP)       | m   |
| Network                | Broadcasting internet datagrams                                                    | RFC 919                                          |                                                  | m   |
| Network                | Host extensions for IP multicasting                                                | RFC 1112                                         |                                                  | m   |
| Link Redundancy        | Parallel redundancy protocol and high availability seamless ring                   | CEI 62439-3, Amendment 1                         | CEI 62439-3, Amendment 1                         | o   |
| DataLink               | Standard for the transmission of IP datagrams over Ethernet networks               | RFC 894                                          |                                                  | m   |
| DataLink               | Carrier sense multiple access with collision detection ( CSMA/CD )                 | ISO/IEC 8802-3:2000                              | ISO/IEC 8802-3:2000                              | m   |
| Physical               | Fibre optic transmission system 100Base-FX                                         | ISO/IEC 8802-3:2000                              | ISO/IEC 8802-3:2000                              | c1  |
| Physical               | Basic optical fibre connector NOTE This is the specification for the ST connector. | CEI 60874-10-1, CEI 60874-10-2 et CEI 60874-10-3 | CEI 60874-10-1, CEI 60874-10-2 et CEI 60874-10-3 | c1  |

## 5.3 Service SV et profil de communication

## 5.3.1 Présentation générale de la mise en correspondance SV

Ce profil  de  communication SV doit  être  utilisé  pour  toute  implémentation  prétendant  être  en conformité avec la présente norme et déclarant supporter l'un des services de la CEI 61850-7-2 suivants, donnés par le Tableau 4.

Tableau 4 - Services exigeant un profil de communication SV

| Modèle                              | Service CEI 61850-7-2   |
|-------------------------------------|-------------------------|
| Multicast sampled value class model | Multicast SV message    |
| Unicast sampled value class model   | Unicast SV message      |

## 5.3.2 "A-Profile"

Le Tableau 5 présente les services et les protocoles SV du "A-Profile".

Tableau 5 - Services et protocoles relatifs au profil de communication SV du "A-Profile"

| Couche du modèle OSI   | Spécification   | Spécification            | Spécification              | m/o   |
|------------------------|-----------------|--------------------------|----------------------------|-------|
| Couche du modèle OSI   | Nom             | Spécification du service | Spécification du protocole |       |
| Application            | SV service      |                          |                            | m     |
| Presentation           | Abstract syntax | ISO/IEC 8824-1:2008      | ISO/IEC 8825-1             | m     |
| Session                |                 |                          |                            |       |

Couche "presentation": voir les définitions supplémentaires en 8.5.

Couche "application": voir les définitions supplémentaires en 8.5.

## 5.3.3 "T-Profile"

Le "T-Profile" pour les services SV est donné au Tableau 6.

Tableau 6 - "T-Profile" SV

|                                                                      | Spécification                                                                           | Spécification                                                        | Spécification                                                        |                                                                      |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Couche du modèle OSI                                                 | Nom                                                                                     | Spécification du service                                             | Spécification du protocole                                           | m/o                                                                  |
| Transport                                                            |                                                                                         |                                                                      |                                                                      |                                                                      |
| Network                                                              |                                                                                         |                                                                      |                                                                      |                                                                      |
| Link Redundancy                                                      | Parallel redundancy protocol and high availability seamless ring                        | CEI 62439-3, Amendement 1                                            | CEI 62439-3, Amendement 1                                            | o                                                                    |
| DataLink                                                             | Priority tagging/ VLAN                                                                  | IEEE 802.1Q                                                          | IEEE 802.1Q                                                          | m                                                                    |
| DataLink                                                             | Carrier sense multiple access with collision detection ( CSMA/CD )                      | ISO/IEC 8802-3:2000                                                  | ISO/IEC 8802-3:2000                                                  | m                                                                    |
| Physical                                                             | Fibre optic transmission system 100Base-FX                                              | ISO/IEC 8802-3:2000                                                  | ISO/IEC 8802-3:2000                                                  | c1                                                                   |
| Physical                                                             | Basic optical fibre connector NOTE Il s'agit de la spécification pour le connecteur ST. | CEI 60874-10-1, CEI 60874-10-2 et CEI 60874-10-3                     | CEI 60874-10-1, CEI 60874-10-2 et CEI 60874-10-3                     | c1                                                                   |
| c1 - Recommandé, mais une technologie future pourrait être utilisée. | c1 - Recommandé, mais une technologie future pourrait être utilisée.                    | c1 - Recommandé, mais une technologie future pourrait être utilisée. | c1 - Recommandé, mais une technologie future pourrait être utilisée. | c1 - Recommandé, mais une technologie future pourrait être utilisée. |

## 5.3.3.1 Couche physique: Spécifications relatives à medium attachment unit ( MAU )

Le  système  de  transmission  par  fibre  optique  100Base-FX,  conforme  à  l'ISO/CEI 8802-3,  est recommandé, comme indiqué ci-dessus, en raison des exigences concernant l'environnement électromagnétique.

## 5.3.3.2 Couche liaison: adresses Ethernet

L'adresse de la destination ISO/CEI 8802-3 multidiffusion (multicast)/envoi individuel (unicast) doit  être  configurée  pour  la  transmission  des  valeurs  échantillonnées.  Une  seule  adresse source  ISO/CEI 8802-3  doit  être  utilisée.  Des  recommandations  d'affectations  de  plages d'adresses multidiffusion sont données à l'Annexe B.

## 5.3.3.3 Couche liaison: "Priority tagging/virtual LAN"

"Priority  tagging",  conformément  à  l'IEEE 802.1Q,  est  utilisé  pour  séparer  le  trafic  sur  le  bus ayant  une  criticité  temporelle  et  une  haute  priorité  pour  les  applications  relatives  à  la protection, de la charge du bus ayant une faible priorité.

Voir la Figure 2 pour la structure de l'entête de l'étiquette.

Figure 2 - Structure de l'entête de l'étiquette

<!-- image -->

Champ TPID (tag  protocol  identifier):  Indique  le  type  Ethernet  assigné  pour  les  trames encodées Ethernet 802.1Q. Cette valeur doit être 0x8100.

Champs TCI (tag control information): Priorité utilisateur BS3; la valeur de la priorité utilisateur doit être établie par la configuration des valeurs échantillonnées séparées de la charge du bus ayant une faible priorité. Si la priorité n'est pas configurée, les valeurs par défaut du Tableau 7 doivent alors être utilisées.

CFI (canonical format indicator): BS 1 [0]; Une valeur d'indicateur à bit unique. Pour la présente norme, la valeur du bit CFI doit être remise à l'état initial (valeur = 0).

NOTE  1 Si  activé  (valeur  =  1),  un  champ  "embedded  resource  identification  field"  (E-RIF)  suit  le  champ Length/Type dans la trame étiquetée ISO/CEI 8802-3.

VID:  Le  support  "virtual  LAN"  est  facultatif.  Si  ce  mécanisme  était  utilisé,  le  " VLAN identifier" ( VID ) doit être positionné par configuration; s'il ne l'était pas, il doit être mis à zéro (0).

NOTE 2 Comme l'IEEE 802.1Q autorise l'implémentation avec un ensemble restreint de priorités, il convient que les  trames de priorités les plus élevées aient une priorité de 4 à 7 et que celles de priorités inférieures aient une priorité de 1 à 3. La valeur 1 est la priorité des trames non étiquetées, ainsi il convient que la valeur 0 soit évitée, car elle peut entraîner un retard imprévisible en raison du trafic normal.

De plus, puisque les valeurs échantillonnées ont besoin d'avoir potentiellement leur propre allocation de largeur de bande, leur VID configuré sera différent de GOOSE et de GSSE .

Les valeurs de priorité et de VID par défaut doivent être telles que définies par le Tableau 7.

Tableau 7 - Valeurs par défaut des ID "Virtual LAN" et des priorités

| Service        |   VID par défaut |   Priorité par défaut |
|----------------|------------------|-----------------------|
| Sampled Values |                0 |                     4 |

La structure générale de trame ISO/CEI 8802-3 relative aux valeurs échantillonnées peut être consultée à l'Annexe A.

## 5.3.3.4 Couche liaison: Ethertype et autres informations d'entête

## 5.3.3.4.1 Ethertype

Les Ethertypes, basés sur la sous-couche MAC de l'ISO/CEI 8802-3, sont agréés par l'autorité d'enregistrement  de  l'IEEE.  La  gestion  des GSSE ,  les GOOSE et  les  valeurs  échantillonnées doivent  être  directement  affectées  et  mises  en  correspondance  avec  le(s)  Ethertype(s) réservé(s) et avec l'unité de données du protocole ( PDU ) de l'Ethertype. Les valeurs assignées sont données par le Tableau 8.

Tableau 8 - Valeurs Ethertype assignées

| Utilisation                  | Valeur Ethertype (hexadécimal)   | Type d' APPID   |
|------------------------------|----------------------------------|-----------------|
| CEI 61850-8-1 GOOSE          | 88-B8                            | 0 0             |
| CEI 61850-8-1 GSE Management | 88-B9                            | 0 0             |
| CEI 61850-9-2 Sampled Values | 88-BA                            | 0 1             |

Les octets PDU et APDU de l'Ethertype doivent être tels que définis par l'Annexe A.

## 5.3.3.4.2 APPID

Application  identifier  (l'identificateur  d'application).  L' APPID est  utilisé  pour  sélectionner  les trames  de  l'ISO/CEI 8802-3  contenant  les  messages  des  valeurs  échantillonnées  et  pour différencier l'association à l'application.

La valeur de l' APPID est  la  combinaison du type d' APPID ,  défini  comme les deux bits les plus significatifs de la valeur (comme défini par le Tableau 8), et de l'identification réelle ( ID ) .

La plage de valeurs réservée pour les valeurs échantillonnées est 0x4000 à 0x7FFF. Si aucun APPID n'est configuré, la valeur par défaut doit être 0x4000. La valeur par défaut est réservée à l'indication de la configuration manquante. Il est vivement recommandé d'avoir un APPID de SV orienté  source  unique  dans  un  système,  afin  d'activer  un  filtre  sur  la  couche  liaison.  Il convient que la configuration de l' APPID soit imposée par le système de configuration.

## 5.3.3.4.3 Length

Nombre d'octets comprenant l'entête de l'unité de données de protocole ( PDU ) de l'Ethertype, commençant à l' APPID (identificateur d'application) et la longueur de l' APDU (unité de données de protocole d'application ). Par conséquent, la valeur de "Length" doit être 8 + m, où m est la longueur  de  l' APDU et  inférieure  à  1493.  Les  trames  dont  le  champ  est  d'une  longueur incohérente ou invalide doivent être rejetées.

## 5.3.3.4.4 Reserved 1

La structure de "Reserved 1" est définie par la Figure 3.

Figure 3 - "Reserved 1"

<!-- image -->

- S:  Simulate.  Lorsque  cet  indicateur  est  activé,  une  trame  SampledValue  a  été  émise  par  un émetteur  situé  au  sein  d'un  dispositif  d'essai  et  non  par  l'émetteur  spécifié  par  le  fichier  de configuration du dispositif.
- R: Reserved. Les trois bits sont réservés pour une application normalisée future et doivent être mis à 0 par défaut.

Reserved security: Voir Reserved 2 ci-dessous.

## 5.3.3.4.5 Reserved 2

Le champ Reserved 2 et 'reserved security' du champ Reserved 1 forment un mot de 28 bits défini  par  la  norme  de  sécurité  CEI/TS 62351-6.  Il  doit  être  utilisé  comme  cela  est  indiqué lorsque la trame SampledValue avec sécurité est transmise, sinon il doit être mis à 0.

## 5.4 Restrictions

Cette  mise  en  correspondance  est  limitée  à  celle  du  modèle ACSI pour  la  transmission  des valeurs échantillonnées. Le modèle s'applique aux ensembles de données. Pour bénéficier de tous les avantages de la CEI 61850, il est nécessaire que des modèles ACSI supplémentaires soient  supportés,  conformément  à  la  CEI 61850-8-1.  À  titre  d'exemple,  pour  permettre  la transmission de la mémoire tampon des valeurs échantillonnées, l'attribut du bloc de contrôle associé  "SvEna"  doit  être  écrit.  Cependant,  si  le  client  veut  lire  une  liste  d'ensembles  de données disponibles ou le contenu d'un ensemble de données, il est nécessaire que d'autres modèles  soient  supportés  (par  exemple    dispositif  logique,  nœud  logique  ou  ensemble  de données).

Les ensembles de données relatifs aux valeurs échantillonnées seront spécifiés en utilisant le langage XML au niveau ingénierie, conformément  à  la CEI 61850-6, pour en assurer l'interopérabilité.

Pour  la  transmission  des  ensembles  de  données  de  valeurs  échantillonnées,  les  règles  de codage de base ASN.1 ( ASN.1, basic encoding rules BER ) seront utilisées en conjonction avec la  notation  des  marquages  harmonisée  avec  la  grammaire  de  la MMS utilisée  dans  la CEI 61850-8-1.

## 6 Mise en correspondance des attributs de données CEI 61850-7-2 et CEI 61850-7-3

La  mise  en  correspondance  des  attributs  de  données  et  de  ceux  communs  à  la MMS sont spécifiés dans la CEI 61850-8-1.

Pour la transmission des valeurs échantillonnées, l' ASN.1 , les règles de codage de base (basic encoding  rules  BER )  et  les  classes  de  données  communes  définies  par  la  CEI 61850-7-3 s'appliquent.

IEC   1788/11

## 7 Mise en correspondance des classes et des services CEI 61850-7-2

## 7.1 Classes des ensembles de données de valeurs échantillonnées ( SV data sets)

Si une association client/serveur basée sur la MMS est utilisée en plus de la transmission des ensembles  de  données  des SV ,  les  définitions  de  la  CEI 61850-8-1  s'appliquent  pour  les classes suivantes:

- -modèle de classe de serveur ("server");
- -modèle d'association ("association");
- -modèle d'équipement logique ("logical device");
- -modèle de nœud logique ("logical node");
- -modèle de classe de donnée ("data");
- -modèle de classe d'ensemble de données ("data set").

## 7.2 Définition des ensembles de données de valeurs échantillonnées ( SV data sets)

Pour la transmission des valeurs échantillonnées, les ensembles de données sont définis dans le nœud  logique " LLN0 ". Toute spécification des ensembles de données de valeurs échantillonnées fait partie de la description de configuration de l' IED ( ICD ).

NOTE Il  est  supposé  que  les  ensembles  de  données  utilisés  pour  la  transmission  des  valeurs  échantillonnées peuvent inclure des objets de données à partir de plusieurs nœuds logiques et sont donc affectés dans LLN0 .

## 8 Mise en correspondance du modèle pour la transmission des valeurs échantillonnées

## 8.1 Présentation générale

Pour  assurer  l'interopérabilité,  les  ensembles  de  données  pour  les  valeurs  échantillonnées sont spécifiés en XML , conformément à la définition de la CEI 61850-6.

Le modèle de classe des valeurs échantillonnées fournit un compte rendu des ensembles de données  de  valeurs  échantillonnées,  d'une  manière  organisée  et  avec  contrôle  temporel,  de sorte que le transfert est très rapide et le temps de transfert est maintenu constant. Le bloc de contrôle des valeurs échantillonnées pour envoi individuel (unicast) et multidiffusion (multicast) définit les caractéristiques de transmission de l'ensemble de données auquel elles se réfèrent. Une description détaillée est donnée dans la CEI 61850-7-2.

## 8.2 Mise en correspondance de classes et de services du bloc de contrôle des valeurs échantillonnées multidiffusion

## 8.2.1 Définition du bloc de contrôle des valeurs échantillonnées multidiffusion

Le bloc de contrôle des valeurs échantillonnées, tel que défini dans la CEI 61850-7-2, doit être prédéfini  par  configuration  ou  doit  être  affecté  et  mis  en  correspondance  avec  un  bloc  de contrôle de valeurs échantillonnées multidiffusion MMS ( MMS multicast sampled value control block  MSVCB ),  comme  cela  est  défini  par  le  Tableau 9.  Tous  les  composants  du MSVCB doivent être de contrainte fonctionnelle 'MS'.

Tableau 9 - Définition MMS TypeDescription pour structure MSVCB MMS

| Nom du composant MMS   | Nom du composant MMS   | TypeDescription MMS   | r/w   | m/o   | Condi- tion   | Commentaires                                                                                                                                                                                           |
|------------------------|------------------------|-----------------------|-------|-------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MsvCBNam               | MsvCBNam               | Identifier            | r     | m     |               | Identificateur MMS de la structure du MsvCBName dans l'objet MMS nommé: LLN0$MV, par exemple, LLN0$MS$<MsvCBNam>                                                                                       |
| MsvCBRef               | MsvCBRef               | Visible-string        | r     | m     |               | La valeur de ce composant doit contenir la référence CEI du MsvCB. Par exemple, <MMSDomain>/LLN0$MS$<MsvCBNam>                                                                                         |
| SvEna                  | SvEna                  | Boolean               | r/w   | m     |               | TRUE (VRAI) = la transmission de la mémoire tampon de la valeur échantillonnée est activée. FALSE (FAUX) = la transmission de la mémoire tampon de la valeur échantillonnée est désactivée.            |
| MsvID                  | MsvID                  | Visible-string        | r     | m     |               | Identification unique à l'échelle du système.                                                                                                                                                          |
| DatSet                 | DatSet                 | Visible-string        | r     | m     |               | La valeur de ce composant doit contenir la référence CEI du DataSet exprimée par le MsvCB. Cette ObjectReference doit être limitée à un VMD ou à un Domain de NamedVariableLists.                      |
| ConfRev                | ConfRev                | Integer               | r     | m     |               | Compte les changements de configuration concernant le MSVCB.                                                                                                                                           |
| SmpRate                | SmpRate                | Integer               | r     | m     |               | Quantité d'échantillons (défaut par période nominale, voir SmpMod).                                                                                                                                    |
| OptFlds                | OptFlds                | BitString             |       |       |               |                                                                                                                                                                                                        |
|                        | refresh-time           | Boolean               | r     | m     |               | TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'RefrTm'. FALSE (FAUX) = l'attribut 'RefrTm' n'est pas disponible dans la mémoire tampon SV.                                                    |
|                        | sample- synchronised   | Boolean               | r     | m     |               | La valeur sera ignorée. Conservée pour assurer la rétrocompatibilité avec l'édition 1.0 de la CEI 61850-9-2.                                                                                           |
|                        | sample-rate            | Boolean               | r     | m     |               | TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'SmpRate'. FALSE (FAUX) = l'attribut 'SmpRate' n'est pas disponible dans la mémoire tampon SV.                                                  |
|                        | data-set               | Boolean               | r     | m     |               | TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'DatSet'. FALSE (FAUX) = l'attribut 'DatSet' n'est pas disponible dans la mémoire tampon SV.                                                    |
|                        | security               | Boolean               | r     | M     |               | Attribut spécifique de mise en correspondance. TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'Security'. FALSE (FAUX) = l'attribut 'Security' n'est pas disponible dans la mémoire tampon SV. |
| SmpMod                 | SmpMod                 | Enumerated            | r     | O     |               | SmpMod spécifie 0 = échantillons par période nominale (DÉFAUT) 1 = échantillons par seconde 2 = secondes par échantillon Si non disponible (rétrocompatibilité), la valeur par défaut est 0.           |
| DstAddress             | DstAddress             | Voir Tableau 10       |       | M     |               | Attribut spécifique de mise en correspondance.                                                                                                                                                         |
| noASDU                 | noASDU                 | Integer               | r     | M     |               | Attribut spécifique de mise en correspondance. Nombre d'ASDU concaténées dans une APDU.                                                                                                                |

Tableau 10 - Structure DstAddress

| Nom du composant MMS   | TypeDescription MMS   | r/w   | m/o   | Condi- tion   | Commentaires                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------|-----------------------|-------|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Addr                   | OCTET-STRING          | r     | M     |               | La longueur est de 6 octets et contient la valeur de l'adresse du media access control (MAC) de destination à laquelle le message SV doit être envoyé. Si DstAddress fait partie d'un MSVCB, l'adresse doit être une adresse Ethernet dont le bit multidiffusion est fixé à TRUE (VRAI). Afin de faciliter le filtrage du trafic sur le réseau, il est recommandé d'utiliser différentes adresses Ethernet pour chaque DstAddress. Si DstAddress fait partie d'un USVCB, l'adresse doit être l'adresse Ethernet de l'abonné SV. Voir l'Annexe B pour des recommandations concernant l'adressage multidiffusion. |
| PRIORITY               | Unsigned8             | r     | M     |               | La plage des valeurs doit être limitée entre 0 et 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VID                    | Unsigned16            | r/w   | M     |               | La plage des valeurs doit être limitée entre 0 et 4095.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| APPID                  | Unsigned16            | r     | M     |               | Comme cela est défini en 5.3.3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## 8.2.2 Services MSV

Voir Tableau 11.

Tableau 11 - Mise en correspondance des services des valeurs échantillonnées multidiffusion

| Services de classe MSVCB   | Service                                                                                                                                                     |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SendM SV Message           | La transmission des messages MSV est mise en correspondance directement sur la couche liaison de données (DataLink), comme cela est défini en 8.4 et en 8.5 |
| Get MSVCB Value            | Mis en correspondance au service lecture MMS.                                                                                                               |
| Set MSVCB Value            | Mis en correspondance au service écriture MMS.                                                                                                              |

## 8.3 Mise en correspondance de classes et de services du bloc de contrôle des valeurs échantillonnées envoi individuel

## 8.3.1 Définition du bloc de contrôle des valeurs échantillonnées envoi individuel

Le bloc de contrôle des valeurs échantillonnées, tel que défini dans la CEI 61850-7-2, doit être prédéfini  par  configuration  ou  doit  être  affecté  et  mis  en  correspondance  avec  un  bloc  de contrôle de valeurs échantillonnées envoi individuel MMS ( MMS unicast sampled value control block  USVCB ),  comme  cela  est  défini  par  le  Tableau 12.  Tous  les  composants  du USVCB doivent être de contrainte fonctionnelle 'US'.

Tableau 12 - Définition MMS TypeDescription pour structure USVCB MMS

| Nom du composant MMS   | Nom du composant MMS   | TypeDescription MMS   | r/w   | m/o   | Condi- tion   | Commentaires                                                                                                                                                                                           |
|------------------------|------------------------|-----------------------|-------|-------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsvCBNam               | UsvCBNam               | Identifier            | r     | M     |               | Identificateur MMS de la structure du UsvCBName dans l'objet MMS nommé: LLN0$MV, par exemple, LLN0$US$<UsvCBNam>                                                                                       |
| UsvCB Ref              | UsvCB Ref              | Visible-string        | r     | M     |               | La valeur de ce composant doit contenir la référence CEI du UsvCB. Par exemple, <MMSDomain>/LLN0$US$<UsvCBNam>                                                                                         |
| SvEna                  | SvEna                  | Boolean               | r/w   | M     |               | TRUE (VRAI) = la transmission de la mémoire tampon de la valeur échantillonnée est activée. FALSE (FAUX) = la transmission de la mémoire tampon de la valeur échantillonnée est désactivée.            |
| Resv                   | Resv                   | Boolean               | r/w   | M     |               | TRUE (VRAI) = USVCB est exclusivement réservé au client qui a fixé cette valeur à TRUE (VRAI).                                                                                                         |
| UsvID                  | UsvID                  | Visible-string        | r     | M     |               | Identification unique à l'échelle du système.                                                                                                                                                          |
| DatSet                 | DatSet                 | Visible-string        | r     | M     |               | La valeur de ce composant doit contenir la référence CEI du DataSet exprimée par le UsvCB. Cette ObjectReference doit être limitée à un VMD ou à un Domain de NamedVariableLists.                      |
| ConfRev                | ConfRev                | Integer               | r     | M     |               | Compte les changements de configuration concernant le USVCB.                                                                                                                                           |
| SmpRate                | SmpRate                | Integer               | r     | M     |               | Quantité d'échantillons (défaut par période nominale, voir SmpMod).                                                                                                                                    |
| OptFlds                | OptFlds                | BitString             |       |       |               |                                                                                                                                                                                                        |
|                        | refresh-time           | Boolean               | r     | M     |               | TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'RefrTm'. FALSE (FAUX) = l'attribut 'RefrTm' n'est pas disponible dans la mémoire tampon SV.                                                    |
|                        | sample- synchronised   | Boolean               | r     | M     |               | La valeur sera ignorée. Conservée pour assurer la rétrocompatibilité avec l'édition 1.0 de la CEI 61850-9-2.                                                                                           |
|                        | sample-rate            | Boolean               | r     | M     |               | TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'SmpRate'. FALSE (FAUX) = l'attribut 'SmpRate' n'est pas disponible dans la mémoire tampon SV.                                                  |
|                        | data-set               | Boolean               | r     | M     |               | TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'DatSet'. FALSE (FAUX) = l'attribut 'DatSet' n'est pas disponible dans la mémoire tampon SV.                                                    |
|                        | security               | Boolean               | r     | M     |               | Attribut spécifique de mise en correspondance. TRUE (VRAI) = la mémoire tampon SV contient l'attribut 'Security'. FALSE (FAUX) = l'attribut 'Security' n'est pas disponible dans la mémoire tampon SV. |
| SmpMod                 | SmpMod                 | Enumerated            | r     | O     |               | SmpMod spécifie 0 = échantillons par période nominale (DÉFAUT) 1 = échantillons par seconde 2 = secondes par échantillon Si non disponible (rétrocompatibilité), la valeur par défaut est 0.           |
| DstAddress             | DstAddress             | Voir Tableau 10       |       | M     |               | Attribut spécifique de mise en correspondance.                                                                                                                                                         |

| Nom du composant MMS   | TypeDescription MMS   | r/w   | m/o   | Condi- tion   | Commentaires                                                                            |
|------------------------|-----------------------|-------|-------|---------------|-----------------------------------------------------------------------------------------|
| noASDU                 | Integer               | r     | M     |               | Attribut spécifique de mise en correspondance. Nombre d'ASDU concaténées dans une APDU. |

## 8.3.2 Services USV

Voir Tableau 13.

Tableau 13 - Mise en correspondance des services des valeurs échantillonnées envoi individuel

| Services de classe USVCB   | Service                                                                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Send USV Message           | La transmission des messages USV est affectée directement sur la couche liaison de données (DataLink), comme cela est défini en 8.4 et en 8.5 |
| Get USVCB Value            | Affecté au service lecture MMS.                                                                                                               |
| Set USVCB Value            | Affecté au service écriture MMS.                                                                                                              |

## 8.4 Mise en correspondance de la mise à jour de la mémoire tampon des valeurs échantillonnées

Comme spécifié par la CEI 61850-7-2, le système de communication a la charge de mettre à jour la mémoire tampon de l'abonné.

La mise à jour est directement affectée et mise en correspondance avec un Ethertype réservé pour les applications CEI 61850 basées sur l'ISO/CEI 8802-3 -sous-couche MAC .

La pile de communication utilisée ne fournit pas les fonctionnalités suivantes.

- -Lancement  et vérification de la mise à jour de la mémoire  tampon  des  valeurs échantillonnées.  Concaténation  optionnelle  de  la  mise  à  jour  de  plusieurs  mémoires tampon dans la même trame de couche de liaison. C'est une fonctionnalité de la couche application.
- -Encodage  des  types de données  abstraits. C'est une fonctionnalité de la couche présentation.
- -Concaténation  de  la  mise  à  jour  de  plusieurs  mémoires  tampon  de  transmission  dans  la même trame de couche de liaison, du fait que la fonctionnalité de la couche transport n'est pas  supportée.  Réciproquement,  segmenter  la  mise  à  jour  d'une  mémoire  tampon  en plusieurs  trames  de  couche  de  liaison  n'est  pas  considéré,  car  la  longueur  maximale  de trame des protocoles de couche de liaison est suffisante.
- -Transformation de l'adresse logique de l'abonné en une adresse MAC physique.

Cependant, les définitions supplémentaires de 8.5 s'appliquent.

## 8.5 Définitions supplémentaires pour la transmission des valeurs échantillonnées

## 8.5.1 Fonctionnalité de la couche application

La mise en correspondance donne la possibilité de concaténer plusieurs ASDU en une APDU , avant  que  cette  dernière  soit  envoyée  dans  la  mémoire  tampon  de  transmission.  Le  nombre d' ASDU qui  seront concaténés dans une APDU est  configurable et en rapport avec la cadence d'échantillonnage.  La  concaténation  des ASDU n'est  pas  dynamiquement  modifiable,  afin  de

réduire la complexité de l'implémentation. Lorsque plusieurs ASDU sont concaténés dans une même trame, l' ASDU ayant les échantillons les plus anciens est le premier de la trame.

De plus amples détails sont donnés à la Figure 4.

<!-- image -->

IEC   1789/11

Figure 4 - Concaténation de plusieurs ASDU en une trame

La  grammaire ASN.1 ,  en  relation  avec  les  règles  de  codage  de  base  (basic  encoding  rules  BER),  est  utilisée  pour  encoder  les  messages  des  valeurs  échantillonnées  en  vue  de  la transmission sur l'ISO/CEI 8802-3.

## 8.5.2 Fonctionnalité de la couche présentation

Pour  la  transmission,  la  mémoire  tampon  des  valeurs  échantillonnées  est  encodée  comme spécifié par le Tableau 14.

## Tableau 14 - Encodage relatif à la transmission de la mémoire tampon des valeurs échantillonnées

IEC61850 DEFINITIONS::= BEGIN

IMPORTS Data FROM ISO-IEC-9506-2CEI 61850-9-2 Specific Protocol::= CHOICE {    savPdu [APPLICATION 0] IMPLICIT SavPdu,

| Format de mémoire tampon abstrait (abstract buffer format) selon la CEI 61850-7-2   | Format de mémoire tampon abstrait (abstract buffer format) selon la CEI 61850-7-2   | Codage en CEI 61850-9-2                                   | Commentaires                                                                                                      |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Nom d'attribut                                                                      | Type d'attribut                                                                     | Règles de codage de base ASN.1 (BER) SavPdu::= SEQUENCE { |                                                                                                                   |
|                                                                                     |                                                                                     | noASDU [0] IMPLICIT INTEGER (1..65535),                   | Attribut spécifique de mise en correspondance. Nombre d'ASDU qui seront concaténées dans une APDU.                |
|                                                                                     |                                                                                     | security [1] ANY OPTIONAL,                                | Attribut spécifique de mise en correspondance. Réservé pour future définition (par exemple, signature numérique). |
|                                                                                     |                                                                                     | asdu [2] IMPLICIT SEQUENCE OF ASDU }                      | Nombre 1 à n d'ASDU comme spécifié précédemment.                                                                  |
|                                                                                     |                                                                                     | ASDU::= SEQUENCE {                                        |                                                                                                                   |

| Format de mémoire tampon abstrait (abstract buffer format) selon la   | Format de mémoire tampon abstrait (abstract buffer format) selon la   | Codage en CEI 61850-9-2                                   | Commentaires                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nom d'attribut                                                        | Type d'attribut                                                       | Règles de codage de base ASN.1 (BER) SavPdu::= SEQUENCE { |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MsvID or UsvID                                                        | VISIBLE STRING                                                        | svID [0] IMPLICIT VisibleString,                          | Il convient que cela soit une identification unique à l'échelle du système.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DatSet                                                                | ObjectReference                                                       | datset [1] IMPLICIT VisibleString OPTIONAL,               | Valeur issue du MSVCB ou du USVCB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SmpCnt                                                                | INT16U                                                                | smpCnt [2] IMPLICIT OCTET STRING (SIZE(2)),               | Sera incrémenté chaque fois qu'une nouvelle valeur d'échantillonnage sera prélevée. Le compteur doit être mis à zéro si l'échantillonnage est synchronisé par le signal d'horloge et le signal de synchronisation se produit. Lorsque des impulsions de synchro sont utilisées pour synchroniser des unités de fusion, le compteur doit être mis à zéro avec chaque impulsion de synchro. La valeur 0 doit être donnée à l'ensemble de données dans le cas où l'échantillonnage du courant primaire coïncide avec l'impulsion de synchro. OCTET STRING est interprété comme INT16U, tel que défini par le |
| ConfRev                                                               | INT32U                                                                | confRev [3] IMPLICIT OCTET STRING (SIZE(4)),              | Valeur issue du MSVCB ou du USVCB. OCTET STRING est interprété comme INT32U, tel que défini par le Tableau 15.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RefrTm                                                                | TimeStamp                                                             | refrTm [4] IMPLICIT UtcTime OPTIONAL,                     | RefrTm contient le temps de rafraîchissement de la mémoire tampon SV.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SmpSynch                                                              | INT8U                                                                 | smpSynch [5] IMPLICIT OCTET STRING (SIZE(1)),             | 0 = les SV ne sont pas synchronisées par un signal d'horloge externe. 1 = les SV sont synchronisées par un signal d'horloge provenant d'une horloge d'une zone locale non spécifiée. 2 = les SV sont synchronisées par un signal d'horloge de zone globale (traçabilité temporelle). 5 à 254 = les SV sont synchronisées par un signal d'horloge provenant d'une horloge d'une zone locale identifiée par cette valeur. 3; 4; 255 = valeurs réservées - Ne pas utiliser.                                                                                                                                  |
| SmpRate                                                               | INT16U                                                                | smpRate [6] IMPLICIT OCTET STRING (SIZE(2)) OPTIONAL,     | Valeur issue du MSVCB ou du USVCB. OCTET STRING est interprété comme INT16U, tel que défini par le Tableau 15.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

| Format de mémoire tampon abstrait (abstract buffer format) selon la CEI 61850-7-2                                                                                                                                                  | Format de mémoire tampon abstrait (abstract buffer format) selon la CEI 61850-7-2                                                                                                                                                  | Codage en CEI 61850-9-2                                                                                                                                                                                                            | Commentaires                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nom d'attribut                                                                                                                                                                                                                     | Type d'attribut                                                                                                                                                                                                                    | Règles de codage de base ASN.1 (BER) SavPdu::= SEQUENCE {                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                        |
| Sample [1..n]                                                                                                                                                                                                                      | Type depends on the CDC defined in CEI 61850-7-3.                                                                                                                                                                                  | sample [7] IMPLICIT OCTET STRING (SIZE(n))                                                                                                                                                                                         | Liste des valeurs de données liée à la définition de l'ensemble de données. Pour l'encodage des données (Data), les règles de codage des types de données de base doivent s'appliquer, comme cela est défini par le Tableau 15. SIZE(n) est la taille cumulée de toutes les données transmises, comme cela est défini dans le DataSet. |
| SmpMod                                                                                                                                                                                                                             | INT16U                                                                                                                                                                                                                             | smpMod [8] IMPLICIT OCTET STRING (SIZE(2)) OPTIONAL }                                                                                                                                                                              | Valeur issue du MSVCB ou du USVCB. OCTET STRING est interprété comme INT16U, tel que défini par le Tableau 15.                                                                                                                                                                                                                         |
| NOTE L'utilisation de l'attribut OptFlds, conformément à la CEI 61850-7-2, n'est pas nécessaire du fait que les attributs associés RefrTm, security, SmpRate et DatSet seront signés comme étant facultatifs via l'attribut ASN.1, | NOTE L'utilisation de l'attribut OptFlds, conformément à la CEI 61850-7-2, n'est pas nécessaire du fait que les attributs associés RefrTm, security, SmpRate et DatSet seront signés comme étant facultatifs via l'attribut ASN.1, | NOTE L'utilisation de l'attribut OptFlds, conformément à la CEI 61850-7-2, n'est pas nécessaire du fait que les attributs associés RefrTm, security, SmpRate et DatSet seront signés comme étant facultatifs via l'attribut ASN.1, | NOTE L'utilisation de l'attribut OptFlds, conformément à la CEI 61850-7-2, n'est pas nécessaire du fait que les attributs associés RefrTm, security, SmpRate et DatSet seront signés comme étant facultatifs via l'attribut ASN.1,                                                                                                     |

... }

## END

Pour la définition d'étiquette des types de données de base, voir 8.6.

## 8.6 Définitions relatives aux types de données de base - Fonctionnalité de la couche présentation

Le Tableau 15 donne l'encodage relatif aux types de données de base utilisés pour les valeurs de données (Data) référencées par les membres des ensembles de données.

Tableau 15 - Encodage relatif aux types de données de base

| Types de données selon la CEI 61850-7-2   | Encodage dans l'ensemble de données        | Commentaires   |
|-------------------------------------------|--------------------------------------------|----------------|
| BOOLEAN                                   | 8 Bit set to 0 FALSE; anything else = TRUE |                |
| INT8                                      | 8 Bit Big Endian                           | signé          |
| INT16                                     | 16 Bit Big Endian                          | signé          |
| INT32                                     | 32 Bit Big Endian                          | signé          |
| INT64                                     | 64 Bit Big Endian                          | signé          |
| INT8U                                     | 8 Bit Big Endian                           | non signé      |
| INT16U                                    | 16 Bit Big Endian                          | non signé      |
| INT24U                                    | 24 Bit Big Endian                          | non signé      |
| INT32U                                    | 32 Bit Big Endian                          | non signé      |
| FLOAT32                                   | 32 Bit IEEE Floating Point (IEEE 754)      |                |
| FLOAT64                                   | 64 Bit IEEE Floating Point (IEEE 754)      |                |
| ENUMERATED                                | 32 Bit Big Endian                          |                |

| Types de données selon la CEI 61850-7-2   | Encodage dans l'ensemble de données          | Commentaires   |
|-------------------------------------------|----------------------------------------------|----------------|
| CODED ENUM                                | 32 Bit Big Endian                            |                |
| OCTET STRING                              | 20 Bytes ASCII Text, Null terminated         |                |
| VISIBLE STRING                            | 35 Bytes ASCII Text, Null terminated         |                |
| UNICODE STRING                            | 20 Bytes ASCII Text, Null terminated         |                |
| ObjectName                                | 20 Bytes ASCII Text, Null terminated         |                |
| ObjectReference                           | 20 Bytes ASCII Text, Null terminated         |                |
| TimeStamp                                 | 64 Bit Timestamp as defined in CEI 61850-8-1 |                |
| EntryTime                                 | 48 Bit Timestamp as defined in CEI 61850-8-1 |                |
| Types de données selon la CEI 61850-8-1   | Encodage dans l'ensemble de données          | Commentaires   |
| BITSTRING                                 | 32 Bit Big Endian                            |                |

## 9 Conformité

## 9.1 Notation

Le Paragraphe 9.2 à l'Article 11 font appel aux abréviations données à l'Article 4.

## 9.2 PICS

## 9.2.1 Conformité des profils

Le Tableau 16 et le Tableau 17 définissent la déclaration de conformité de base.

Tableau 16 PICS prenant en charge le "A-Profile"

|    |                         | Client   | Serveur   | Valeur/commentaire   |
|----|-------------------------|----------|-----------|----------------------|
|    |                         | F/S      | F/S       |                      |
| A1 | Client/Server A-Profile | c1       | c1        | Se référer à 5.2     |
| A2 | SV A-Profile            | c2       | c2        | Se référer à 5.3     |

c1 - Doit être "m" si les services pris en charge spécifiés par le Tableau 1 sont déclarés dans la déclaration de conformité de base ACSI .

c2 - Doit être "m" si les services pris en charge spécifiés par le Tableau 4 sont déclarés dans la déclaration de conformité de base ACSI .

Tableau 17 PICS prenant en charge le "T-Profile"

|                                                                                      |                                                                                      | Client                                                                               | Serveur                                                                              | Valeur/commentaire                                                                   |                                                                                      |                                                                                      |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|                                                                                      |                                                                                      | F/S                                                                                  | F/S                                                                                  |                                                                                      |                                                                                      |                                                                                      |
| T1                                                                                   | TCP/IP T-Profile                                                                     | c1                                                                                   | c1                                                                                   |                                                                                      |                                                                                      |                                                                                      |
| T2                                                                                   | SV T-Profile                                                                         | c2                                                                                   | c2                                                                                   |                                                                                      |                                                                                      |                                                                                      |
| c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". | c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". | c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". | c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". | c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". | c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". | c1 - Doit être "m" si la prise en charge pour A1 est déclarée. Sinon, doit être "i". |

## 9.2.2 Services SV

Ce  paragraphe  décrit  la  déclaration  de  conformité  de  mise  en  œuvre  de  protocole  (protocol implementation conformance statement) pour des services des valeurs échantillonnées basés sur la déclaration de conformité de base de la CEI 61850-7-2. Voir le Tableau 18.

Tableau 18 - Déclaration de conformité SV

| Services         | Client/ abonné   | Serveur/ émetteur   | Valeur/commentaire   |
|------------------|------------------|---------------------|----------------------|
| Multidiffusion   |                  |                     |                      |
| SendM SV Message | c1               | c1                  |                      |
| Get MSVCB Values | c2               | c2                  |                      |
| Set MSVCB Values | c3               | c3                  |                      |
| Envoi individuel |                  |                     |                      |
| Send USV Message | c1               | c1                  |                      |
| Get USVCB Values | c2               | c2                  |                      |
| Set USVCB Values | c3               | c3                  |                      |

c1 - Doit être déclaré "m" pour au moins une ( MSV ou USV ), tel que déclaré dans la déclaration de conformité  de base ACSI .

c2 - Doit être déclaré "o", tel que déclaré dans la déclaration de conformité  de base ACSI . Voir la CEI 61850-8-1, Tableau 117 ' Déclaration de conformité pour le service Read '.

c3 - Doit être déclaré "o", tel que déclaré dans la déclaration de conformité  de base ACSI . Voir la CEI 61850-8-1, Tableau 118 ' Déclaration de conformité pour Write '.

## 10  Langage de configuration de poste (SCL)

Les  mises  en  œuvre  conformes  doivent  prendre  en  charge  le  langage  de  configuration  de poste  (substation  configuration  language),  tel  que  défini  par  la  CEI 61850-6  pour  l'échange entre les outils d'étude.

## 11  Définitions d'éléments d'adresses spécifiques SCSM

Cet article  définit  les  types  "xs:string"  autorisés  pour  l'adressage SV comme paramètres type de  l'élément  P  de  l'élément  "Address".  Les  valeurs  et  les  restrictions  de  caractères  sont définies par le Tableau 19.

Tableau 19 - Définitions relatives au SCL SV

| Désignation P-type                                           | Description                                                  | m/o                                                          | Restrictions/commentaires                                                                                                                             |
|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAC-Address                                                  | Media Access Address value                                   | m                                                            | Doit être constitué de 6 groupes de 2 caractères visibles séparés par des traits d'union (-). Les caractères doivent être limités à 0 à 9 et à A à F. |
| APPID                                                        | Identificateur d'application (Application Identifier)        | o                                                            | Doit être constitué de 4 caractères. Les caractères doivent être limités à 0 à 9 et à A à F.                                                          |
| VLAN-PRIORITY                                                | VLAN User Priority                                           | c1                                                           | Doit être constitué d'un seul caractère. Les caractères doivent être limités à 0 à 7.                                                                 |
| VLAN-ID                                                      | VLAN ID                                                      | o                                                            | Doit être constitué de 3 caractères. Les caractères doivent être limités à 0 à 9 et à A à F.                                                          |
| c1 - Ne doit être présent que si VLAN est également présent. | c1 - Ne doit être présent que si VLAN est également présent. | c1 - Ne doit être présent que si VLAN est également présent. | c1 - Ne doit être présent que si VLAN est également présent.                                                                                          |

## Annexe A

(informative)

## Format de la trame ISO/CEI 8802-3 et règles de codage de base ASN.1

## A.1 Format de la trame ISO/CEI 8802-3

Voir Figure A.1les Figures A.1, A.2 et A.3.

<!-- image -->

IEC   1790/11

Figure A.1 - Format de la trame ISO/CEI 8802-3 - Pas de redondance de liaison

<!-- image -->

IEC   1791/11

Figure A.2 - Format de la trame ISO/CEI 8802-3 - Redondance de liaison: HSR

<!-- image -->

IEC   1792/11

Figure A.3 - Format de la trame ISO/CEI 8802-3 - Redondance de liaison: PRP

## A.2 Règles de codage de base ASN.1 (BER)

Les  règles  de  codage  de  base ASN.1 (telles  que  spécifiées  par  l'ISO/CEI 8825-1)  seront utilisées  pour  coder  et  décoder  des  valeurs  échantillonnées.  Une  présentation  générale  des principaux principes d'encodage est donnée ci-dessous.

La syntaxe de transfert des BER a le format d'un triplet TLV [Type (type), Length (longueur), Value  (valeur)]  ou  [Tag  (étiquette),  Length  (longueur),  Value  (valeur)],  suivant  les  indications de la Figure A.4.

Tous les champs (T, L, V) sont des séries d'octets. La valeur V peut elle-même être un triplet TLV, si elle est composée.

La  syntaxe  de  transfert  est  au  niveau  octet  et  orientée  "gros-boutiste".  Le  champ  "Length" (longueur) L définit la longueur de chaque triplet TLV.

Figure A.4 - Format des règles de codage de base

<!-- image -->

Les  octets  du  champ  "Tag"  (étiquette)  correspondent  au  codage  de  l'étiquette  du  type  de valeur. La Figure A.5 montre les deux formats des octets "Tag" (étiquette).

## Octet 'Tag' (étiquette)

<!-- image -->

IEC   1794/11

Figure A.5 - Format des octets "Tag" (étiquette)

## A.3 Exemple de structure de trame APDU codée ASN.1

L'exemple de la Figure A.6 donne la structure de trame APDU avec 4 ASDU concaténées.

Figure A.6 - Exemple de structure de trame APDU codée ASN.1

<!-- image -->

| "Tag" (étiquette) ASN.1   | L = Length (longueur)   |
|---------------------------|-------------------------|

IEC   1795/11

## Annexe B

(informative)

## Sélection d'adresse multidiffusion (multicast)

Dans le but d'augmenter les performances globales de réception des messages multidiffusion (par exemple "GOOSE", "GSSE", et "Sampled Values"), il est préférable d'avoir un matériel du type "media access controller ( MAC )" (contrôleur d'accès aux données) qui effectue le filtrage. Les  algorithmes  de  hachage  des  divers  circuits  intégrés  le  font  de  manière  variable.  Il  est recommandé,  en  tant  qu'intégrateur  système,  d'évaluer  l'impact  de  ces  algorithmes  lors  de l'affectation des adresses multidiffusion de destination.

Il  convient  que  les  fournisseurs  d'implémentations  CEI 61850-8-1  ou  CEI 61850-9-2  diffusant ces types de messages donnent des recommandations d'adressage basées sur les algorithmes de hachage des circuits intégrés MAC .  Une telle recommandation pourrait être la suivante:

Les  adresses  multidiffusion  (chaîne  d'octets  de  taille 6)  utilisées  dans  la  présente  norme auront la structure suivante.

- -Les trois premiers octets sont affectés par l'IEEE:01-0C-CD.
- -Le quatrième  octet sera 01 pour GOOSE , 02 pour GSSE , et 04 pour des  valeurs échantillonnées multidiffusion.
- -Les deux derniers octets seront utilisés en tant qu'adresses individuelles affectées dans les plages définies par le Tableau B.1.

Tableau B.1 - Exemple d'adressage multidiffusion recommandé

|                          | Affectations de plages d'adresses recommandées   | Affectations de plages d'adresses recommandées   |
|--------------------------|--------------------------------------------------|--------------------------------------------------|
| Service                  | Début d'adresse (hexadécimal)                    | Fin d'adresse (hexadécimal)                      |
| GOOSE                    | 01-0C-CD-01-00-00                                | 01-0C-CD-01-01-FF                                |
| GSSE                     | 01-0C-CD-02-00-00                                | 01-0C-CD-02-01-FF                                |
| Multicast sampled values | 01-0C-CD-04-00-00                                | 01-0C-CD-04-01-FF                                |

\_\_\_\_\_\_\_\_\_\_\_

## INTERNATIONAL ELECTROTECHNICAL COMMISSION

3, rue de Varembé PO Box 131 CH-1211 Geneva 20 Switzerland

Tel:  + 41 22 919 02 11

Fax: + 41 22 919 03 00

info@iec.ch

www.iec.ch