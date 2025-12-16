| INTERNATIONAL STANDARD   | IEC 61850-9-1 First edition   |
|--------------------------|-------------------------------|

## Communication networks and systems in substations -

## Part 9-1: Specific Communication Service Mapping (SCSM) Sampled values over serial unidirectional multidrop point to point link

<!-- image -->

## Publication numbering

As  from  1  January  1997  all  IEC  publications  are  issued  with  a  designation  in  the 60000 series. For example, IEC 34-1 is now referred to as IEC 60034-1.

## Consolidated editions

The IEC is  now  publishing  consolidated  versions  of  its  publications.  For  example, edition  numbers  1.0,  1.1  and  1.2  refer,  respectively,  to  the  base  publication,  the base publication incorporating amendment 1 and the base publication incorporating amendments 1 and 2.

## Further information on IEC publications

The technical content of IEC publications is kept under constant review by the IEC, thus  ensuring  that  the  content  reflects  current  technology.  Information  relating  to this publication, including its validity, is available in the IEC Catalogue of publications  (see below)  in  addition  to  new  editions,  amendments  and corrigenda. Information  on  the  subjects  under  consideration  and  work  in  progress  undertaken by the technical committee which has prepared this publication, as well as the list of publications issued, is also available from the following:

•

•

•

•

IEC Web Site (www.iec.ch)

Catalogue of IEC publications

The  on-line  catalogue  on  the  IEC  web  site  (http://www.iec.ch/searchpub/cur\_fut.htm) enables you to search by a variety of criteria including text searches, technical committees  and  date  of  publication.  On-line  information  is  also  available  on recently  issued  publications,  withdrawn  and  replaced  publications,  as  well  as corrigenda.

IEC Just Published

This  summary  of  recently  issued  publications  (http://www.iec.ch/online\_news/ justpub/jp\_entry.htm)  is  also  available  by  email.  Please  contact  the  Customer Service Centre (see below) for further information.

Customer Service Centre

If you have any questions regarding this publication or need further assistance, please contact the Customer Service Centre:

Email: custserv@iec.ch

Tel:

+41 22 919 02 11

Fax:

+41 22 919 03 00

INTERNATIONAL

STANDARD

IEC

61850-9-1

First edition 2003-05

## Communication networks and systems in substations -

## Part 9-1: Specific Communication Service Mapping (SCSM) Sampled values over serial unidirectional multidrop point to point link

 IEC 2003  Copyright - all rights reserved

No  part  of  this  publication  may  be  reproduced  or  utilized  in  any  form  or  by  any  means,  electronic  or mechanical, including photocopying and microfilm, without permission in writing from the publisher.

International  Electrotechnical  Commission,    3,  rue  de  Varembé,  PO  Box  131,  CH-1211  Geneva  20,  Switzerland Telephone: +41 22 919 02 11 Telefax: +41 22 919 03 00 E-mail: inmail@iec.ch    Web: www.iec.ch

<!-- image -->

<!-- image -->

U

## CONTENTS

| FOREWORD.......................................................................................................................... 4                                                                                  | FOREWORD.......................................................................................................................... 4                                                                                    | FOREWORD.......................................................................................................................... 4                                                                                    | FOREWORD.......................................................................................................................... 4   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| INTRODUCTION....................................................................................................................                                                                                      | INTRODUCTION....................................................................................................................                                                                                        | INTRODUCTION....................................................................................................................                                                                                        | 6                                                                                                                                      |
| 1 Scope ..............................................................................................................................                                                                                | 1 Scope ..............................................................................................................................                                                                                  | 1 Scope ..............................................................................................................................                                                                                  | 7                                                                                                                                      |
| 2 Normative references.......................................................................................................                                                                                         | 2 Normative references.......................................................................................................                                                                                           | 2 Normative references.......................................................................................................                                                                                           | 8                                                                                                                                      |
| 3 Terms and definitions.......................................................................................................                                                                                        | 3 Terms and definitions.......................................................................................................                                                                                          | 3 Terms and definitions.......................................................................................................                                                                                          | 8                                                                                                                                      |
| 4 Abbreviations ...................................................................................................................                                                                                   | 4 Abbreviations ...................................................................................................................                                                                                     | 4 Abbreviations ...................................................................................................................                                                                                     | 8                                                                                                                                      |
| 5 Principle of mapping to the serial unidirectional multidrop point to point link .....................                                                                                                               | 5 Principle of mapping to the serial unidirectional multidrop point to point link .....................                                                                                                                 | 5 Principle of mapping to the serial unidirectional multidrop point to point link .....................                                                                                                                 | 9                                                                                                                                      |
| 5.1                                                                                                                                                                                                                   | Communication stack..............................................................................................                                                                                                       | Communication stack..............................................................................................                                                                                                       | 9                                                                                                                                      |
|                                                                                                                                                                                                                       | 5.1.1                                                                                                                                                                                                                   | Physical layer.............................................................................................10                                                                                                           |                                                                                                                                        |
|                                                                                                                                                                                                                       | 5.1.2                                                                                                                                                                                                                   | Link layer                                                                                                                                                                                                              | ...................................................................................................11                                  |
|                                                                                                                                                                                                                       | 5.1.3                                                                                                                                                                                                                   | Network layer .............................................................................................12                                                                                                           |                                                                                                                                        |
|                                                                                                                                                                                                                       | 5.1.4                                                                                                                                                                                                                   | Transport layer...........................................................................................12                                                                                                            |                                                                                                                                        |
|                                                                                                                                                                                                                       | 5.1.5                                                                                                                                                                                                                   | Session layer                                                                                                                                                                                                           | .............................................................................................12                                        |
|                                                                                                                                                                                                                       | 5.1.6                                                                                                                                                                                                                   | Presentation layer                                                                                                                                                                                                      | ......................................................................................12                                               |
|                                                                                                                                                                                                                       | 5.1.7                                                                                                                                                                                                                   | Application layer.........................................................................................12                                                                                                            |                                                                                                                                        |
|                                                                                                                                                                                                                       | 5.2 Restrictions............................................................................................................12                                                                                          | 5.2 Restrictions............................................................................................................12                                                                                          |                                                                                                                                        |
| 6                                                                                                                                                                                                                     | Mapping of common types...............................................................................................12                                                                                                | Mapping of common types...............................................................................................12                                                                                                |                                                                                                                                        |
|                                                                                                                                                                                                                       | 6.1 Object name ..........................................................................................................12                                                                                            | 6.1 Object name ..........................................................................................................12                                                                                            |                                                                                                                                        |
|                                                                                                                                                                                                                       | 6.2 Object reference ....................................................................................................12                                                                                             | 6.2 Object reference ....................................................................................................12                                                                                             |                                                                                                                                        |
| 7                                                                                                                                                                                                                     | Mapping of the model for transmission of sampled values using multicast........................13                                                                                                                       | Mapping of the model for transmission of sampled values using multicast........................13                                                                                                                       |                                                                                                                                        |
|                                                                                                                                                                                                                       | 7.1 Mapping of the multicast sampled values services..................................................13                                                                                                                | 7.1 Mapping of the multicast sampled values services..................................................13                                                                                                                |                                                                                                                                        |
|                                                                                                                                                                                                                       | 7.2 Mapping of the update of the sampled value buffer.................................................14                                                                                                                | 7.2 Mapping of the update of the sampled value buffer.................................................14                                                                                                                |                                                                                                                                        |
|                                                                                                                                                                                                                       | 7.3 Additional definitions for the transmission of sampled analogue values ...................14                                                                                                                        | 7.3 Additional definitions for the transmission of sampled analogue values ...................14                                                                                                                        |                                                                                                                                        |
|                                                                                                                                                                                                                       | 7.3.1                                                                                                                                                                                                                   | Application layer functionality .....................................................................14                                                                                                                 |                                                                                                                                        |
|                                                                                                                                                                                                                       | 7.3.2                                                                                                                                                                                                                   | Presentation layer functionality...................................................................15                                                                                                                   |                                                                                                                                        |
|                                                                                                                                                                                                                       | 7.3.3                                                                                                                                                                                                                   | Transport layer functionality                                                                                                                                                                                           | .......................................................................15                                                              |
| 8                                                                                                                                                                                                                     | Mapping of the common data classes..............................................................................16                                                                                                      | Mapping of the common data classes..............................................................................16                                                                                                      |                                                                                                                                        |
|                                                                                                                                                                                                                       | 8.1                                                                                                                                                                                                                     | Overview                                                                                                                                                                                                                | ...............................................................................................................16                      |
|                                                                                                                                                                                                                       | 8.2                                                                                                                                                                                                                     | Additional definitions for the mapping of the common data classes                                                                                                                                                       | .........................16                                                                                                            |
|                                                                                                                                                                                                                       | Annex A (normative) Definition of data set instances and related multicast sampled value control instances ..........................................................................................................19 | Annex A (normative) Definition of data set instances and related multicast sampled value control instances ..........................................................................................................19 |                                                                                                                                        |
| Annex B (informative) Calculation of required bandwidth.......................................................22                                                                                                      | Annex B (informative) Calculation of required bandwidth.......................................................22                                                                                                        | Annex B (informative) Calculation of required bandwidth.......................................................22                                                                                                        |                                                                                                                                        |
| Annex C (informative) Definitions of logical node instance names and data names related to the data sets ..........................................................................................................24 | Annex C (informative) Definitions of logical node instance names and data names related to the data sets ..........................................................................................................24   | Annex C (informative) Definitions of logical node instance names and data names related to the data sets ..........................................................................................................24   |                                                                                                                                        |

| Figure 1 - Example for the use of the serial unidirectional multidrop point to point link ............                                                                                                                        | 7                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Figure 2 - Communication stack............................................................................................10                                                                                                  |                                                      |
| Figure 3 - Concatenation of several ASDU's into one APDU                                                                                                                                                                      | ..................................................14 |
| Figure A.1 - Data set for status indication..............................................................................20                                                                                                   |                                                      |
| Figure B.1 - Ethernet Frame Format......................................................................................23                                                                                                    |                                                      |
| Figure C.1 - Contents of the universal data set based on the specification in IEC 60044-8                                                                                                                                     | ....27                                               |
| Figure D.1 - Example for general block diagram of a single-phase electronic transformer                                                                                                                                       | .....28                                              |
| Figure D.2 - Example for electronic transformers configuration..............................................29                                                                                                                |                                                      |
| Table 1 - Mapping of the object reference .............................................................................13                                                                                                     |                                                      |
| Table 2 - Mapping of the multicast sampled value services....................................................13                                                                                                               |                                                      |
| Table 3 - Encoding for the transmission of sampled value buffer                                                                                                                                                               | ...........................................15        |
| Table 4 - Extended common data class single point status information ..................................16                                                                                                                     |                                                      |
| Table 5 - Encoding of the common data class SPS used for the universal data set                                                                                                                                               | ................16                                   |
| Table 6 - Encoding of the common data class MV .................................................................17                                                                                                            |                                                      |
| Table 7 - Encoding of common data class SPS used for the status indication group...............18                                                                                                                             |                                                      |
| Table A.1 - Predefined multicast sampled value control block instances relating to the transmission of the Universal Data Set according to IEC 60044-8.................................19                                     |                                                      |
| Table A.2 - Predefined multicast sampled value control block instances relating to the transmission of status indications ..........................................................................................21        |                                                      |
| Table B.1 - Selection guide for Ethernet physical layer (receiving node).................................22                                                                                                                   |                                                      |
| Table B.2 - Selection guide for Ethernet physical layer (sending node)                                                                                                                                                        | ..................................22                 |
| Table C.1 - Definitions of logical instance name and data names related to the universal data set ..................................................................................................................24        |                                                      |
| Table C.2 - Definitions of logical instance name and data names related to the status indication data set .................................................................................................................26 |                                                      |

## INTERNATIONAL ELECTROTECHNICAL COMMISSION

\_\_\_\_\_\_\_\_\_\_\_\_\_

## COMMUNICATION NETWORKS AND SYSTEMS IN SUBSTATIONS -

## Part 9-1: Specific Communication Service Mapping (SCSM) Sampled values over serial unidirectional multidrop point to point link

## FOREWORD

- 1) The IEC (International Electrotechnical Commission) is a worldwide organisation for standardisation comprising all  national  electrotechnical  committees  (IEC National  Committees).  The  object  of  the  IEC is  to  promote international co-operation on all questions concerning standardisation in the electrical and electronic fields. To this  end  and  in  addition  to  other  activities,  the  IEC publishes  International  Standards.  Their  preparation  is entrusted  to  technical  committees;  any  IEC National  Committee  interested  in  the  subject  dealt  with  may participate  in  this  preparatory  work.  International,  governmental  and  non-governmental  organisations  liaising with the IEC also participate in this preparation. The IEC collaborates closely with the International Organisation for Standardisation (ISO) in accordance with conditions determined by agreement between the two organisations.
- 2)  The  formal  decisions  or  agreements  of  the  IEC on  technical  matters  express,  as  nearly  as  possible,  an international consensus of opinion on the relevant subjects since each technical committee has representation from all interested National Committees.
- 3) The documents produced have the form of recommendations for international use and are published in the form of  standards,  technical  specifications,  technical  reports  or  guides  and  they  are  accepted  by  the  National Committees in that sense.
- 4) In  order  to  promote  international  unification,  IEC National  Committees  undertake  to  apply  IEC International Standards  transparently  to  the  maximum  extent  possible  in  their  national  and  regional  standards.  Any divergence  between  the  IEC Standard  and  the  corresponding  national  or  regional  standard  shall  be  clearly indicated in the latter.
- 5) The  IEC provides  no  marking  procedure  to  indicate  its  approval  and  cannot  be  rendered  responsible  for  any equipment declared to be in conformity with one of its standards.
- 6) Attention is drawn to the possibility that some of the elements of this International Standard may be the subject of patent rights. The IEC shall not be held responsible for identifying any or all such patent rights.

International  Standard  IEC 61850-9-1  has  been  prepared  by  IEC technical  committee  57: Power system control and associated communications.

The text of this standard is based on the following documents:

| FDIS        | Report on voting   |
|-------------|--------------------|
| 57/619/FDIS | 57/636/RVD         |

Full  information  on  the  voting  for  the  approval  of  this  standard  can  be  found  in  the  report  on voting indicated in the above table.

This publication has been drafted in accordance with the ISO/IEC Directives, Part 2.

IEC 61850 consists of the following parts, under the general title Communication networks and systems in substations.

- Part 1: Introduction and overview
- Part 2: Glossary  1
- Part 3: General requirements
- Part 4: System and project management
- Part 5: Communication requirements for functions and devices models  2
- Part 6: Configuration description language  for communication  in  electrical substations related to IEDs  1
- Part 7-1: Basic communication structure for substation and feeder equipment - Principles and models
- Part 7-2: Basic  communication  structure  for  substation  and  feeder  equipment  -  Abstract communication service interface (ACSI)
- Part 7-3: Basic communication structure for substation and feeder equipment - Common data classes
- Part 7-4: Basic  communication  structure  for  substation  and  feeder  equipment  -  Compatible logical node classes and data classes
- Part 8-1: Specific communication service mapping (SCSM) -Mappings to MMS (ISO/IEC 9506-1 and ISO/IEC 9506-2) and to ISO/IEC 8802-3  1
- Part 9-1: Specific  communication  service  mapping  (SCSM)  -  Sampled  values  over  serial unidirectional multidrop point to point link
- Part 9-2: Specific communication service mapping (SCSM)  Sampled  values over ISO/IEC 8802-3  1
- Part 10: Conformance testing 1

The relationship between IEC 60044-8 and this standard is as follows:

IEC 60044-8 defines a merging unit as interface to electronic current and voltage transformers. Data  objects  provided  by  that  merging  unit  are  specified  in  IEC 60044-8.  This  standard specifies a serial communication interface between the merging unit and equipment using the digital output of the merging unit like protection or metering equipment. For the specification of that serial interface, a subset of the abstract communication services defined in IEC 61850-7-2 are mapped on an ISO/IEC 8802-3 based communication link.

The committee has decided that the contents of this publication will remain unchanged until 2005. At this date, the publication will be

- reconfirmed;
- withdrawn;
- replaced by a revised edition, or
- amended.

A bilingual version of this standard may be issued at a later date.

-------

1    Under consideration.

2    To be published.

## INTRODUCTION

This part of IEC 61850 applies to electronic current and voltage transformers (ECT and EVT) with  a  digital  output  via  a  merging  unit,  for  use  with  electronic  measuring  instruments  and electronic protective devices.

The  transformer  technology  can  be  based  on  optical  arrangements  equipped  with  electronic components,  on  air  core  coils  (with  or  without  a  built-in  integrator)  or,  on  iron  core  coils with integrated  burden  and  used  as  a  current  to  voltage  converter,  alone  or  equipped  with electronic components.

For digital output, this standard takes into account a point to point connection from the merging unit to electronic measuring instruments and electronic devices.

This mapping allows interoperability between devices from different manufacturers.

This standard does not specify individual implementations or products, nor does it constrain the implementation of entities and interfaces within a computer system. This standard specifies the externally visible functionality of implementations.

## Reading Guide

- The point to point transformer interface as defined here is based on the concepts described in IEC 60044-8. This standard extends this concept and proposes an alternative link layer to  provide  a  solution  for  transmitting  sampled  measured  values  via    Ethernet  based interfaces. For the definition and measurement of the accuracy, synchronisation methods, data rates etc. of the transformers, refer to IEC 60044-8.
- This document can best be understood if the reader is thoroughly familiar with Parts 7-1, 7-2, 7-3 and 7-4 of this Standard.
- No explanations  to  the  ACSI  services  are  given  in  this  part  of  the  standard.  For  detailed information about the use of the ACSI services, refer to IEC 61850-7-2.

## COMMUNICATION NETWORKS AND SYSTEMS IN SUBSTATIONS -

## Part 9-1: Specific Communication Service Mapping (SCSM) Sampled values over serial unidirectional multidrop point to point link

## 1 Scope

This  part  of  IEC 61850  specifies  the  specific  communication  service  mappings  for  the communication  between  bay  and  process  level  and  it  specifies  a  mapping  on  a  serial unidirectional  multidrop  point  to  point  link  in  accordance  with  IEC 60044-8.  This  part  of IEC 61850 specifies a mapping of the abstract service for the transmission of sampled values (as  defined  in  IEC 61850-7-2)  on  a  serial  unidirectional  multidrop  point  to  point  link  in accordance  with  IEC 60044-8.  It  applies  to  the  communication  between  merging  units  of electronic  current  (ECT)  or  voltage-transformers  (EVT)  and  bay  devices  such  as  protection relays. If higher requirements on sampling rate, further sampled measured value data sets in addition  to  the  universal  data  set,  inter-bay  communication  and  synchronisation  apply,  these will be covered by IEC 61850-9-2 3 . Figure 1 shows the schematics of this interface.

Figure 1 - Example for the use of the serial unidirectional multidrop point to point link

<!-- image -->

-------

3    Under consideration.

## 2 Normative references

The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applies.  For  undated  references,  the  latest  edition  of the referenced document (including any amendments) applies.

IEC 60044-7: Instrument Transformers - Part 7: Electronic voltage transformers

IEC 60044-8: Instrument Transformers - Part 8: Electronic current transformers

IEC 60874-10-1:1997, Connectors for optical fibres and cables -Part 10-1: Detail specification for fibre optic connector type BFOC/2,5 terminated to multimode fibre type A1

IEC 61850-7-2: Communication  networks  and  systems  in  substations  -  Part  7-2:  Basic  communication  structure  for  substation  and  feeder  equipment  -  Abstract  communication  service interface (ACSI)

IEC 61850-7-3: Communication  networks  and  systems  in  substations  -  Part  7-3:  Basic communication structure for substation and feeder equipment - Common data classes

ISO/IEC 8802-3: Information  technology -Telecommunications  and  information  exchange between  systems -Local  and  metropolitan  area  networks -Specific  requirements -Part  3: Carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specifications

ISO/IEC  8825-1: Information  technology  -  ASN.1  encoding  rules:  Specification  of  Basic  Encoding Rules (BER), Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER)

IEEE 802.1Q-1998: IEEE Standards for Local and Metropolitan Area Networks: Virtual Bridged Local Area Networks

IEEE 802.3: Information Technology - Telecommunication and Information Exchange Between Systems  -  LAN/MAN  -  Specific  Requirements  -  Part  3:  Carrier  Sense  Multiple  Access  with Collision Detection (CSMA/CD) Access Method and Physical Layer Specifications

## 3 Terms and definitions

For  the  purpose  of  this  part  of  IEC 61850,  the  definitions  of  IEC 61850-2 4 ,  IEC 60044-7  and IEC 60044-8 apply.

## 4 Abbreviations

| ACSI   | Abstract Communication Service Interface   |
|--------|--------------------------------------------|
| ASDU   | Application Service Data Unit              |
| ASN.1  | Abstract Syntax Notation number One        |
| APCI   | Application Protocol Control Information   |
| APDU   | Application Protocol Data Unit             |
| AUI    | Attachment Unit Interface                  |
| BER    | ASN.1 Basic Encoding Rules                 |
| CFI    | Canonical format identifier                |

-------

4     Under consideration.

| CSMA/CD   | Carrier Sense Multiple Access/Collision Detection   |
|-----------|-----------------------------------------------------|
| DF        | Data Frame                                          |
| DO        | Data Object                                         |
| DSG       | Data Set Group                                      |
| ECT       | Electronic Current Transformers                     |
| EVT       | Electronic Voltage Transformers                     |
| LSDU      | Link Layer Service Data Unit                        |
| MAC       | Media Access Control                                |
| MSVCB     | Multicast Sampled Value Control Block               |
| MU        | Merging Unit                                        |
| PDU       | Protocol Data Unit                                  |
| SBO       | Select Before Operate                               |
| SC        | Secondary Converter                                 |
| SCSM      | Specific Communication Services Mapping             |
| SIG       | Status Indication Group                             |
| SAV       | Sampled Analogue Value                              |
| TCI       | Tag Control Information                             |
| TPID      | Tag Protocol Identifier                             |
| VID       | VLAN Identifier                                     |
| VLAN      | Virtual Local Area Network                          |

## 5 Principle of mapping to the serial unidirectional multidrop point to point link

This  Clause  gives  an  overview  of  the  mapping  to  the  serial  unidirectional  multidrop  point  to point link. It defines the communication stack and data unit structures for the application layer. Restrictions to the application that are a consequence of this mapping are defined as well.

## 5.1 Communication stack

Figure  2  gives  an  overview  of  the  communication  stack.  The  link  layer  is  in  conformity  with ISO/IEC 8802-3.  This  standard  is  usually  referred  to  as  Ethernet.  In  the  following,  the  term Ethernet will be used instead of ISO/IEC 8802-3 (CSMA/CD).

Figure 2 - Communication stack

<!-- image -->

The relevant device standards will specify whether 100Base-FX, 10Base-FL or 10Base-T is used, depending on the application.

## 5.1.1 Physical layer

## 5.1.1.1 Specifications for the Medium Attachment Unit (MAU)

The  connection  of  the  merging  unit  to  the  secondary  equipment  can  be  an  optical  fibre transmission  system.  By  taking  into  account  and  solving  the  EMC  requirements,  a  copper based transmission system is an option.

## 5.1.1.2 Fibre optic transmission system

The preferred version of the fibre optic  transmission  system  is  IEEE  802.3  100Base-FX.  The 10Base-FL  system  could  be  used  also  for  sampling  rates  below  48  × f r (a  selection  guide is given in Annex B). This interface shall be used for applications where this media interface is already  used  for  other  communication  links.  It  is  recommended  to  use  the  BFOC  connectors (IEC 60874-10-1). Two fibres are always necessary for the optical fibre transmission system in order to support the link supervision.

## 5.1.1.3 Twisted-pair transmission system

The  twisted-pair  medium  according  to  IEEE  802.3  10Base-T  could  be  used  as  an  option,  if appropriate electromagnetic shield measures are considered.

## 5.1.2 Link layer

## 5.1.2.1 Ethernet addresses

The  Ethernet  broadcast  address  shall  be  used  as  a  default  value  for  a  destination  address, which consists of ones in the destination address field (the Ethernet frame format is shown in Annex  B).  For  this  reason,  no  address  configuration  is  necessary  on  the  publisher  side. However,  the  destination  address  could  be  configurable  as  an  optional  feature  for  example, adjust a multicast address to connect a merging unit via switch to bay level devices. A unique Ethernet address shall be used as a source address.

NOTE   The recommended address range assignments will be specified in IEC 61850-9-2 and IEC 61850-8-1.

## 5.1.2.2 Priority tagging/Virtual LAN

Priority tagging according to IEEE 802.1Q is used to separate time critical and high priority bus traffic for protection relevant applications from low priority busload.

Structure of the tag header:

<!-- image -->

## 5.1.2.3 Ethertype

An  Ethertype  based  on  ISO/IEC 8802-3  MAC  -  Sublayer  is  registered  by  the  IEEE  Authority Registration.  The  registered  Ethertype  value  is  88-BA  (hexadecimal).  The  sampled  analogue value buffer update is directly mapped to the reserved Ethertype and the Ethertype PDU.

Structure of the Ethertype PDU:

<!-- image -->

## Key

TPID value: 0x8100

User priority: BS3; user priority value shall be set by configuration  to  separate  sampled  analogue  values and time critical protection relevant GOOSE messages from low priority busload.

CFI:  BS1  [0];  No  Embedded  RIF  field  follows  the length/type field in the Ethernet tagged frame.

VID: Virtual LAN support is optional. If this mechanism is  used,  the  VLAN  identifier  (VID)  shall be set by configuration. Otherwise, the VLAN identifier is set by default to 0.

## Key

APPID:  application  identifier.  The  APPID  is  used  to select  sampled  analogue  value  messages  and  to distinguish the application association.

Reserved value range for SAV are 0x4000 to 0x7FFF.

Length:  number  of  octets  including  the  Ethertype PDU starting at APPID (8 + m) (m &lt; 1480).

Reserved 1/Reserved 2: reserved for future standardised applications.

## 5.1.3 Network layer

This layer is intentionally left empty.

## 5.1.4 Transport layer

This layer is intentionally left empty.

## 5.1.5 Session layer

This layer is intentionally left empty.

## 5.1.6 Presentation layer

Empty. See additional definitions in 7.3.

## 5.1.7 Application layer

Empty. See additional definitions in 7.3.

## 5.2 Restrictions

This  specification  is  restricted  to  define  the  communication  between  the  ECT/EVT  related merging  unit  and  devices  on  bay  level  which  need  raw  data  of  ECT  and/or  EVT  for  their algorithms.  Referring  to  the  ACSI,  only  the  mapping  of  sampled  values  using  multicast/ broadcast is supported. The multicast sampled value control (MSVC) class is implicit.

The transmission of sampled values as specified in this standard only uses a unidirectional link from  merging  unit  to  bay  level  devices  with  broadcast/multicast  addressing.  However,  the devices  supporting  this  transmission  will  use  an  interface  which  is  fully  Ethernet  compatible that  includes  all  the  facilities  for  easy  plug  in.  This  may  imply  that  bi-directional  exchanges exist  to  establish  and  maintain  good  quality  transmission.  These  exchanges  are  part  of  the lower communication layers and are specified in the relevant standards.

The  use  of  the  Ethernet  link  in  a  bi-directional  way  to  support  other  exchanges  should  be possible according to device capability, but it should not impact transmission of the universal data set. Typical cases may be synchronisation of local clocks, configuration loading and mode switching. These features are outside the scope of this standard.

## 6 Mapping of common types

## 6.1 Object name

For the transmission of the sampled value buffer, the object reference is encoded as integer values. The single elements of the object reference are assigned to integer values. Integer values  related  to  logical  node  name  and  data  name  are  defined  with  this  SCSM. The integer value related to the logical device name will be defined by configuration tools or will be agreed by vendors of the client and server.

## 6.2 Object reference

As  defined  in  IEC 61850-7-2,  the  name  structure  for  the  whole  path  to  an  instance  is  as follows:

## &lt;LDName&gt; / &lt;LNName&gt;.&lt;DataName&gt;[.&lt;DataName&gt;]. &lt;DataAttributeName&gt;

The  object  reference  in  this  SCSM  concludes  the  whole  path  of  the  class  and  instance reference. Other hierarchy levels are not separately accessible.

In detail the SCSM Data Sets are mapped to the object reference as follows:

Table 1 - Mapping of the object reference

| ACSI Object name                                                                                                                                                                           | SCSM value                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <LDName>                                                                                                                                                                                   | INTEGER UI16                                                                                                                                                                               |
| <LNName>                                                                                                                                                                                   | INTEGER UI8                                                                                                                                                                                |
| <DataName>                                                                                                                                                                                 | INTEGER UI8                                                                                                                                                                                |
| <DataAttributeName>                                                                                                                                                                        | not visible                                                                                                                                                                                |
| NOTE It is assumed, that the data sets used for the transmission of sampled values in many cases include data objects from more than one logical node and are therefore allocated in LLN0. | NOTE It is assumed, that the data sets used for the transmission of sampled values in many cases include data objects from more than one logical node and are therefore allocated in LLN0. |

## 7 Mapping of the model for transmission of sampled values using multicast

There are two data sets specified in this document. The universal data set is compatible with IEC 60044-8 and the status indications is specified in Annex A.

Each data set refers to one multicast sampled value control class instantiation. The mapping of the sampled value buffer update is defined.

The transmission buffer refresh rate and the communication update rate are always equal and not independent from each other. The consequences on the publisher level are:

- After  the  sampling  procedure  is  finished,  the  APDU  will  be  stored  into  the  transmission buffer (refresh rate  = sampled rate), or more than one ASDU ( n = number of ASDUs) could be stored into one APDU frame before the transmission buffer is refreshed (refresh rate = sampled rate/ n ). For a description of the blocking mechanism, see 7.3.
- Only  one  APDU  can  be  stored  into  the  transmission  buffer,  previous  entries  will  be overwritten. The consistency of stored data will be guaranteed in case of overwriting.
- To avoid data overwriting, the data transmission must be initiated from the communication system immediately after the buffer update process is finished.

## 7.1 Mapping of the multicast sampled values services

Table 2 - Mapping of the multicast sampled value services

| ACSI services   | Ethernet services   |
|-----------------|---------------------|
| Send MSVMessage | not supported       |
| GetMSVCValue    | not supported       |
| SetMSVCValue    | not supported       |

## 7.2 Mapping of the update of the sampled value buffer

According  to  the  standard  of  IEC 61850-7-2,  the  communication  system  is  responsible  for updating the buffer of the subscriber.

The update is directly mapped to an Ethertype reserved for IEC 61850 applications based on ISO/IEC 8802-3 MAC - Sublayer.

However, the communication stack used does not provide the following functionalities:

- Initiating  the  update  of  the  sampled  value  buffer  over  the  communication  link.  This  is  an application layer functionality.
- Encode the abstract data types. This is a presentation layer functionality.
- Concatenation and segmentation of ASDU's is not supported.

NOTE   Segmentation  is  not  further  considered,  since  the  maximum  frame  length  of  the  link  layer  protocol  is sufficient.

Therefore, the additional definitions of 7.3 apply.

## 7.3 Additional definitions for the transmission of sampled analogue values

## 7.3.1 Application layer functionality

The  mapping  provides  the  capacity,  to  concatenate  more  than  one  ASDU  into  one  APDU before the APDU is posted into the transmission buffer. The number of ASDUs which will be concatenated  into  one  ASDU  is  defined  with  a  configuration  parameter  and  related  to  the sample rate.

Details are shown in Figure 3.

Figure 3 - Concatenation of several ASDU's into one APDU

<!-- image -->

An ASN.1 tag and length according to ISO/IEC 8825-1 is added up front as a part of the APCI. This  tag  specifies  an  octet  string  and  is  defined  as  context-specific  and  primitive  (0x80) according to the ASN.1 basic encoding rules. The ASN.1 grammar for the sampled analogue value messages are defined as follows to ensure data consistency in combination with further sampled analogue value messages as described in this SCSM.

```
IEC61850 DEFINITIONS IecSavPdu ::= CHOICE { 9-1-Pdu [0] IMPLICIT OCTET STRING, --Used for 9-1 APDU savPdu [1] IMPLICIT SavPdu, --Reserved for 9-2 APDUs --others TBD }
```

## 7.3.2 Presentation layer functionality

For the transmission, the sampled value buffer is encoded as specified in Table 3.

Table 3 - Encoding for the transmission of sampled value buffer

| Abstract Buffer Format according to IEC 61850-7-2   | Abstract Buffer Format according to IEC 61850-7-2    | Coding in IEC 61850-9-1         | Comment                                                                                                                                 |
|-----------------------------------------------------|------------------------------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Attribute Name                                      | Attribute Type                                       |                                 |                                                                                                                                         |
|                                                     |                                                      | OCTET: Tag                      | Tag is encoded according to ASN.1 Basic encoding rules                                                                                  |
|                                                     |                                                      | OCTET STRING: Length            | Length is encoded according to ASN.1 Basic encoding rules                                                                               |
|                                                     |                                                      | UI16: No. of ASDUs              | Number of ASDU which will concatenated into one APDU and stored into the sampled value buffer                                           |
| MsvID                                               | VISIBLE STRING65                                     | OCTET STRING                    | Broadcast MAC address is part of the Ethernet header                                                                                    |
|                                                     |                                                      | UI16: Length                    | Length of the ASDU added as header (UI = Unsigned Integer)                                                                              |
| OptFlds                                             | PACKED LIST                                          |                                 | Not mapped                                                                                                                              |
| DatSet                                              | ObjectReference                                      |                                 |                                                                                                                                         |
| LNName DataSetInstanceName DataSetName LDName       |                                                      | UI8: UI8: UI16:                 |                                                                                                                                         |
| Sample [1 .. n]                                     | Value of the member of the instance of the DATA- SET | Encoding of common data classes | See Note                                                                                                                                |
| SmpCnt                                              | INT16U                                               | UI16                            | Counter specification see IEC 60044-8                                                                                                   |
| RefrTm                                              | TimeStamp                                            |                                 | Not mapped                                                                                                                              |
| ConfRev                                             | INT32U                                               | UI8                             | Configuration revision number will be incremented each time that the configuration of the logical device changes. Default value is NULL |
| SmpSynch                                            | BOOLEAN                                              |                                 | See IEC 60044-8 status word attribute 'NotSynch'                                                                                        |
| SmpRate                                             | INT16U                                               | UI8                             | 0 = not defined; 1 - 255 = number of samples per cycle related to f r                                                                   |

NOTE   For the encoding of the samples, the rules for the encoding of the common data classes apply for the SIG. The mapping of the sampled values and status attributes in  the  universal  data  set  is  optimised  according  to  the specifications in IEC 60044-8. It is not necessary that all possible transformers be connected to the merging unit. In this case, in the universal data set for the current or respectively voltage values not used, zeros are transmitted and the relevant data invalid bits are set.

## 7.3.3 Transport layer functionality

The  communication  system  of  the  publisher  has  to  send  the  sampled  value  buffer  over the communication  link  after  every  buffer  refresh.  The  buffer  refresh  rate  depends  on  the sampling rate and the number of concatenated ASDUs as specified in Clause 7.

## 8 Mapping of the common data classes

## 8.1 Overview

For  the  use  of  the  common  data  classes  defined  in  IEC 61850-7-3  with  the  model  for  the transmission of sampled analogue values, the definitions of 8.2 apply.

## 8.2 Additional definitions for the mapping of the common data classes

To support the mapping to a bitstring based status indication group, an extended common data class  SPS  will  be  defined  as  follows  by  using  the  name  space  mechanism  specified  in IEC 61850-7-2.

Table 4 - Extended common data class single point status information

| SPS class                                | SPS class                                     | SPS class                                     | SPS class                                     | SPS class                                     | SPS class                                |
|------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|------------------------------------------|
| Attribute Name                           | Attribute Type                                | FC                                            | TrgOp                                         | Value / Value Range                           | M/O                                      |
| DataName                                 | Inherited from Data Class (see IEC 61850-7-2) | Inherited from Data Class (see IEC 61850-7-2) | Inherited from Data Class (see IEC 61850-7-2) | Inherited from Data Class (see IEC 61850-7-2) |                                          |
| DataAttribute                            | DataAttribute                                 | DataAttribute                                 | DataAttribute                                 | DataAttribute                                 | DataAttribute                            |
| status                                   | status                                        | status                                        | status                                        | status                                        | status                                   |
| stVal                                    | BOOLEAN                                       | ST                                            | dchg                                          | TRUE | FALSE                                  | AC_UDS_M                                 |
| grpVal                                   | BIT STRING                                    | ST                                            | dchg, dupd                                    |                                               | AC_SIG_M                                 |
| q                                        | Quality                                       | ST                                            | qchg                                          |                                               | M                                        |
| t                                        | TimeStamp                                     | ST                                            |                                               |                                               | M                                        |
| configuration, description and extension | configuration, description and extension      | configuration, description and extension      | configuration, description and extension      | configuration, description and extension      | configuration, description and extension |
| cdcNs                                    | VISIBLE STRING255                             | EX                                            |                                               | 'IEC 61850-9-1:2003'                          |                                          |

| Abbreviation   | Condition                                                       |
|----------------|-----------------------------------------------------------------|
| AC_UDS_M       | Attribute is mandatory, if universal data set is supported      |
| AC_SIG_M       | Attribute is mandatory, if status indication group is supported |

| Data attribute name   | Semantics                                    |
|-----------------------|----------------------------------------------|
| grpVal                | Bitstring where each bit represents a status |

The  common data  classes  of  IEC 61850-7-3  and  of  this  standard  used  in  the  context  of  the transmission of sampled analogue values shall be encoded as specified in Tables 5, 6 and 7 (only status attributes are shown).

Table 5 - Encoding of the common data class SPS used for the universal data set

| Common data class SPS (IEC 61850-9-1)   | Common data class SPS (IEC 61850-9-1)   | Coding in IEC 61850-9-1                 | Comment                                                              |
|-----------------------------------------|-----------------------------------------|-----------------------------------------|----------------------------------------------------------------------|
| Attribute name                          | Attribute type                          |                                         |                                                                      |
| stVal                                   | BOOLEAN                                 | BOOLEAN <0> = FALSE, OFF <1> = TRUE, ON | Status attribute of the universal data set according to IEC 60044-8. |
| grpVal                                  | BIT STRING                              | -                                       | Not mapped                                                           |
| q                                       | Quality                                 | -                                       | Not mapped                                                           |
| t                                       | TimeStamp                               | -                                       | Not mapped                                                           |

NOTE The transmission of information with the common data class SPS is only supported in the context of the universal data set that is defined in IEC 60044-8.

Table 6 - Encoding of the common data class MV

| Common data class MV (IEC 61850-7-3)    | Common data class MV (IEC 61850-7-3)   | Coding in IEC 61850-9-1                         | Comment                                                                     |
|-----------------------------------------|----------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------|
| Attribute name                          | Attribute type                         | Coding in IEC 61850-9-1                         | Comment                                                                     |
| instMag                                 | AnalogueValue                          |                                                 | Not mapped                                                                  |
| mag                                     | AnalogueValue                          |                                                 |                                                                             |
| i f                                     | INT32 FLOATING POINT32                 | UI16 -                                          | Sampled analogue values of the universal data set according to IEC 60044-8. |
| range                                   | ENUMERATED                             | -                                               | Not mapped, see Note 1                                                      |
| q                                       | Quality                                |                                                 |                                                                             |
| validity                                | CODED ENUM                             | BOOLEAN <0> = valid <1> = questionable, invalid |                                                                             |
| detail-qual source test operatorBlocked | PACKED LIST CODED ENUM BOOLEAN BOOLEAN | - - - -                                         | Not mapped Not mapped Not mapped Not mapped                                 |
| t                                       | TimeStamp                              | -                                               | Not mapped, see Note 2                                                      |

NOTE 1   According  to  IEC 61850-7-3,  range  is  an  optional  attribute  and  is  not  required  in  the  sampled  value  buffer format defined in IEC 61850-7-2.

NOTE 2   According to IEC 61850-7-3, t is a mandatory attribute. However,  in  the  specification  of  the  sampled  value buffer  format  as  defined  in  IEC 61850-7-2,  t  is  not  included  with  the  data  object  values;  there  is  only  one  sample counter attached that indicates the refresh of the universal data set sampled values as specified in IEC 60044-8.

However,  for  the  universal  data  set,  the  encoding  of  the  list  of  data  object  values  does  not follow  some  general  rules  but  is  instead  optimised.  The  encoding  of  the  list  of  data  object values is defined in IEC 60044-8.

Table 7 - Encoding of common data class SPS used for the status indication group

| Common data class SPS (IEC 61850-7-3)   | Common data class SPS (IEC 61850-7-3)   | Coding in IEC 61850-9-1                                                                                                                                           | Comment                                                                     |
|-----------------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Attribute name                          | Attribute type                          |                                                                                                                                                                   |                                                                             |
| stVal                                   | BOOLEAN                                 | -                                                                                                                                                                 | Not mapped                                                                  |
| grpVal                                  | BIT STRING                              | BS16 <0> = FALSE, OFF <1> = TRUE, ON                                                                                                                              | 16 individual status values. See Annex A                                    |
|                                         |                                         | BS16 <0> = VALID <1> = INVALID                                                                                                                                    | 16 individual quality indications related to the status values. See Annex A |
| q                                       | Quality                                 |                                                                                                                                                                   |                                                                             |
| validity (IV) detailQual                | CODED ENUM PACKED LIST                  | BS1 [0] <0> = VALID <1> = INVALID BS7 [1] = oscillatory (OS) [2] = failure, external error (EE) [3] = oldData (OD) [4] = inconsistent (IC) [5..7] = reserved (RE) | Further elements of detail- qual not mapped                                 |
| source test operatorBlocked             | CODED ENUM BOOLEAN BOOLEAN              | - - -                                                                                                                                                             | Not mapped Not mapped Not mapped                                            |
| SecondsSinceEpoch                       | INT32                                   | UI32                                                                                                                                                              |                                                                             |
| FractionOfSecond                        | INT24                                   | UI24                                                                                                                                                              |                                                                             |
| TimeQuality                             | TimeQuality                             |                                                                                                                                                                   |                                                                             |
| LeapSecondsKnown (LK)                   | BOOLEAN                                 | BS1 [0] <0> = FALSE <1> = TRUE                                                                                                                                    | SecondsSinceEpoch includes leap seconds                                     |
| ClockFailure (CF)                       | BOOLEAN                                 | BS1 [0] <0> = FALSE, <1> = TRUE,                                                                                                                                  | Time function is unreliable                                                 |
| ClockNotSynchronized (NS)               | BOOLEAN                                 | BS1 [1] <0> = FALSE,                                                                                                                                              | Clock is not synchronized to the reference source                           |
| TimeAccuracy                            | CODED ENUM                              | <1> = TRUE, UI5                                                                                                                                                   | Reserved                                                                    |

## Annex A

(normative)

## Definition of data set instances and related multicast sampled value control instances

## A.1 ASDU for universal data set

This data set is defined in IEC 60044-8, an overview is shown in Annex C.

Table A.1 - Predefined multicast sampled value control block instances relating to the transmission of the Universal Data Set according to IEC 60044-8

| MSVCB attribute   | Value                                                        |
|-------------------|--------------------------------------------------------------|
| MsvCBNam          | Implicit (IEC 60044-8)                                       |
| MsvCBRef          | Not visible                                                  |
| SvEna             | Enabled during the start up phase                            |
| MsvID             | Broadcast MAC address (optional multicast if configurable)   |
| DatSet            | <LDName> = UI16 = <FFFF H> or configurable                   |
|                   | <LNName>.<DataSetName> = <UI8>.<UI8> = <2>.< 1>              |
| ConfRev           | Preconfigured                                                |
| SmpRate           | Preconfigured                                                |
| OptFlds           | refresh-time=FALSE sample-synchronised=TRUE sample-rate=TRUE |

## A.2 ASDU for status indication data set

The status indication data set contains binary input status and quality information which will be transmitted periodically in the same way as the sampled analogue values. The intention is to give for example merging units or simpler devices the possibility to transmit binary input status indications, as a kind of distributed I/O mechanism based on the sampled value class model, to avoid the implementation of the reporting models specified in IEC 61850-7-2. Only one data set instance is permitted. This data set is related to the data name 'Ind' of the logical node GGIO.

<!-- image -->

IEC   815/03

Figure A.1 - Data set for status indication

## Table A.2 - Predefined multicast sampled value control block instances relating to the transmission of status indications

| MSVCB attribute   | Value                                                         |
|-------------------|---------------------------------------------------------------|
| MsvCBNam          | Implicit (Status indications )                                |
| MsvCBRef          | Not visible                                                   |
| SvEna             | Enabled during the start up phase.                            |
| MsvID             | Broadcast MAC address (optional multicast if configurable)    |
| DatSet            | <LDName> = UI16 = <FFFF H> or configurable                    |
| DatSet            | <LNName>.<DataSetName> = <UI8>.<UI8> = <2>.< 2>               |
| ConfRev           | Preconfigured                                                 |
| SmpRate           | Preconfigured                                                 |
| OptFlds           | refresh-time=FALSE sample-synchronised=FALSE sample-rate=TRUE |

## Annex B

(informative)

## Calculation of required bandwidth

The following tables can be used as a  guideline  for  the  selection  of  the  appropriate  physical layer related to the transmission of sampled analogue values.

Table B.1 - Selection guide for Ethernet physical layer (receiving node)

| Sampling rate   | Number of connected MUs   | Number of connected MUs   | Number of connected MUs   | Number of connected MUs   |                                      |
|-----------------|---------------------------|---------------------------|---------------------------|---------------------------|--------------------------------------|
| Sampling rate   | 1                         | 2                         | 3                         | 4-5                       |                                      |
| 10 × f r        | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   |                                      |
| 12 × f r        | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   |                                      |
| 16 × f r        | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   |                                      |
| 20 × f r        | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | Rated value according to IEC 60044-8 |
| 40 × f r        | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | 100 Mbps                  |                                      |
| 48 × f r        | 10 Mbps                   | 10 Mbps                   | 10 Mbps                   | 100 Mbps                  | Rated value according to IEC 60044-8 |
| 80 × f r        | 10 Mbps                   | 100 Mbps                  | 100 Mbps                  | 100 Mbps                  | Rated value according to IEC 60044-8 |
| 200 × f r       | 100 Mbps                  | 100 Mbps                  | 100 Mbps                  | 100 Mbps                  |                                      |

NOTE   Concerning 400 × f r : the available bandwidth of 100 Mbps Ethernet is not sufficient to allow three or more MUs transmit their samples to one receiving device.

Table B.2 - Selection guide for Ethernet physical layer (sending node)

| Sampling rate               | 1                           |                                      |
|-----------------------------|-----------------------------|--------------------------------------|
| 10 × f r                    | 10 Mbps                     |                                      |
| 12 × f r                    | 10 Mbps                     |                                      |
| 16 × f r                    | 10 Mbps                     |                                      |
| 20 × f r                    | 10 Mbps                     | Rated value according to IEC 60044-8 |
| 40 × f r                    | 10 Mbps                     |                                      |
| 48 × f r                    | 10 Mbps                     | Rated value according to IEC 60044-8 |
| 80 × f r                    | 10 Mbps                     | Rated value according to IEC 60044-8 |
| 200 × f r                   | 100 Mbps                    |                                      |
| f r : Rated frequency (Hz). | f r : Rated frequency (Hz). | f r : Rated frequency (Hz).          |

Available Data rate:

S R  × T L × n MU ≤ D R

D R : Data rate (10 Mbps or 100 Mbps).

S R : Sampling rate (Hz).

T L : Max. telegram length; (26 Byte Ethernet frame + 4 Byte Priority tagging + 8 Byte Ethertype PDU + 2 Byte ASN.1 tag/length + 2 Byte No. of blocks + 46 Byte universal data set + 23 Byte status indications = 111 Byte × 8 Bit = 888 Bit + 96 Bit interFrameGap = 984 Bit)

n MU : Number of connected MUs

EXAMPLE S R × T L × n MU  = (400 × 60 Hz) × 984 Bit × 1 = 23,616 Mbps ≤ 100 Mbps

NOTE   The  above  equation  to  determine  the  available  data  rate  is  theoretical  only.  In  practice,  it  should  be calculated with a reserve of approximately 10 %. In real applications, the available data rate depends normally on the CPU-power within the sender or receiver.

<!-- image -->

IEC   816/03

Figure B.1 - Ethernet Frame Format

## Annex C

(informative)

## Definitions of logical node instance names and data names related to the data sets

The  following tables show  the  relationship between  the  universal  data set  and  status indications  data  set  object  names  related  to  the  logical  node  and  data  classes  defined  in IEC 61850-7-4.

Table C.1 - Definitions of logical instance name and data names related to the universal data set

| Attribute      | Type           | Definition                                                                        |
|----------------|----------------|-----------------------------------------------------------------------------------|
| DataSetName    | INTEGER        | For the universal data set according to IEC 60044-8 the integer value is set to 1 |
| Data-Reference | See next table |                                                                                   |

| Logical node instance name   | Data name   | Common data class   | Definition according to IEC 60044-8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------|-------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| phsaTCTR                     | ARtg        | ASG                 | Rated phase current Defines the rated current in Ampere r.m.s.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| neutTCTR                     | ARtg        | ASG                 | Rated neutral current Defines the rated neutral current in Ampere r.m.s.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| phsaTVTR                     | VRtg        | ASG                 | Rated phase voltage Defines the rated voltage in 1/10 kV r.m.s.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                              | Tdr         | SAV                 | Rated delay time Defines the rated delay time in µ s. The rated delay time indicates the time between the instant a certain current/voltage is present at the primary terminals and the instant the transmission of the belonging digital data set starts. According to this standard, synchronisation pulses are used to synchronise several merging units. Therefore the rated delay time is not relevant for the ECT/EVT accuracy. The rated delay time value shall be high enough to allow reasonable antialiasing filters in the merging unit, but it shall not be so high that it significantly affects protection device performance. Therefore the rated delay time for this standard should be 3 000 µ s (tolerance band -100 % to +10 %) for all sampled rates. Tdr is not defined in IEC 61850-7-4. |
| phsaTCTR                     | Amp         | SAV                 | Current phase A, used for protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| phsbTCTR                     | Amp         | SAV                 | Current phase B, used for protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| phscTCTR                     | Amp         | SAV                 | Current phase C, used for protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| neutTCTR                     | Amp         | SAV                 | Current neutral                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| phsaTCTR1                    | Amp         | SAV                 | Current phase A; different scaling; used for measurement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| phsbTCTR1                    | Amp         | SAV                 | Current phase B; different scaling; used for measurement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| phscTCTR1                    | Amp         | SAV                 | Current phase C; different scaling; used for measurement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| phsaTVTR                     | Vol         | SAV                 | Voltage phase A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| phsbTVTR                     | Vol         | SAV                 | Voltage phase B                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| phscTVTR                     | Vol         | SAV                 | Voltage phase C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| neutTVTR                     | Vol         | SAV                 | Voltage neutral                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| bbTVTR                       | Vol         | SAV                 | Busbar Voltage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

| Logical node instance name   | Data name   | Common data class   | Definition according to IEC 60044-8                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|-------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LPHD                         | PhyHealth   | ISI                 | Merging unit maintenance required: This attribute is part of the first status word defined in IEC 60044-8. If the merging unit has failed, the maintenance required status shall be set. <0> = Maintenance not required <1> = Maintenance required The stVal attribute will be mapped to BIT STRING.                                                                                                                                                                                                     |
| LLN0                         | Mod         | ISC                 | Merging unit test status: This attribute is part of the first status word defined in IEC 60044-8. This status shall be set if the merging unit operates in test mode and calculates sampled values internally. <0> = Normal operation <1> = Test mode activated The stVal attribute will be mapped to BIT STRING.                                                                                                                                                                                        |
|                              | WkUpTim     | SPS                 | Wake up time indication: This attribute is part of the first status word defined in IEC 60044-8. Wake up time indication shall be set during a wake up time period respectively start up time period corresponding with the sampled value invalid indication. <0> = Normal operation <1> = Data not valid                                                                                                                                                                                                |
|                              | SynchMeth   | SPS                 | Synchronisation method: This attribute is part of the first status word defined in IEC 60044-8. The synchronisation method indicates whether the sampled values of the data set are suitable for interpolation or whether the data set values cannot be used with interpolation schemes. <0> = Data set values not to be used with interpolation schemes <1> = Data set values are suitable for interpolation; Not recommended for IEC 61850-9-1 applications SynchMeth is not defined in IEC 61850-7-4. |
|                              | NotSynch    | SPS                 | Merging Unit not synchronised: This attribute is part of the first status word defined in IEC 60044-8. If interpolation schemes are defined via the synchronisation method, the unsynchronised bit must be set. <0> = Time synchronisation activated and ready. <1> = Time synchronisation missing or invalid. NotSynch is not defined in IEC 61850-7-4.                                                                                                                                                 |
|                              | CTType      | SPS                 | Type of CT output: This attribute is part of the first status word defined in IEC 60044-8. Type of CT output shall be set to indicate the use of air core coils. <0> = i ( t ) <1> = d( i ( t ))/d t ; air core coils. CTType is not defined in IEC 61850-7-4.                                                                                                                                                                                                                                           |
|                              | Range Flag  | SPS                 | Range flag defines the scaling factor for the phase current data for protection applications. <0> = 01CF H (dynamic range 50 × I r ) <1> = 00E7 H (dynamic range 100 × I r ) RangeFlag is not defined in IEC 61850-7-4.                                                                                                                                                                                                                                                                                  |

## Table C.2 - Definitions of logical instance name and data names related to the status indication data set

| Attribute      | Type           | Definition                                                        |
|----------------|----------------|-------------------------------------------------------------------|
| DataSetName    | INTEGER        | For the status indication data set, the integer value is set to 2 |
| Data-Reference | See next table |                                                                   |

| Logical node name   | Data name   | Common data class   | Definition                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------|-------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GGIO                | Ind         | SPS                 | Binary Status Indication: Individual binary status inputs and related quality status indications. Quality bit for each status point gives the sending unit (i.e. the merging unit) the ability to tag the specific bits as invalid to indicate unused or disabled status points to the receiving IED. Binary status input: <0> FALSE, OFF <1> TRUE, ON Quality Indication: <0> VALID <1> INVALID |

<!-- image -->

|                           | 2 7   | 2 6   | 2                                        | 5                                        | 2 3                                      | 2 2                                      | 2 1                                      | 2 0   |
|---------------------------|-------|-------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|-------|
| ASDU Header               | msb   | msb   | Length of ASDU ( = 44)                   | Length of ASDU ( = 44)                   | Length of ASDU ( = 44)                   | Length of ASDU ( = 44)                   | Length of ASDU ( = 44)                   |       |
|                           | msb   |       | LNName ( =02)                            | LNName ( =02)                            | LNName ( =02)                            | LNName ( =02)                            | LNName ( =02)                            | lsb   |
|                           | msb   |       | DataSetName (=01)                        | DataSetName (=01)                        | DataSetName (=01)                        | DataSetName (=01)                        | DataSetName (=01)                        | lsb   |
|                           | msb   |       | LDName                                   | LDName                                   | LDName                                   | LDName                                   | LDName                                   |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Rated Phase Current                      | Rated Phase Current                      | Rated Phase Current                      | Rated Phase Current                      | Rated Phase Current                      |       |
|                           | msb   |       | Rated Neutral Current                    | Rated Neutral Current                    | Rated Neutral Current                    | Rated Neutral Current                    | Rated Neutral Current                    |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Rated Phase Voltage                      | Rated Phase Voltage                      | Rated Phase Voltage                      | Rated Phase Voltage                      | Rated Phase Voltage                      |       |
|                           | msb   |       | Rated Delay Time                         | Rated Delay Time                         | Rated Delay Time                         | Rated Delay Time                         | Rated Delay Time                         |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
| ASDU (universal data set) | msb   |       | Current Phase A, prot.                   | Current Phase A, prot.                   | Current Phase A, prot.                   | Current Phase A, prot.                   | Current Phase A, prot.                   | lsb   |
|                           | msb   |       | Current Phase B, prot.                   | Current Phase B, prot.                   | Current Phase B, prot.                   | Current Phase B, prot.                   | Current Phase B, prot.                   |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Current Phase C, prot.                   | Current Phase C, prot.                   | Current Phase C, prot.                   | Current Phase C, prot.                   | Current Phase C, prot.                   |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       |                                          |                                          |                                          |                                          |                                          |       |
|                           |       |       | Current Neutral                          | Current Neutral                          | Current Neutral                          | Current Neutral                          | Current Neutral                          |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Current Phase A, mes.                    | Current Phase A, mes.                    | Current Phase A, mes.                    | Current Phase A, mes.                    | Current Phase A, mes.                    |       |
|                           | msb   |       | Current Phase B, mes.                    | Current Phase B, mes.                    | Current Phase B, mes.                    | Current Phase B, mes.                    | Current Phase B, mes.                    |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Current Phase C, mes.                    | Current Phase C, mes.                    | Current Phase C, mes.                    | Current Phase C, mes.                    | Current Phase C, mes.                    |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Voltage Phase A                          | Voltage Phase A                          | Voltage Phase A                          | Voltage Phase A                          | Voltage Phase A                          |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Voltage Phase B                          | Voltage Phase B                          | Voltage Phase B                          | Voltage Phase B                          | Voltage Phase B                          |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Voltage Phase C                          | Voltage Phase C                          | Voltage Phase C                          | Voltage Phase C                          | Voltage Phase C                          |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Voltage Neutral                          | Voltage Neutral                          | Voltage Neutral                          | Voltage Neutral                          | Voltage Neutral                          |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Busbar Voltage                           | Busbar Voltage                           | Busbar Voltage                           | Busbar Voltage                           | Busbar Voltage                           |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | StatusWord#1                             | StatusWord#1                             | StatusWord#1                             | StatusWord#1                             | StatusWord#1                             |       |
|                           | msb   |       |                                          |                                          |                                          |                                          |                                          |       |
|                           |       |       | StatusWord#2                             | StatusWord#2                             | StatusWord#2                             | StatusWord#2                             | StatusWord#2                             | lsb   |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Sample Counter                           | Sample Counter                           | Sample Counter                           | Sample Counter                           | Sample Counter                           |       |
|                           |       |       |                                          |                                          |                                          |                                          |                                          | lsb   |
|                           | msb   |       | Sampling rate Configuration revision no. | Sampling rate Configuration revision no. | Sampling rate Configuration revision no. | Sampling rate Configuration revision no. | Sampling rate Configuration revision no. | lsb   |

IEC   817/03

Figure C.1 - Contents of the universal data set based on the specification in IEC 60044-8

## Annex D

(informative)

## Electronic transformers block diagram and configuration example

## D.1 General block diagram of electronic transformers

Figure  D.1  is  a  general  block  diagram  of  an  electronic  transformer.  Depending  on  the application, not all  of  the  illustrated  blocks  may  be  included  in  the  transformers  (see IEC 60044-8).

Figure D.1 - Example for general block diagram of a single-phase electronic transformer

<!-- image -->

IEC   818/03

## D.2 General block diagram of electronic transformers with a digital output and the merging unit

Up  to  seven  current  transformers  and  up  to  five  voltage  transformers  are  grouped  together using  a  merging  unit  (MU).  This  merging  unit  supplies  the  secondary  equipment  with  a  timecoherent set of current and voltage data.

Figure D.2 gives the maximum configuration.

<!-- image -->

Figure D.2 - Example for electronic transformers configuration

NOTE   SC  of  EVTa  is  the  secondary  converter  of  the  electronic  voltage  transformers  of  phase a  (see IEC 60044-7).  SC  of  ECTa  is  the  secondary  converter  of  the  electronic  current  transformers  of  phase a (see IEC 60044-8).

The  implementation of the merging  unit as a standalone device is not  a  mandatory requirement. It may be part of the ECT or EVT electronics.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<!-- image -->

## Standards Survey

The IEC would like to offer you the best quality standards possible. To make sure that we continue to meet your needs, your feedback is essential. Would you please take a minute to answer the questions overleaf and fax them to us at +41 22 919 03 00 or mail them to the address below. Thank you!

Customer Service Centre (CSC)

## International Electrotechnical Commission

3, rue de Varembé 1211 Genève 20 Switzerland or

Fax to: IEC /CSC at +41 22 919 03 00

Thank you for your contribution to the standards-making process.

<!-- image -->

## RÉPONSE P A YÉE SUISSE

Customer Service Centre (CSC) International Electrotechnical Commission

3,  r ue de Varembé 1211   G ENEVA 20 Sw i tz erl and

Nicht frank i er en N e  pas affra nchir

<!-- image -->

N on aff r ancare No   st am p  r equi red

Q1 Please report on ONE STANDARD and ONE STANDARD ONLY . Enter the exact number of the standard: (e.g. 60601-1-1) ............................................................. Q6

Q2 Please tell us in what capacity(ies) you bought the standard (tick all that apply). I am the/a:

purchasing agent /G52 librarian /G52 researcher /G52 design engineer /G52 safety engineer /G52 testing engineer /G52 marketing specialist /G52 other.....................................................

Q3 I work for/in/as a:

## (tick all that apply)

manufacturing /G52 consultant /G52 government /G52 test/certification facility /G52 public utility /G52 education /G52 military /G52 other.....................................................

Q4 This standard will be used for: (tick all that apply)

general reference /G52 product research /G52 product design/development /G52 specifications /G52 tenders /G52 quality assessment /G52 certification /G52 technical documentation /G52 thesis /G52 manufacturing /G52 other..................................................... Q9

Q5 This standard meets my needs: (tick one)

not at all /G52 nearly /G52 fairly well /G52 exactly

Q7 Please assess the standard in the following categories, using the numbers: (1) unacceptable, (2) below average, (3) average, (4) above average, (5) exceptional, (6) not applicable

Q8 I read/use the: (tick one)

French text only /G52 English text only /G52 both English and French texts

/G52

Please share any comment on any aspect of the IEC that you would like us to know:

/G52

If you ticked NOT AT ALL in Question 5 the reason is: (tick all that apply) standard is out of date /G52 standard is incomplete /G52 standard is too academic /G52 standard is too superficial /G52 title is misleading /G52 I made the wrong choice /G52 other ..............................................

timeliness......................................... quality of writing.................................. technical contents................................. logic of arrangement of contents .......... tables, charts, graphs, figures............... other ..............................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

...................................................

<!-- image -->