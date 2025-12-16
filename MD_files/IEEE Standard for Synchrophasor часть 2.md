<!-- image -->

## IEEE Std 90003™-2008 IEEE Std 90003™-2008 IEEE Standard for Synchrophasor Data Transfer for Power Systems

## IEEE Power &amp; Energy Society

Sponsored by the Power System Relaying Committee

IEEE 3 Park Avenue New York, NY 10016-5997 USA

28 December 2011

IEEE Std C37.118.2™-2011

(Revision of IEEE Std C37.118™-2005)

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Sponsor

## Power System Relaying Committee of the IEEE Power &amp; Energy Society

## Approved 7 December 2011

## IEEE-SA Standards Board

Abstract: A method for real-time exchange of synchronized phasor measurement data between power system equipment is defined. This standard specifies messaging that can be used with any suitable communication protocol for real-time communication between phasor measurement units (PMU),  phasor  data  concentrators  (PDC),  and  other  applications.  It  defines  message  types, contents,  and  use.  Data  types  and  formats  are  specified.  A  typical  measurement  system  is described. Communication options and requirements are described in annexes.

Keywords: data  concentrator,  DC,  IEEE  C37.118.2,  PDC,  phasor,  phasor  data  concentrator, phasor measurement unit, PMU, synchronized phasor, synchrophasor

•

The Institute of Electrical and Electronics Engineers, Inc.

3 Park Avenue, New York, NY 10016-5997, USA

Copyright © 2011 by the Institute of Electrical and Electronics Engineers, Inc.

All rights reserved. Published 28 December 2011. Printed in the United States of America.

IEEE is a registered trademark in the U.S. Patent &amp; Trademark Office, owned by the Institute of Electrical and Electronics Engineers, Incorporated.

PDF:

ISBN 978-0-7381-6813-5

STD97168

Print:

ISBN 978-0-7381-6814-2 STDPD97168

IEEE prohibits discrimination, harassment and bullying. For more information, visit http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html. No part of this publication may be reproduced in any form, in an electronic retrieval system or otherwise, without the prior written permission of the publisher.

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the  IEEE Standards Association (IEEE-SA) Standards Board. The IEEE develops its standards through a consensus development  process,  approved  by  the  American  National  Standards  Institute,  which  brings  together  volunteers representing varied viewpoints and interests to achieve the final product. Volunteers are not necessarily members of the Institute  and  serve  without  compensation.  While  the  IEEE  administers  the  process  and  establishes  rules  to  promote fairness in the consensus development process, the IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the soundness of any judgments contained in its standards.

Use of an IEEE Standard is wholly voluntary. The IEEE disclaims liability for any personal injury, property or other damage,  of  any  nature  whatsoever,  whether  special,  indirect,  consequential,  or  compensatory,  directly  or  indirectly resulting from the publication, use of, or reliance upon this, or any other IEEE Standard document.

The  IEEE  does  not  warrant  or  represent  the  accuracy  or  content  of  the  material  contained  herein,  and  expressly disclaims any express or implied warranty, including any implied warranty of merchantability or fitness for a specific purpose, or that the use of the material contained herein is free from patent infringement. IEEE Standards documents are supplied ' AS IS .'

The existence of an IEEE Standard does not imply that there are no other ways to produce, test, measure, purchase, market, or provide other goods and services related to the scope of the IEEE Standard. Furthermore, the viewpoint expressed at the time a standard is approved and issued is subject to change brought about through developments in the state of the art and comments received from users of the standard. Every IEEE Standard is subjected to review at least every five years for revision or reaffirmation, or every ten years for stabilization. When a document is more than five years  old  and  has  not  been  reaffirmed,  or  more  than  ten  years  old  and  has  not  been  stabilized,  it  is  reasonable  to conclude that its  contents,  although  still  of  some  value,  do  not  wholly  reflect  the  present  state  of  the  art.  Users  are cautioned to check to determine that they have the latest edition of any IEEE Standard.

In  publishing  and  making  this  document  available,  the  IEEE  is  not  suggesting  or  rendering  professional  or  other services for, or on behalf of, any person or entity. Nor is the IEEE undertaking to perform any duty owed by any other person or entity to another. Any person utilizing this, and any other IEEE Standards document, should rely upon his or her independent judgment in the exercise of reasonable care in any given circumstances or, as appropriate, seek the advice of a competent professional in determining the appropriateness of a given IEEE standard.

Interpretations:  Occasionally  questions  may  arise  regarding  the  meaning  of  portions  of  standards  as  they  relate  to specific applications. When the need for interpretations is brought to the attention of IEEE, the Institute will initiate action  to  prepare  appropriate  responses.  Since  IEEE  Standards  represent  a  consensus  of  concerned  interests,  it  is important to ensure that any interpretation has also received the concurrence of a balance of interests. For this reason, IEEE  and  the  members  of  its  societies  and  Standards  Coordinating  Committees  are  not  able  to  provide  an  instant response to interpretation requests except in those cases where the matter has previously received formal consideration. A statement, written or oral, that is not processed in accordance with the IEEE-SA Standards Board Operations Manual shall not be considered the official position of IEEE or any of its committees and shall not be considered to be, nor be relied  upon  as,  a  formal  interpretation  of  the  IEEE.  At  lectures,  symposia,  seminars,  or  educational  courses,  an individual presenting information on IEEE standards shall make it clear that his or her views should be considered the personal views of that individual rather than the formal position, explanation, or interpretation of the IEEE.

Comments for revision of IEEE Standards are welcome from any interested party, regardless of membership affiliation with IEEE. Suggestions for changes in documents should be in the form of a proposed change of text, together with appropriate  supporting  comments.  Recommendations  to  change  the  status  of  a  stabilized  standard  should  include  a rationale as to why a revision or withdrawal is required. Comments and recommendations on standards, and requests for interpretations should be addressed to:

Secretary, IEEE-SA Standards Board 445 Hoes Lane Piscataway, NJ 08854 USA

Authorization to photocopy portions of any individual standard for internal or personal use is granted by The Institute of Electrical and Electronics Engineers, Inc., provided that the appropriate fee is paid to Copyright Clearance Center. To arrange for payment of licensing fee, please contact Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978 750 8400. Permission to photocopy portions of any individual standard for educational classroom use can also be obtained through the Copyright Clearance Center.

## Introduction

This introduction is not part of IEEE Std C37.118.2-2011, IEEE Standard for Synchrophasor Data Transfer for Power Systems.

Digital  computer based measurement, protection, and control systems have become common features of electric power systems. These measurement, protection, and control systems use sampled data to compute various  quantities  such  as  voltage  and  current  phasors.  Phasors  are  used  in  many  protection  and  data acquisition functions, and their utility is increased further by referencing them to a common time base. This can be accomplished by synchronizing the phasor estimate to a precise time source that is common to the various  measuring  sites.  Phasor  estimates  synchronized  to  a  common  time  source  and  referenced  to  a common nominal frequency are defined as synchrophasors. Simultaneous measurement sets derived from synchronized phasors provide a vastly improved method for tracking power system dynamic phenomena for improved power system monitoring, protection, operation, and control.

The original standard for synchrophasors was IEEE Std 1344™-1995 [B3], which was reaffirmed in 2001. a This standard was replaced in 2005 by IEEE Std C37.118™-2005 [B6]. IEEE Std C37.118-2005 provided additional  clarification  for  the  phasor  and  synchronized  phasor  definitions.  The  concepts  of  total  vector error and compliance tests were introduced. The message formats were updated from the original standard to improve information exchange with other systems such as a master station. Specifically, the sync, frame size, and station identification fields were added to the data frame, configuration frame, header frame, and command  frame.  Analog  data  was  added  to  the  data  frame,  the  fraction-of-second  (FRACSEC)  field replaced the sample count field, and the status field was significantly modified to include time quality.

The  2005  version  of  IEEE  Std  C37.118  included  both  measurement  requirements  and  real-time  data transfer  requirements.  To  simplify  widespread  adoption  and  facilitate  the  use  of  other  communication protocols for phasor data transfer, IEEE  Std C37.118-2005  [B6] was split into two standards: IEEE Std C37.118.1™ for synchrophasor measurement requirements including dynamic performance, and IEEE  Std  C37.118.2-2011  (this  standard)  with  synchrophasor  data  transfer  requirements. b The  previous requirements for data transfer are retained, and one new configuration frame has been added.

## Notice to users

## Laws and regulations

Users  of  these  documents  should  consult  all  applicable  laws  and  regulations.  Compliance  with  the provisions  of  this  standard  does  not  imply  compliance  to  any  applicable  regulatory  requirements. Implementers  of  the  standard  are  responsible  for  observing  or  referring  to  the  applicable  regulatory requirements.  IEEE  does  not,  by  the  publication  of  its  standards,  intend  to  urge  action  that  is  not  in compliance with applicable laws, and these documents may not be construed as doing so.

a The numbers in brackets correspond to those of the bibliography in Annex A.

b Information on references can be found in Clause 2.

## Copyrights

This  document  is  copyrighted  by  the  IEEE.  It  is  made  available  for  a  wide  variety  of  both  public  and private  uses.  These  include  both  use,  by  reference,  in  laws  and  regulations,  and  use  in  private  selfregulation,  standardization,  and  the  promotion  of  engineering  practices  and  methods.  By  making  this document available for use and adoption by public authorities and private users, the IEEE does not waive any rights in copyright to this document.

## Updating of IEEE documents

Users  of  IEEE  standards  should  be  aware  that  these  documents  may  be  superseded  at  any  time  by  the issuance  of  new  editions  or  may  be  amended  from  time  to  time  through  the  issuance  of  amendments, corrigenda, or errata. An official IEEE document at any point in time consists of the current edition of the document together with any amendments, corrigenda, or errata then in effect. In order to determine whether a  given  document  is  the  current  edition  and  whether  it  has  been  amended  through  the  issuance  of amendments, corrigenda, or errata, visit the IEEE Standards Association web site at http://ieeexplore.ieee.org/xpl/standards.jsp, or contact the IEEE at the address listed previously.

For more information about the IEEE Standards Association or the IEEE standards development process, visit the IEEE-SA web site at http://standards.ieee.org.

## Errata

Errata, if any, for this and all other standards can be accessed at the following URL: http://standards.ieee.org/findstds/errata/index.html.  Users  are  encouraged  to  check  this  URL  for  errata periodically.

## Interpretations

Current interpretations can be accessed at the following URL: http://standards.ieee.org/findstds/interps/index.html.

## Patents

Attention is called to the possibility that implementation of this standard may require use of subject matter covered by patent rights. By publication of this standard, no position is taken with respect to the existence or  validity  of  any  patent  rights  in  connection  therewith.  The  IEEE  is  not  responsible  for  identifying Essential Patent Claims for which a license may be required, for conducting inquiries into the legal validity or  scope  of  Patents  Claims  or  determining  whether  any  licensing  terms  or  conditions  provided  in connection with submission of a Letter of Assurance, if any, or in any licensing agreements are reasonable or non-discriminatory. Users of this standard are expressly advised that determination of the validity of any patent  rights,  and  the  risk  of  infringement  of  such  rights,  is  entirely  their  own  responsibility.  Further information may be obtained from the IEEE Standards Association.

## Participants

At the time this standard was submitted to the IEEE-SA Standards Board for approval, the Synchrophasor Data Transfer for Power Systems Working Group had the following membership:

## Kenneth Martin , Chair Gustavo Brunello , Vice Chair

Mark Adamiak

Galina Antonova

Gabriel Benmouyal

Christoph Brunner

Phuoc-Doc Bui

Herbert Falk

Allen Goldstein Yi Hu Takahiro Kase Mladen Kezunovic Yuchen Lu Rene Midence Jay Murphy

Farnoosh Rahmatian Veselin Skendzic Fred Steinhauser Tim Tibbals Benton Vandiver Abu Zahid

The following members of the individual balloting committee voted on this standard. Balloters may have voted for approval, disapproval, or abstention.

William J. Ackerman Mark Adamiak Eric Allen M. Victoria Alonso Galina Antonova James Ariza Jack Arnold Ali Al Awazi Munnu Bajpai David Bassett Philip Beaumont Kenneth Behrendt Oscar Bolado Gustavo Brunello Arvind K. Chaudhary Luis Coronado Randall Crellin Gary Donner Michael Dood Randall Dotson Gary Engmann Herbert Falk Vasudev S. Gharpure Jeffrey Gilbert Jalal Gohari Allen Goldstein Roman Graf Stephen Grier

Randall C. Groves Roger Hedding C. Huntley Gerald Johnson Innocent Kamwa Yuri Khersonsky James Kinney Stanley Klein Joseph L. Koepfinger Jim Kulchisky Chung-Yiu Lam Raluca Lascu Amir Makki Kenneth Martin Pierre Martin John McDonald Michael McDonald Harish Mehta Gary Michel Adi Mulawarman Jerry Murphy R. Murphy Bruce Muschlitz Michael S. Newman Lorraine Padden Donald Parker Mark Peterson

Robert Pettigrew Bruce Pickett Farnoosh Rahmatian Michael Roberts Charles Rogers Steven Sano Bartien Sayogo Thomas Schossig Robert Seitz Jose Antonio De La O Serna Gil Shultz Mark Simon Veselin Skendzic James Smith Jerry Smith Gary Stoedter Charles Sufana William Taylor Demetrios Tziouvaras Joe Uchiyama Eric Udren John Vergis Roel Vries John Wang Solveig Ward Ray Young Jian Yu Sergio Zimath

When the IEEE-SA Standards Board approved this standard on 7 December 2011, it had the following membership:

Richard H. Hulett ,

Chair

John Kulick ,

Vice Chair

Robert M. Grow

, Past Chair

Judith Gorman ,

Secretary

Joseph L. Koepfinger*

Jim Hughes David J. Law Thomas Lee Hung Ling Oleg Logvinov Ted Olsen

Masayuki Ariyoshi William Bartley Ted Burse Clint Chaplin Wael Diab Jean-Philippe Faure Alexander Gelman Paul Houzé

*Member Emeritus

Also included are the following nonvoting IEEE-SA Standards Board liaisons:

Satish K. Aggarwal, NRC Representative Richard DeBlasio, DOE Representative Michael Janezic, NIST Representative

Lisa Perry IEEE Standards Program Manager, Document Development

Soo H. Kim IEEE Standards Project Manager

Gary Robinson Jon Walter Rosdahl Sam Sciacca Mike Seavey Curtis Siller Phil Winston Howard L. Wolfman Don Wright

## Contents

| 1. Overview                                                                                                                                                                                                                                                                                                        | 1                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| .................................................................................................................................................... 1.1 Scope ................................................................................................................................................... | 1                                                                                                                                           |
| 1.2 Purpose ................................................................................................................................................                                                                                                                                                       | 1                                                                                                                                           |
| 1.3 General overview.................................................................................................................................                                                                                                                                                              | 2                                                                                                                                           |
| 1.4 Need for this standard..........................................................................................................................                                                                                                                                                               | 2                                                                                                                                           |
| 2. Normative references..................................................................................................................................                                                                                                                                                          | 3                                                                                                                                           |
| 3. Definitions, acronyms, and abbreviations ..................................................................................................                                                                                                                                                                     | 3                                                                                                                                           |
| 3.1 Definitions ...........................................................................................................................................                                                                                                                                                        | 3                                                                                                                                           |
| 3.2 Special terms........................................................................................................................................                                                                                                                                                          | 4                                                                                                                                           |
| 3.3 Abbreviations and acronyms ...............................................................................................................                                                                                                                                                                     | 4                                                                                                                                           |
| 4. Synchrophasor measurement......................................................................................................................                                                                                                                                                                 | 4                                                                                                                                           |
| 4.1 Introduction                                                                                                                                                                                                                                                                                                   | ......................................................................................................................................... 4 |
| 4.2 Synchrophasor definition.....................................................................................................................                                                                                                                                                                  | 5                                                                                                                                           |
| 4.3 Frequency and rate of change of frequency definition ........................................................................                                                                                                                                                                                  | 6                                                                                                                                           |
| 4.4 Measurement time tag from synchrophasors .......................................................................................                                                                                                                                                                               | 6                                                                                                                                           |
| 4.5 System time synchronization...............................................................................................................                                                                                                                                                                     | 6                                                                                                                                           |
| 4.6 Synchrophasor transmission ................................................................................................................                                                                                                                                                                    | 7                                                                                                                                           |
| 4.7 Synchrophasor measurement...............................................................................................................                                                                                                                                                                       | 7                                                                                                                                           |
| 5. Synchrophasor measurement system overview..........................................................................................                                                                                                                                                                             | 7                                                                                                                                           |
| 5.1 Synchrophasor network .......................................................................................................................                                                                                                                                                                  | 7                                                                                                                                           |
| 5.2 Synchrophasor network elements ........................................................................................................                                                                                                                                                                        | 8                                                                                                                                           |
| 5.3 Multiple data streams from PMUs and PDCs......................................................................................                                                                                                                                                                                 | 9                                                                                                                                           |
| 6. Synchrophasor message format..................................................................................................................                                                                                                                                                                  | 9                                                                                                                                           |
| 6.1 Message application ............................................................................................................................                                                                                                                                                               | 9                                                                                                                                           |
| 6.2 Message framework.............................................................................................................................                                                                                                                                                                 | 9                                                                                                                                           |
| 6.3 Data frame .........................................................................................................................................                                                                                                                                                           | 13                                                                                                                                          |
| 6.4 Configuration frame ..........................................................................................................................                                                                                                                                                                 | 17                                                                                                                                          |
| 6.5 Header frame .....................................................................................................................................                                                                                                                                                             | 24                                                                                                                                          |
| 6.6 Command frame ................................................................................................................................                                                                                                                                                                 | 25                                                                                                                                          |
| Annex A (informative) Bibliography ...........................................................................................................                                                                                                                                                                     | 27                                                                                                                                          |
| Annex B (informative) Cyclic redundancy codes.........................................................................................                                                                                                                                                                             | 28                                                                                                                                          |
| Annex C (informative) System communications considerations..................................................................                                                                                                                                                                                       | 31                                                                                                                                          |
| Annex D (informative) Message examples ..................................................................................................                                                                                                                                                                          | 33                                                                                                                                          |
| Annex E (normative) Synchrophasor message mapping into communications............................................                                                                                                                                                                                                  | 39                                                                                                                                          |
| Annex F (informative) Synchrophasor communication methods for IP.......................................................                                                                                                                                                                                            | 41                                                                                                                                          |

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

IMPORTANT  NOTICE:  This  standard  is  not  intended to ensure safety, security, health, or environmental  protection.  Implementers  of  the  standard  are  responsible  for  determining  appropriate safety, security, environmental, and health practices or regulatory requirements.

This  IEEE  document  is  made  available  for  use  subject  to  important  notices  and  legal  disclaimers. These notices and disclaimers appear in all publications containing this document  and  may be found under the heading 'Important Notice' or 'Important Notices and Disclaimers Concerning  IEEE  Documents.'  They  can  also  be  obtained  on  request  from  IEEE  or  viewed  at http://standards.ieee.org/IPR/disclaimers.html.

## 1. Overview

## 1.1 Scope

This  standard  defines  a  method  for  exchange  of  synchronized  phasor  measurement  data  between  power system  equipment.  It  specifies  messaging  including  types,  use,  contents,  and  data  formats  for  real-time communication between phasor measurement units (PMU), phasor data concentrators (PDC), and other applications.

## 1.2 Purpose

The  purpose  for  this  standard  is  to  facilitate  data  exchange  among  measurement,  data  collection,  and application  equipment.  It  provides  a  defined,  open  access  method  for  all  vendors  to  use  to  facilitate development and use of synchrophasors. It is a simple and direct method of data transmission and accretion within a phasor measurement system, which may be used directly or with other communication protocols. This method was initially established by IEEE Std C37.118™-2005 [B6]. 1

1 The numbers in brackets correspond to those of the bibliography in Annex A.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## 1.3 General overview

This  standard  defines  data  transmission  formats  for  real-time  data  reporting  for  synchronized  phasor measurements used in electric power systems.

- Clause 1 provides the scope and need for the standard.
- Clause 2 references other standards that are related or may be useful in the study and application of this standard.
- Clause 3 defines terms, acronyms, and abbreviations found in this standard.
- Clause 4 provides background for synchrophasor measurement.
- Clause 5 describes synchrophasor measurement system.
- Clause 6 defines the real-time communication protocol and message formats.

Six informative annexes are provided to clarify the standard and give supporting information:

- Annex A is a bibliography.
- Annex  B  gives  information  about  cyclic  redundancy  codes  and  the  cyclic  redundancy  check (CRC) required by this standard.
- Annex C provides background in communication bandwidth.
- Annex D illustrates the message formats defined in Clause 6 with complete message examples.
- Annex E defines message mapping into standard communication protocols.
- Annex F discusses synchrophasor communications methods for Internet Protocol (IP).

## 1.4 Need for this standard

The 2005 version of IEEE Std C37.118 includes both measurement requirements and real-time data transfer requirements. To simplify widespread adoption of synchrophasor measurement technology and facilitate the use of other communication protocols for phasor data transmission, IEEE Std C37.118-2005 [B6] was split  into  two  standards,  one  with  measurement  requirements  and  the  other  with  the  data  transfer requirements. This allows other communication protocols and systems to be used with phasor measurement systems supporting the original purpose of the standard. This split facilitates harmonization of IEEE  Std  C37.118-2005  with  IEC  61850.  This  standard  includes  only  the  data  transfer  portion  of IEEE Std C37.118-2005, adding some corrections and improvements yet retaining the current messaging for  backward compatibility.  This  approach  supports  the  widely  used  method  for  current  and  developing deployments, and allows for a smooth transition of synchrophasor systems to new protocols as needed.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## 2. Normative references

The following referenced documents are indispensable for the application of this document (i.e., they must be understood and used, so each referenced document is cited in text and its relationship to this document is explained). For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments or corrigenda) applies.

IEEE Std 754™-1985, IEEE Standard for Binary Floating-Point Arithmetic. 2, 3

IEEE Std C37.118.1™, IEEE Standard for Synchrophasor Measurements for Power Systems.

## 3. Definitions, acronyms, and abbreviations

## 3.1 Definitions

For  the  purposes  of  this  document,  the  following  terms  and  definitions  apply. The IEEE  Standards Dictionary: Glossary of Terms &amp; Definitions [B1] should be consulted for terms not defined in this clause. 4

Coordinated Universal Time (UTC): (Initials are ordered based on French language.) The time of day at the  Earth's  prime  meridian  (0°  longitude).  It  is  distributed  by  various  media,  including  the  Global Positioning System (GPS) system.

CRC-CCITT: 16-bit  cyclic  redundancy  check  (CRC)  calculated  using  the  generating  polynomial X 16 + X 12 + X 5 + 1, seed value 0xFFFF (-1), no final mask.

data concentrator (DC) : A device that combines data from several measurement devices.

Global Positioning System (GPS): A U.S. Department of Defense (DoD) navigation system that uses a constellation of 24 satellites broadcasting a precision signal for location and time synchronization. Basic time synchronization accuracy is ± 0.2 microseconds ( μ s).

IEEE floating point: A 32-bit representation of a real number.

NOTE-This definition is in accordance with IEEE Std 754-1985. 5, 6

phasor: A complex equivalent of a sinusoidal wave quantity such that the complex modulus is the cosine wave amplitude and the complex angle (in polar form) is the cosine wave phase angle.

phasor data concentrator (PDC): A data concentrator (DC) used in phasor measurement systems.

2 IEEE publications are available from the Institute of Electrical and Electronics Engineers, 445 Hoes Lane, Piscataway, NJ 08854, USA (http://standards.ieee.org).

3 The IEEE standards or products referred to in Clause 2 are trademarks owned by the Institute of Electrical and Electronics Engineers, Incorporated.

4 The IEEE Standards Dictionary: Glossary of Terms &amp; Definitions is available at http://shop.ieee.org/.

5 Information on references can be found in Clause 2.

6 Notes in text, tables, and figures of a standard are given for information only and do not contain requirements needed to implement this standard.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

synchronism: The  state  in  which  connected  alternating-current  systems,  machines,  or  a  combination operate at the same frequency, and in which the phase angle displacements between voltages in them are constant, or vary about a steady and stable average value.

synchronized phasor or synchrophasor: A  phasor  calculated  from  data  samples  using  a  standard time signal as the reference for the measurement.

NOTE-In this standard, the phasors from remote sites have a defined common phase relationship.

## 3.2 Special terms

phasor  measurement  unit  (PMU): In  this  standard,  a  device  that  produces  synchronized  phasor, frequency, and rate of change of frequency (ROCOF) estimates from voltage and/or current signals and a time  synchronizing  signal.  Note  that  the  same  device  may  perform  other  functions  and  include  another functional name [e.g., the device may also record power system waveforms and be called a digital fault recorder (DFR)].

## 3.3 Abbreviations and acronyms

| BCD    | binary coded decimal                                                        |
|--------|-----------------------------------------------------------------------------|
| IRIG-B | InterRange Instrumentation Group Time Code Format B                         |
| MMS    | manufacturing messaging specification                                       |
| NTP    | Network Time Protocol                                                       |
| PPS    | pulse per second                                                            |
| PTP    | Precision Time Protocol                                                     |
| ROCOF  | rate of change of frequency, as defined by IEEE Std C37.118.1               |
| SCADA  | Supervisory Control and Data Acquisition                                    |
| SOC    | second of century                                                           |
| UTF-8  | Unicode character encoding scheme used to represent text in writing systems |

## 4. Synchrophasor measurement

## 4.1 Introduction

Synchrophasor measurement definitions, detailed descriptions, and performance requirements are spelled out in the IEEE Std C37.118.1. That standard is based on the original performance requirements from IEEE Std C37.118-2005 [B6]. It extends them with dynamic performance requirements for synchrophasors and steady-state  and  dynamic  performance  requirements  for  frequency  and  rate  of  change  of  frequency (ROCOF)  measurements.  This  clause  includes  the  basic  synchrophasor  measurement  definition  from

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

IEEE Std C37.118.1 for background and clarity, and the requirements for synchronization and data rates, which are important for the transfer of these measurements.

## 4.2 Synchrophasor definition

Phasor representation of sinusoidal signals is commonly used in ac power system analysis. The sinusoidal waveform defined as shown in Equation (1):

<!-- formula-not-decoded -->

is commonly represented as the phasor shown in Equation (2):

<!-- formula-not-decoded -->

where the magnitude is the rms value, X m / √ 2, of the waveform and the subscripts r and i signify real and imaginary parts of a complex value in rectangular components. The value of φ depends on the time scale, particularly  where t =  0.  It  is  important  to  note  this  phasor  is  defined  for  the  angular  frequency ω ; evaluations with other phasors must be done with the same time scale and frequency.

The synchrophasor representation of the signal x ( t ) in Equation (1) is the value X in Equation (2) where φ is the instantaneous phase angle relative to a cosine function at the nominal system frequency synchronized to UTC.

Under this definition, φ is the offset from a cosine function at the nominal system frequency synchronized to UTC. A cosine has a maximum at t = 0, so the synchrophasor angle is 0 degrees when the maximum of x ( t )  occurs  at  the  UTC  second  rollover  (1  PPS  time  signal),  and  -90  degrees  when  the  positive  zero crossing occurs at the UTC second rollover (sin waveform). Figure 1 illustrates the phase angle/UTC time relationship.

See IEEE Std C37.118.1 for details about synchrophasor definitions and measurements.

Figure 1  -Convention for synchrophasor representation

<!-- image -->

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## 4.3 Frequency and rate of change of frequency definition

A PMU shall be capable of reporting frequency and ROCOF. For this measurement, the following standard definitions shall be used. Given a sinusoidal signal as shown in Equation (3):

<!-- formula-not-decoded -->

Frequency is defined by Equation (4):

<!-- formula-not-decoded -->

The ROCOF is defined as shown in Equation (5):

<!-- formula-not-decoded -->

See IEEE Std C37.118.1 for details about frequency, and ROCOF definitions and measurements.

## 4.4 Measurement time tag from synchrophasors

Synchrophasor  measurements  shall  be tagged with the UTC  time  corresponding  to  the time of measurement. This shall consist of three numbers: a second-of-century (SOC) count, a fraction-of-second (FRACSEC) count, and a message time quality flag. The SOC count shall be a four (4) byte binary count of seconds  from  UTC  midnight  (00:00:00)  of  January  1,  1970,  to  the  current  second.  This  count  shall  be represented  as  a  32-bit  unsigned  integer.  Leap  seconds  shall  be  added  to  or  deleted  from  this  count  as necessary to keep it synchronized with UTC. Insertion of a leap second results in two successive seconds having  the  same  SOC  count,  which  are  differentiated  by  the  Leap  Second  bit  in  the  FRACSEC  word, defined as follows. Conversely, the deletion of a leap second results in a second that is  missing, so the second count only goes to 58. (With this convention, time count can always be determined from current time by multiplying the number of days since 1/1/70 by the number of seconds per day: 86 400.) This SOC time stamp will roll over to 0 in 2106 (136+ years of seconds). It is similar to the time counts used in most computer systems such as UNIX, LINUX, and DOS as well as networks [Network Time Protocol (NTP), Precision Time Protocol (PTP)].

The second shall be divided into an integer number of subdivisions by the TIME\_BASE integer specified in 6.4, Table 8. The FRACSEC count shall be an integer representing the numerator of the FRACSEC with TIME\_BASE as the denominator. Compatibility with IEC 61850 requires a TIME\_BASE value of 2^24. The FRACSEC count shall be zero when it coincides with the one-second roll over. This time tag shall be applied to all communication frames as described in Clause 6.

## 4.5 System time synchronization

Synchrophasor  measurements  shall  be  synchronized  to  UTC  time  with  accuracy  sufficient  to  meet  the accuracy  requirements  of  IEEE  Std  C37.118.1.  A  phase  error  of  0.01  radian  (0.57  degrees)  in  the synchrophasor measurement will cause 1% total vector error (TVE), which is the maximum steady-state error allowed in IEEE Std C37.118.1. A 0.01 radian phase error corresponds to a time error of ± 26 μ s for a 60 Hz system, and ± 31 μ s for a 50 Hz system.

The system shall be capable of receiving time from a highly reliable source, such as the Global Positioning System (GPS), which can provide sufficient time accuracy to keep the TVE within the required limits and provide indication of loss of synchronization. The flag in the data output (6.3, Table 6, STAT word Bit 13) is  provided to indicate a loss of time synchronization and shall be set to 1 when loss of synchronization could cause the TVE to exceed the limit or within 1 min of actual loss of synchronization, whichever is less. The flag shall remain set until data acquisition is resynchronized to the required accuracy level.

## 4.6 Synchrophasor transmission

Synchrophasor estimates shall be made so they can be reported (transmitted) as data frames at a rate F s that is  an  integer  number  of  times  per  second  or  integer  number  of  seconds  per  frame  as  specified  by  the DATA\_RATE variable in the configuration frame (6.4, Table 8 and Table 10). A data frame is a set of measurements  that  may  include  multiple  channels  of  phasor  estimates,  analog  words,  and  digital  words with a measurement status word and a time tag as defined in Clause 6.

## 4.6.1 Reporting rates

The PMU shall support data reporting (by recording or output) at sub-multiples of the nominal power-line (system) frequency. Required rates for 50 Hz and 60 Hz systems are listed in Table 1.

Table 1  -Required PMU reporting rates

| System frequency                           |   50 Hz |   50 Hz |   50 Hz |   60 Hz |   60 Hz |   60 Hz |   60 Hz |   60 Hz |   60 Hz |
|--------------------------------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Reporting rates ( F s - frames per second) |      10 |      25 |      50 |      10 |      12 |      15 |      20 |      30 |      60 |

The actual rate to be used shall be user selectable. Support for other reporting is permissible, and higher rates  such  as  100  frames/s  or  120  frames/s  and  rates  lower  than  10  frames/s  such  as  1  frame/s  are encouraged.

## 4.6.2 Reporting times

For a reporting rate, N frames per second where N is a positive integer, the reporting times shall be evenly spaced through each second with the time of the first frame coincident with the UTC second rollover. Thus the first frame will be frame number 0 (frames numbered 0 thru N-1) with a FRACSEC time of 0, the next frame number 1 with a fractional time 1/N, and so on through frame N-1 with a fractional time (N-1)/N. These  reporting  times  (time  tags)  are  to  be  used  for  determining  the  instantaneous  values  of  the synchrophasor  as  defined  in  4.1.  If  rates  lower  than  1/s  are  used,  there  shall  be  one  report  on  the  hour (xx:00:00) and evenly spaced thereafter according to the chosen rate.

## 4.7 Synchrophasor measurement

Requirements for synchrophasor, frequency, and ROCOF estimates are detailed in IEEE Std C37.118.1. Refer to that standard for measurement requirements.

## 5. Synchrophasor measurement system overview

## 5.1 Synchrophasor network

A simple structure of a synchrophasor network consists of the PMU and PDC as shown in Figure 2. If multiple intelligent electronic devices (IEDs) in a substation provide synchrophasor measurements, a local PDC may be deployed in the substation. Typically, many PMUs located at various key substations gather data and send it in real time to a PDC at the utility location where the data is aggregated. The data collected by PDCs may be used to support many applications, ranging from visualization of information and alarms for situational awareness, to ones that provide sophisticated analytical, control, or protection functionality. Applications,  such  as  dynamics  monitoring,  use  full-resolution  real-time  data  along  with  grid  models  to support  both  operating  and  planning  functions.  The  application  displays  locally  measured  frequency,

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

primary voltages, currents, real and reactive power flows, and other quantities for system operators. Many PDCs belonging to different utilities can be connected to a common central PDC to aggregate data across the utilities, in order to provide an interconnection-wide snapshot of the power grid measurements.

Figure 2  -Synchrophasor data collection network

<!-- image -->

## 5.2 Synchrophasor network elements

## 5.2.1 Synchrophasor measurement unit

The PMU is a function or logical device that provides synchrophasor and system frequency estimates, as well as other optional information such as calculated megawatts (MW) and megavars (MVAR), sampled measurements,  and  Boolean  status  words.  The  PMU  may  provide  synchrophasor  estimates  from  one  or more voltage or current waveforms. The PMU can be realized as a stand-alone physical device or as a part of  a  multifunction  device  such  as  a  protective  relay,  DFR,  or  meter.  This  information  may  be  recorded locally or transmitted in real time to a central location as illustrated in Figure 2. This standard addresses the real-time transfer of data from the PMU to the PDC or other devices.

## 5.2.2 Phasor data concentrator

A PDC works as a node in a communication network where synchrophasor data from a number of PMUs or PDCs is correlated and fed out as a single stream to the higher level PDCs and/or applications. The PDC correlates synchrophasor data by time tag to create a system wide measurement set.

Additional functions may be provided, as follows:

- a) Various quality checks on the phasor data and insertion of appropriate flags into the correlated data stream.
- b) Checks for disturbance flags and recordings of data files for analysis.
- c) Monitoring of the overall measurement system and displaying the results, as well as recording of the performance.
- d) Number of specialized outputs, such as a direct interface to a SCADA or EMS system.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

Local PDCs as shown in Figure 2 aggregate and time-align synchrophasor data from multiple IEDs and feed  the  data  to  applications.  Mid-level  regional  PDCs  collect  synchrophasor  data  from  multiple  PDCs, conduct  data  quality  checks,  and  feed  the  data  to  applications.  Higher  level  PDCs  (SuperPDCs)  both aggregate  and  archive  synchrophasor  data.  The  PDCs  may  be  recognized  as  a  function  rather  than  as  a stand-alone device or hardware-software package, and can be integrated into other systems and devices. A structured hierarchy of distributed PDCs may be formed to serve a hierarchy of systems: substation, utility, control area, reliability coordinator, and interconnection level. Each layer in the hierarchy may be serving different  data  requirements  (latency,  quality,  resolution),  with  archival  and  event  triggering  and  data capture requirements driven by applications. Since local PDCs represent a local point of failure for the data stream, backups and bypass options are needed for mitigating such failures.

## 5.3 Multiple data streams from PMUs and PDCs

A PMU or PDC may transmit its data in one or more separate data streams. Each stream may have different contents and may be sent at a different rate. The destination of each stream may be a different device and location.  Each  stream  must  then  be  individually  controllable,  have  its  own  IDCODE,  and  a  separation configuration control. This feature is useful for sending data to different devices with different purposes, allowing latency control and class of service (M and P class) supply.

## 6. Synchrophasor message format

## 6.1 Message application

This  clause  describes  the  format  of  messages  to  and  from  a  PMU  or  PDC  for  use  in  real-time communication of phasor data. Real-time data transmission here  is  defined  as  taking  place  concurrently with the measurement process. If the PMU device is to be used with other systems where the phasor data information is to be transmitted in real time, implementation of this protocol is required for conformance with this standard. If the PMU device is used only for phasor data archiving or recording, then this protocol is  not  required.  This  standard  does  not  address  requirements  for  stored  phasor  data.  Implementation  of additional protocols for phasor data communication is not restricted.

Any communication system  or  media  may  be  used  for  data  transmission.  The  message  frames  shall  be transmitted in their entirety as they are specified. When used with a stacked protocol such as manufacturing messaging specification (MMS) or IP, the entire frame including sync and CRC-CCITT shall be written into and read from the application layer interface. When used with more direct systems like raw Ethernet or RS-232, the entire frame will also be sent with the CRC-CCITT to assure data integrity.

This  message  protocol  may  be  used  for  communication  with  a  single  PMU  or  a  secondary  system  that receives  data  from  several  PMUs.  The  secondary  system,  a  PDC,  shall  have  its  own  user  assigned IDCODE.  The  protocol  allows  for  necessary  identifying  information,  such  as  the  PMU  IDCODE  and status, to be embedded in the data frame for proper interpretation of the measured data.

## 6.2 Message framework

Four message types are defined here: data , configuration , header ,  and command .  The first three message types are transmitted from the PMU/PDC that serves as the data source, and the last (command) is received by the PMU/PDC.

- ⎯ Data messages are the measurements made by a PMU.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

- ⎯ Configuration  is  a  machine-readable  message  describing  the  data  types,  calibration  factors,  and other meta-data for the data that the PMU/PDC sends.
- ⎯ Header  information  is  human  readable  descriptive  information  sent  from  the  PMU/PDC  but provided by the user.
- ⎯ Commands are machine-readable codes sent to the PMU/PDC for control or configuration.
- ⎯ A PMU or PDC may transmit multiple data streams, each with different content, rate, format, etc. Each data stream shall have its own IDCODE so that the data, configuration, header, and command messages can be appropriately identified. Each stream shall be independently operable including command execution and data, header, and configuration messages.

Information may be stored in any convenient form in the PMU/PDC itself, but when transmitted it shall be formatted  as  frames  described  in  the  following  sections.  Commands  and  other  messages  received  by  a connected device that are not understood (such as an unimplemented feature, incorrect IDCODE, bad CRC) shall be silently discarded. This messaging framework implements no error or retransmit messages.

Only data, configuration, header, and command frames are defined in this standard. Other types may be designated in the future. In normal operation, the PMU only sends data frames. Annex D contains examples of data, configuration, and command frames.

## 6.2.1 Overall message

All  message frames start with a 2-byte SYNC word followed by a 2-byte FRAMESIZE word, a 2-byte IDCODE,  a  time  stamp  consisting  of  a  4-byte  second-of-century  (SOC)  and  4-byte  FRACSEC,  which includes a 24-bit FRACSEC integer and an 8-bit Time Quality flag described in 6.2.2.

The SYNC word provides synchronization and frame identification. Bits 6-4 in the SYNC word designate the frame type. This word is detailed Table 2. Bits 3-0 describe version number. Since this is the second published edition of the synchrophasor standard, new messages shall be designated version 2 (binary 0010). The CFG-3 message introduced with this standard shall be  designated version 2;  all  previously  defined messages are unchanged in this standard and shall remain version 1. The IDCODE positively identifies the source of a data, header, or configuration message, or the destination of a command message. Note that the message IDCODE is associated with a data stream and ties data frames with the associated configuration and header information. All frames terminate in check word (CHK) which is a CRC-CCITT. This CRCCCITT uses the generating polynomial X 16 + X 12 + X 5 + 1 with an initial value of -1 (hex FFFF) and no final mask.

All frames are transmitted exactly as described with no delimiters. Figure 3 illustrates frame transmission order.  The  SYNC word is transmitted first and CHECK word last. Two- and four-byte words including integer  and  floating-point  numbers  are  transmitted  most  significant  byte  first  (network  or  'big  endian' order). All frame types use this same order and format.

Figure 3  -Example of frame transmission order

<!-- image -->

Table 2  -Word definitions common to all frame types

| Field     |   Size (bytes) | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYNC      |              2 | Frame synchronization word. Leading byte: AA hex Second byte: Frame type and version, divided as follows: Bit 7: Reserved for future definition, must be 0 for this standard version. Bits 6-4: 000: Data Frame 001: Header Frame 010: Configuration Frame 1 011: Configuration Frame 2 101: Configuration Frame 3 100: Command Frame (received message) Bits 3-0: Version number, in binary (1-15) Version 1 (0001) for messages defined in IEEE Std C37.118-2005 [B6]. Version 2 (0010) for messages added in this revision, IEEE Std C37.118.2-2011. |
| FRAMESIZE |              2 | Total number of bytes in the frame, including CHK. 16-bit unsigned number. Range = maximum 65535                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IDCODE    |              2 | Data stream ID number, 16-bit integer, assigned by user, 1-65534 (0 and 65535 are reserved). Identifies destination data stream for commands and source data stream for other messages. A stream will be hosted by a device that can be physical or virtual. If a device only hosts one data stream, the IDCODE identifies the device as well as the stream. If the device hosts more than one data stream, there shall be a different IDCODE for each stream.                                                                                          |
| SOC       |              4 | Time stamp, 32-bit unsigned number, SOC count starting at midnight 01-Jan-1970 (UNIX time base). Range is 136 years, rolls over 2106 AD. Leap seconds are not included in count, so each year has the same number of seconds except leap years, which have an extra day (86 400 s).                                                                                                                                                                                                                                                                     |
| FRACSEC   |              4 | Fraction of second and Time Quality, time of measurement for data frames or time of frame transmission for non-data frames. Bits 31-24: Message Time Quality as defined in 6.2.2. Bits 23-00: FRACSEC, 24-bit integer number. When divided by TIME_BASE yields the actual fractional second. FRACSEC used in all messages to and from a given PMU shall use the same TIME_BASE that is provided in the configuration message from that PMU.                                                                                                             |
| CHK       |              2 | CRC-CCITT, 16-bit unsigned integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## 6.2.2 Time and message time quality

The 32-bit (4-byte) FRACSEC is divided into two components: a 24-bit unsigned integer that is the actual FRACSEC count and an 8-bit message time quality flag. The time of measurement or data transmission for non-data  frames  is  the  SOC  time  stamp,  which  fixes  the  integer  second  plus  the  fractional  time.  The fractional time is determined by dividing the 24-bit integer FRACSEC by the TIME\_BASE integer given in configuration frame.

## Time = SOC + FRACSEC / TIME\_BASE

The bits  of  the  Message  Time  Quality  flag  indicate  the  'quality'  of  the  time  being  reported  as  well  as indication of leap second status. Table 3 details these assignments. Bit 7 is reserved for future use. Bit 4 is the Leap Second Pending bit and shall be set as soon as it is known, but no more than 60 s or less than 1 s before a leap second occurs. It shall be cleared in the first second after the leap second occurs. Bit 5 is the Leap Second Occurred bit and shall be set in the first second after the leap second and remains set for 24  h  afterward.  Bit  6  is  the  Leap  Second  Direction  bit,  which  is  0  for  adding  a  leap  second  and  1  for deleting a leap second. It shall be set (to 0 or 1 as required) at the same time or before the leap second

pending bit is set, and remains the same for at least 24 h afterward. This will allow analysis programs to factor in a ± Leap Second in any analysis or time difference calculation.

Table 3  -Time quality flag bit definitions

| Bit #   | Description                                                                                                                                                 |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 7       | Reserved                                                                                                                                                    |
| 6       | Leap Second Direction - 0 for add, 1 for delete                                                                                                             |
| 5       | Leap Second Occurred - set in the first second after the leap second occurs and remains set for 24 h                                                        |
| 4       | Leap Second Pending - shall be set not more than 60 s nor less than 1 s before a leap second occurs, and cleared in the second after the leap second occurs |
| 3-0     | Message Time Quality indicator code - see Table 4.                                                                                                          |

The Message Time Quality indicator code contained in the lowest 4 bits indicates the maximum time error as determined by the PMU/PDC clock function. Bits 0-3 shall be cleared to 0 when the time function is locked to a UTC traceable source, such as GPS. Either bits 0-3 shall be all set to 1 when there is a clock failure or the clock has never been initially set. The codes for this indicator are detailed in Table 4. Note that an additional time quality indication has been added to the STATUS word. That time quality indicates the maximum time error at all times and uses a different set of code values.

Table 4  -4-bit Message Time Quality indication codes (MSG\_TQ)

|   BINARY | HEX   | Value (worst-case accuracy)                            |
|----------|-------|--------------------------------------------------------|
|     1111 | F     | Fault - clock failure, time not reliable               |
|     1011 | B     | Time within 10 s of UTC                                |
|     1010 | A     | Time within 1 s of UTC                                 |
|     1001 | 9     | Time within 10 -1 s of UTC                             |
|     1000 | 8     | Time within 10 -2 s of UTC                             |
|     0111 | 7     | Time within 10 -3 s of UTC                             |
|     0110 | 6     | Time within 10 -4 s of UTC                             |
|     0101 | 5     | Time within 10 -5 s of UTC                             |
|     0100 | 4     | Time within 10 -6 s of UTC                             |
|     0011 | 3     | Time within 10 -7 s of UTC                             |
|     0010 | 2     | Time within 10 -8 s of UTC                             |
|     0001 | 1     | Time within 10 -9 s of UTC                             |
|     0000 | 0     | Normal operation, clock locked to UTC traceable source |

## 6.2.3 Leap second bit timing examples

The following  examples  show  how  the  time  count  and  leap  second  bits  will  actually  appear  for  both  a positive  (added)  leap  second  and  a  negative  (deleted)  leap  second.  The  direction  bit  can  be  at  any  state before the Leap Second Pending bit is set and after the leap Second Occurred bit clears. When either of these  bits  is  set,  the  direction  bit  shall  be  set  in  the  state  properly  indicating  insertion  or  deletion.  The pending bit shall be set as soon as a leap second occurrence is known but not more than 59 s or less than 1 s before the change will occur.

| Added leap second:   | Added leap second:   |                 |                |               |                                                                                                                    |
|----------------------|----------------------|-----------------|----------------|---------------|--------------------------------------------------------------------------------------------------------------------|
| SOC Time             | Time of day          | Direction Bit 6 | Occurred bit 5 | Pending bit 4 | Comments                                                                                                           |
| 1114991939           | 23:58:59             | X               | 0              | 0             | Direction bit any state before pending                                                                             |
| 1114991940           | 23:59:00             | 0               | 0              | 1             | Pending can be set no earlier than here                                                                            |
| 1114991941           | 23:59:01             | 0               | 0              | 1             |                                                                                                                    |
| 1114991998           | 23:59:58             | 0               | 0              | 1             |                                                                                                                    |
| 1114991999           | 23:59:59             | 0               | 0              | 1             | Pending and direction shall be set by here Leap second occurs here                                                 |
| 1114992000           | 23:59:60             | 0               | 0              | 1             | Pending and direction shall be set by here Leap second occurs here                                                 |
| 1114992000           | 00:00:00             | 0               | 1              | 0             | Occurred and direction remain set                                                                                  |
| 1114992001           | 00:00:01             | 0               | 1              | 0             |                                                                                                                    |
| 1115078399           | 23:59:59             | 0               | 1              | 0             |                                                                                                                    |
| 1115078400           | 00:00:00             | X               | 0              | 0             | Occurred cleared, direction don't care                                                                             |
| Deleted leap second: | Deleted leap second: |                 |                |               |                                                                                                                    |
| SOC Time             | Time of day          | Direction Bit 6 | Occurred bit 5 | Pending bit 4 | Comments                                                                                                           |
| 1114991939           | 23:58:59             | X               | 0              | 0             | Direction bit any state before pending Pending can be set no earlier than here                                     |
| 1114991940           | 23:59:00             | 1               | 0              | 1             | Direction bit any state before pending Pending can be set no earlier than here                                     |
| 1114991941           | 23:59:01             | 1               | 0              | 1             |                                                                                                                    |
| 1114991997           | 23:59:57             | 1               | 0              | 1             |                                                                                                                    |
| 1114991998           | 23:59:58             | 1               | 0              | 1             | Pending and direction shall be set by here Leap second occurred, pending cleared Occurred and direction remain set |
| 1114992000           | 00:00:00             | 1               | 1              | 0             | Pending and direction shall be set by here Leap second occurred, pending cleared Occurred and direction remain set |
| 1114992001           | 00:00:01             | 1               | 1              | 0             | Pending and direction shall be set by here Leap second occurred, pending cleared Occurred and direction remain set |
| 1114992002           | 00:00:02             | 1               | 1              | 0             |                                                                                                                    |
| 1115078399           | 23:59:59             | 1               | 1              | 0             |                                                                                                                    |
| 1115078400           | 00:00:00             | X               | 0              | 0             | Occurred cleared, direction don't care                                                                             |

## 6.3 Data frame

A data frame shall contain measured data and shall be identified by having bits 4-6 in the SYNC word set to zero as shown in Table 2. The real-time phasor data frame shall consist of binary data ordered as shown in Table 5 and described in detail in Table 6. All fields shall be fixed length as described and no delimiters shall be used. The frame starts with SYNC, FRAMESIZE, IDCODE, SOC and FRACSEC, and terminates with a CRC-CCITT as shown in 6.2.

## Table 5  -Data frame organization

| No.   | Field       | Size (bytes)           | Comment                                                                                                                                                                                                                                                                                                                          |
|-------|-------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | SYNC        | 2                      | Sync byte followed by frame type and version number.                                                                                                                                                                                                                                                                             |
| 2     | FRAMESIZE   | 2                      | Number of bytes in frame, defined in 6.2.                                                                                                                                                                                                                                                                                        |
| 3     | IDCODE      | 2                      | Stream source ID number, 16-bit integer, defined in 6.2.                                                                                                                                                                                                                                                                         |
| 4     | SOC         | 4                      | SOC time stamp, defined in 6.2, for all measurements in frame.                                                                                                                                                                                                                                                                   |
| 5     | FRACSEC     | 4                      | Fraction of Second and Time Quality, defined in 6.2, for all measurements in frame.                                                                                                                                                                                                                                              |
| 6     | STAT        | 2                      | Bit-mapped flags.                                                                                                                                                                                                                                                                                                                |
| 7     | PHASORS     | 4 × PHNMR or 8 × PHNMR | Phasor estimates. May be single phase or 3-phase positive, negative, or zero sequence. Four or 8 bytes each depending on the fixed 16-bit or floating-point format used, as indicated by the FORMAT field in the configuration frame. The number of values is determined by the PHNMR field in configuration 1, 2, and 3 frames. |
| 8     | FREQ        | 2 / 4                  | Frequency (fixed or floating point).                                                                                                                                                                                                                                                                                             |
| 9     | DFREQ       | 2 / 4                  | ROCOF (fixed or floating point).                                                                                                                                                                                                                                                                                                 |
| 10    | ANALOG      | 2 × ANNMR or 4 × ANNMR | Analog data, 2 or 4 bytes per value depending on fixed or floating-point format used, as indicated by the FORMAT field in configuration 1, 2, and 3 frames. The number of values is determined by the ANNMR field in configuration 1, 2, and 3 frames.                                                                           |
| 11    | DIGITAL     | 2 × DGNMR              | Digital data, usually representing 16 digital status points (channels). The number of values is determined by the DGNMR field in configuration 1, 2, and 3 frames.                                                                                                                                                               |
|       | Repeat 6-11 |                        | Fields 6-11 are repeated for as many PMUs as in NUM_PMU field in configuration frame.                                                                                                                                                                                                                                            |
| 12+   | CHK         | 2                      | CRC-CCITT                                                                                                                                                                                                                                                                                                                        |

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Table 6  -Word definitions unique to data frames

| Field   | Size (bytes)   | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYNC    | 2              | First byte: AA hex Second byte: 01 hex (frame is version 1, IEEE Std C37.118-2005 [B6])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| STAT    | 2              | Bit mapped flags. Bit 15-14: Data error: 00 = good measurement data, no errors 01 = PMU error. No information about data 10 = PMU in test mode (do not use values) or absent data tags have been inserted (do not use values) 11 = PMU error (do not use values) Bit 13: PMU sync, 0 when in sync with a UTC traceable time source Bit 12: Data sorting, 0 by time stamp, 1 by arrival Bit 11: PMU trigger detected, 0 when no trigger Bit 10: Configuration change, set to 1 for 1 min to advise configuration will change, and clear to 0 when change effected. Bit 09: Data modified, 1 if data modified by post processing, 0 otherwise Bits 08-06: PMU Time Quality. Refer to codes in Table 7. Bits 05-04: Unlocked time: 00 = sync locked or unlocked < 10 s (best quality) \01 = 10 s ≤ unlocked time < 100 s 10 = 100 s < unlock time ≤ 1000 s 11 = unlocked time > 1000 s Bits 03-00: Trigger reason: 1111-1000: Available for user definition 0111: Digital 0110: Reserved 0101: df/dt High 0100: Frequency high or low 0011: Phase angle diff 0010: Magnitude high |
| PHASORS | 4 / 8          | Data type indicated by the FORMAT field in configuration 1, 2, and 3 frames 16-bit integer values: Rectangular format: - real and imaginary, real value first - 16-bit signed integers, range -32 767 to +32 767 Polar format: - magnitude and angle, magnitude first - magnitude 16-bit unsigned integer range 0 to 65535 - angle 16-bit signed integer, in radians × 10 4 , range -31 416 to +31 416 32-bit values in IEEE floating-point format: Rectangular format: - real and imaginary, in engineering units, real value first Polar format: - magnitude and angle, magnitude first and in engineering units - angle in radians, range - π to + π                                                                                                                                                                                                                                                                                                                                                                                                                        |
| FREQ    | 2 / 4          | Frequency deviation from nominal, in mHz Range-nominal (50 Hz or 60 Hz) -32.767 to +32.767 Hz 16-bit integer or 32-bit floating point 16-bit integer: 16-bit signed integers, range -32 767 to +32 767 32-bit floating point: actual frequency value in IEEE floating-point format. Data type indicated by the FORMAT field in configuration 1, 2, and 3 frames                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DFREQ   | 2 / 4          | ROCOF, in hertz per second times 100 Range -327.67 to +327.67 Hz per second Can be 16-bit integer or IEEE floating point, same as FREQ above. Data type indicated by the FORMAT field in configuration 1, 2, and 3 frames                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ANALOG  | 2 / 4          | Analog word. 16-bit integer. It could be sampled data such as control signal or transducer value. Values and ranges defined by user. Can be 16-bit integer or IEEE floating point. Data type indicated by the FORMAT field in configuration 1, 2, and 3 frames                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DIGITAL | 2              | Digital status word. It could be bit mapped status or flag. Values and ranges defined by user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## 6.3.1 Explanation for STAT word in the data frame

The data frame consists of time and data sections with framing. The data can be one block from a single PMU or multiple blocks from multiple PMUs. Each PMU data block is headed by a STAT word that has complete status for that block; this STAT applies to that block only. Bits are set in this STAT flag initially by the PMU that generates the data, and can be altered by other processors in the data chain, such as by a DC.  The  STAT  word  gives  a  complete  status  for  the  data  in  its  data  block  within  the  bounds  of  this standard.

Bit 15-Bit 14 Data Error Indicator: set as noted in Table 6. A PDC is expected to receive data from several PMUs and  transmit  the  aligned  data  to  its  destination(s).  However,  due  to  the  latency  requirements  of applications, the PDC will not wait indefinitely for the arriving data, but implement a wait time . Once the wait  time  is  over,  the  PDC  will  send  whatever  data  has  arrived  within  this  interval.  The  IEEE  C37.118 message format requires sending fixed-size data frames, so if any data that goes in a frame is not present when the frame is assembled, the PDC will need to provide a filler. So a receiving device will not interpret this  filler  as  data,  the  PDC must set these bits to 10 in the status word to indicate the data in this PMU section is not valid. In addition, the data itself can be written as invalid. For floating-point data NaN (not a number) will be inserted for the absent data. For fixed-point data in rectangular format the PDC will use 0x8000 (-32768) as the substitute for the absent data. The standard allows values of +32 767 to -32 767 for valid data (see Table 6). For fixed-point data in polar format all values are permissible for the magnitude field. However, the angle field is restricted to ±31416. A value of 0x8000 (-32768) used in the angle field will be used to signify absent data.

Bit 13 -PMU Sync Error: set to 1 to indicate the PMU has detected a loss of external time synchronization such as a loss of satellite tracking or a time input connection failure. It shall be used both when the time synchronization input fails and when the source of time synchronization loses lock to UTC traceable time. The measuring PMU shall set this bit to 1 when the 4-bit time quality field in the FRACSEC field becomes non-zero. A DC may also set Bit 13 to 1 if it detects a synchronization error in the data stream from a particular PMU. The length of time between detecting a sync error and setting Bit 13 to 1 shall not exceed the  time  for  the  estimated  time  error  to  exceed  31 μ s  in  a  50  Hz  system  or  26 μ s  in  a  60  Hz  system (equivalent to 1% TVE due to phase only) or 1 min, whichever is less.

Bit 12 -Data Sorting Type: set to 1 when the data for the particular PMU is not integrated into the data frame by using its time tag. A concentrator will normally integrate data from a number of PMUs into a single frame by the time tags provided by the PMUs. If a PMU in the group loses external time sync for an extended period, a time tag provided by the PMU may prevent this integration, or make time alignment worse  than  using  another  integration  method.  As  an  alternative  to  simply  discarding  all  the  data,  the concentrator  can  include  the  data  in  the  frame  using  a  'best  guess'  as  to  which  frame  it  goes  in,  and  a warning of lack of precise time correlation by setting bit 12. The simplest approach for the concentrator in a real-time system is to include the unsynchronized data with the most current synchronized data using the assumption that data communication delays are equal. This 'sort-by-arrival' method is a simple best guess data alignment. Other methods can be used. In all cases, Bit 12 will be set to 1 when data is not correlated into its frame by time tag and cleared to 0 when data is correlated by time tag.

Bit 11 -PMU Trigger pick-up: set to indicate a trigger condition has been detected for PMUs that have trigger capability. The bit shall be set for a mandatory set period of at least one data frame or one second, whichever is longer. It may remain set as long as the trigger condition is detected or may be cleared after this mandatory set period to allow for detection of other triggers.

Bit 10 -Configuration change bit shall be set to a 1 to indicate that the PMU configuration will change. Transition of bit 10 from 0 to 1 indicates that a configuration change will become effective in 1 min. This bit is to be reset to 0 after 1 min and the configuration change shall be effective beginning with the first message where bit  10  is  0.  The  bit  serves  as  an  indication  that  the  receiving  device  should  request  the configuration file to be sure configuration data is up to date. To be certain of having a valid configuration file,  the  receiving device shall request a configuration file whenever it has been off-line for more than a minute.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

Bit 9 -Data modified indicator. If phasor data in frame is modified by a post-processing device such as a PDC,  this  bit  shall  be  set  to  1.  This  shall  include  data  points  inserted  by  interpolation  or  lost  point reconstruction, and data modified by down-sampling methods, offset adjustment, or error correction. In all other cases this bit shall be set to 0. It shall not be used to indicate conversions such as polar-rectangular and integer-floating point.

Bits  6-8 -PMU\_TQ  (PMU  Time  Quality):  This  3-bit  time  quality  code  shall  indicate  the  maximum uncertainty in the measurement time at the time of measurement. It shall be derived from the time source and  be  adjusted  to  include  uncertainties  in  the  PMU  measuring  process.  This  time  quality  information indicates time quality at all times, both when time is considered locked and unlocked. The codes and their range of time uncertainty indication are detailed in Table 7. When the time quality is not known during startup, a code of 111b shall be used. A time quality of 000b indicates a previous version of this message that does not indicate time quality in these bits.

NOTE-The previous version of this standard, IEEE Std C37.118-2005 [B6], reserved bits 6-9 for adding security and required them to be set to 0. The security addition proved impractical, so these bits have been reassigned as above. The new  TQ  code  remains  with  the  measurement  so  the  maximum  time  uncertainty  can  be  used  with  any  processing system. Since these bits were previously always zero, a non-zero value indicates time quality. A zero value indicates the bits are not used or PMU Time Quality is unknown (and so is compatible with the previous version of the standard).

This TQ has been added since the previous TQ does not report actual TQ during lock condition and it is not preserved with the measurements. Once data is passed to a higher level, the TQ that was observed during the measurement is lost. This code is the same as the CTQ specified for the IRIG-B profile in Annex D of IEEE Std C37.118.1-2011.

Table 7  -3-bit PMU Time Quality indication codes (PMU\_TQ)

|   BINARY |   HEX | VALUE (worst-case accuracy)                                |
|----------|-------|------------------------------------------------------------|
|      111 |     7 | Estimated maximum time error > 10 ms or time error unknown |
|      110 |     6 | Estimated maximum time error < 10 ms                       |
|      101 |     5 | Estimated maximum time error < 1 ms                        |
|      100 |     4 | Estimated maximum time error < 100 μ s                     |
|      011 |     3 | Estimated maximum time error < 10 μ s                      |
|      010 |     2 | Estimated maximum time error < 1 μ s                       |
|      001 |     1 | Estimated maximum time error < 100 ns                      |
|      000 |     0 | Not used (indicates code from previous version of profile) |

Bits  4-5 -Unlocked  time:  indicates  a  range  of  seconds  since  loss  of  synch  was  detected.  This  counts seconds from the loss of lock on time synch until it is reacquired. When sync is reacquired, the code goes to 00.  The  criteria  for  determining  when  lock  on  time  synch  is  achieved  or  lost  is  not  specified  in  this standard. This will be normally implemented as follows:

|   Bit code | Indication                                    |
|------------|-----------------------------------------------|
|         00 | Locked or unlocked less than 10 s             |
|         01 | Unlocked 10 s or longer but less than 100 s   |
|         10 | Unlocked 100 s or longer but less than 1000 s |
|         11 | Unlocked 1000 s or more                       |

Bits 0-3 -Trigger reason: a 4-bit code indicating the initial cause of a trigger. See Table 6 for encoding.

## 6.4 Configuration frame

A  configuration  frame  is  a  machine-readable  BINARY  data  set  containing  information  and  processing parameters  for  a  synchrophasor  data  stream.  Three  configuration  frame  types  are  specified  and  are identified by bits 4-6 of the SYNC word as shown in Table 2. CFG-1 and CFG-2 are part of the version 1 (IEEE  Std C37.118-2005  [B6]) message  set, and optional CFG-3  is introduced with version 2 (IEEE  Std  C37.118.2-2011).  CFG-1  denotes  the  PMU/PDC  capability,  indicating  all  the  data  that  the

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

PMU/PDC is capable of reporting. CFG-2 indicates measurements currently being reported (transmitted) in the  data  frame.  This  may  be  only  a  subset  of  available  data.  Both  frames  have  identical  structure  with 19  fields,  and  with  fields  8-19  repeated  as  necessary.  In  these  frames,  all  fields  are  fixed  length  as described  and  no  delimiters  shall  be  used.  The  frame  contents  are  shown  in  Table  8,  and  described  in Table 9.

CFG-3 is similar to  the  other  configuration  frames  and  contains  much  of  the  same  data  but  with  added information and flexible framing. CFG-3 indicates measurements currently being reported in the data frame (the same as CFG-2). CFG-3 has variable length fields, added PMU and signal information, and extendable frame. The frame contents are shown in Table 10 and described in Table 11. Note CFG-3 is optional; a synchrophasor  device  does  not  have  to  implement  this  message  to  be  considered  compliant  with  this standard.

Table 8  -Configuration frame 1 and 2 organization

| No   | Field       | Size (bytes)                      | Short description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------|-------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | SYNC        | 2                                 | Sync byte followed by frame type and version number.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2    | FRAMESIZE   | 2                                 | Number of bytes in frame, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 3    | IDCODE      | 2                                 | Stream source ID number, 16-bit integer, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 4    | SOC         | 4                                 | SOC time stamp, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 5    | FRACSEC     | 4                                 | Fraction of Second and Message Time Quality, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 6    | TIME_BASE   | 4                                 | Resolution of FRACSEC time stamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 7    | NUM_PMU     | 2                                 | The number of PMUs included in the data frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 8    | STN         | 16                                | Station Name - 16 bytes in ASCII format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 9    | IDCODE      | 2                                 | Data source ID number identifies source of each data block.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 10   | FORMAT      | 2                                 | Data format within the data frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 11   | PHNMR       | 2                                 | Number of phasors - 2-byte integer (0 to 32 767).                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 12   | ANNMR       | 2                                 | Number of analog values - 2-byte integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 13   | DGNMR       | 2                                 | Number of digital status words - 2-byte integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 14   | CHNAM       | 16 × (PHNMR + ANNMR + 16 × DGNMR) | Phasor and channel names - 16 bytes for each phasor, analog, and each digital channel (16 channels in each digital word) in ASCII format in the same order as they are transmitted. For digital channels, the channel name order will be from the least significant to the most significant. (The first name is for bit 0 of the first 16-bit status word, the second is for bit 1, etc., up to bit 15. If there is more than 1 digital status, the next name will apply to bit 0 of the second word and so on.) |
| 15   | PHUNIT      | 4 × PHNMR                         | Conversion factor for phasor channels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 16   | ANUNIT      | 4 × ANNMR                         | Conversion factor for analog channels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 17   | DIGUNIT     | 4 × DGNMR                         | Mask words for digital status words.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 18   | FNOM        | 2                                 | Nominal line frequency code and flags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 19   | CFGCNT      | 2                                 | Configuration change count.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|      | Repeat 8-19 |                                   | Fields 8 - 19, repeated for as many PMUs as in field 7 (NUM_PMU).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 20+  | DATA_RATE   | 2                                 | Rate of data transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 21+  | CHK         | 2                                 | CRC-CCITT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Table 9  -Word definitions unique to configuration frames 1 and 2

| Field     |   Size (bytes) | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYNC      |              2 | First byte: AA hex Second byte: 21 hex for configuration 1 31 hex for configuration 2 Both frames are version 1 (IEEE Std C37.118-2005 [B6])                                                                                                                                                                                                                                                                                                                  |
| TIME_BASE |              4 | Resolution of the fractional second time stamp (FRACSEC) in all frames. Bits 31-24: Reserved for flags (high 8 bits). Bits 23-0: 24-bit unsigned integer, which is the subdivision of the second that the FRACSEC is based on. The actual 'fractional second of the data frame' = FRACSEC / TIME_BASE.                                                                                                                                                        |
| NUM_PMU   |              2 | The number of PMUs included in the data frame. No limit specified. The actual limit will be determined by the limit of 65 535 bytes in one frame ('FRAMESIZE' field).                                                                                                                                                                                                                                                                                         |
| STN       |             16 | Station Name - 16 bytes in ASCII format.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| IDCODE    |              2 | Data stream ID number, 16-bit integer, defined in 6.2. It identifies the data stream in field 3 and the data source in fields 9 and higher. Field 3 identifies the stream that is being received. The IDCODEs in field 9 (and higher if more than one PMU data is present) identify the original source of the data and will usually be associated with a particular PMU. The IDCODEs in a data stream received directly from a PMU will usually be the same. |
| FORMAT    |              2 | Data format in data frames, 16-bit flag. Bits 15-4: Unused Bit 3: 0 = FREQ/DFREQ 16-bit integer, 1 = floating point Bit 2: 0 = analogs 16-bit integer, 1 = floating point Bit 1: 0 = phasors 16-bit integer, 1 = floating point Bit 0: 0 = phasor real and imaginary (rectangular), 1 = magnitude and angle (polar)                                                                                                                                           |
| PHNMR     |              2 | Number of phasors - 2-byte integer.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ANNMR     |              2 | Number of analog values - 2-byte integer.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DGNMR     |              2 | Number of digital status words - 2-byte integer. Digital status words are normally 16-bit Boolean numbers with each bit representing a digital status channel measured by a PMU. A digital status word may be used in other user-designated ways.                                                                                                                                                                                                             |
| CHNAM     |             16 | Phasor and channel names - 16 bytes for each phasor, analog and digital status word in ASCII format in the same order as they are transmitted.                                                                                                                                                                                                                                                                                                                |
| PHUNIT    |              4 | Conversion factor for phasor channels. Four bytes for each phasor. Most significant byte: 0 - voltage; 1 - current. Least significant bytes: An unsigned 24-bit word in 10 -5 V or amperes per bit to scale 16-bit integer data (if transmitted data is in floating-point format, this 24-bit value shall be ignored).                                                                                                                                        |
| ANUNIT    |              4 | Conversion factor for analog channels. Four bytes for each analog value. Most significant byte: 0 - single point-on-wave, 1 - rms of analog input, 2 - peak of analog input, 5-64 - reserved for future definition; 65-255 - user definable. Least significant bytes: A signed 24-bit word, user defined scaling.                                                                                                                                             |
| DIGUNIT   |              4 | Mask words for digital status words. Two 16-bit words are provided for each digital word. The first will be used to indicate the normal status of the digital inputs by returning a 0 when exclusive ORed (XOR) with the status word. The second will indicate the current valid inputs to the PMU by having a bit set in the binary position corresponding to the digital input and all other bits set to 0. See NOTE.                                       |
| FNOM      |              2 | Nominal line frequency code (16 bit unsigned integer) Bits 15-1:Reserved Bit 0: 1 - Fundamental frequency = 50 Hz 0 - Fundamental frequency = 60 Hz                                                                                                                                                                                                                                                                                                           |

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Table 9 -Word definitions unique to configuration frames 1 and 2 (continued)

| Field     |   Size (bytes) | Description                                                                                                                                                                                                                                                                                                                                               |
|-----------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DATA_RATE |              2 | Rate of phasor data transmissions - 2-byte integer word (-32 767 to +32 767) If DATA_RATE > 0, rate is number of frames per second. If DATA_RATE < 0, rate is negative of seconds per frame. E.g., DATA_RATE = 15 is 15 frames per second; DATA_RATE = -5 is 1 frame per 5 s.                                                                             |
| CFGCNT    |              2 | Configuration change count is incremented each time a change is made in the PMU configuration. 0 is the factory default and the initial value. This count identifies the number of changes in the configuration of this message stream. The count will be the same in all configuration messages (CFG-1, CFG-2, and CFG-3) for the same message revision. |

NOTE -If digital status words are used for something other than Boolean status indications, the use of masks is left to the user, such as min or max settings.

The  CFG-3  frame  includes  the  basic  information  that  is  in  CFG-2,  but  adds  a  number  of  fields  further defining PMU characteristics and quantities being sent. It adds an index for frame continuation in case the configuration  gets  too  large  to  be  sent  as  a  single  frame  (frames  are  limited  by  the  frame  size  field  to 65535 bytes). The name fields have an index byte that specifies the field size. This allows name lengths up to  255  bytes  and  enables  compressing  the  field  size  to  the  actual  name  length.  The  phasor  and  analog scaling  has  been  expanded  to  include  a  multiplier  and  offset.  Additional  information  has  been  added including PMU location, data measurement class, and algorithm factors. CFG-3 reports the contents of the data  currently  being  sent  (same  as  CFG-2).  CFG-3  has  29  fields,  with  9-27  repeated  as  necessary.  The structure is the same as the other configuration messages, except there are more fields and the name fields are not fixed length (decoding requires reading the name field indexes). No delimiters are used. The frame contents are shown in Table 10, and described in Table 11.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Table 10 -Configuration frame 3 organization

| No   | Field       | Size (bytes)   | Short description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------|-------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | SYNC        | 2              | Sync byte followed by frame type and version number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2    | FRAMESIZE   | 2              | Number of bytes in frame, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 3    | IDCODE      | 2              | PMU/PDC data stream ID number, 16-bit integer, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 4    | SOC         | 4              | SOC time stamp, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 5    | FRACSEC     | 4              | Fraction of Second and Message Time Quality, defined in 6.2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 6    | CONT_IDX    | 2              | Continuation index for fragmented frames.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 7    | TIME_BASE   | 4              | Resolution of FRACSEC time stamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 8    | NUM_PMU     | 2              | The number of PMUs included in the data frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 9    | STN         | 1-256          | Station Name - in ASCII format with field index (see Table 12).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 10   | IDCODE      | 2              | Data source ID number identifies source of each data block.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 11   | G_PMU_ID    | 16             | Global PMU ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 12   | FORMAT      | 2              | Data format within the data frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 13   | PHNMR       | 2              | Number of phasors - 2-byte integer (0 to 32 767).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 14   | ANNMR       | 2              | Number of analog values - 2-byte integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 15   | DGNMR       | 2              | Number of digital status words - 2-byte integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 16   | CHNAM       | 1-256 per name | Phasor and channel names - in ASCII with field index (see Table 12). Minimum of 1 byte for each phasor, analog, and digital channel. Names are in the same order as they are transmitted: all phasors, all analogs, and all digitals. For digital channels, the channel name order will be from the least significant to the most significant. (The first name is for bit 0 of the first 16-bit status word, the second is for bit 1, etc., up to bit 15. If there is more than 1 digital status, the next name will apply to bit 0 of the second word and so on.) |
| 17   | PHSCALE     | 12 ×           | Conversion factor for phasor channels with flags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 18   | ANSCALE     | 8 × ANNMR      | Conversion factor for analog channels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 19   | DIGUNIT     | 4 × DGNMR      | Mask words for digital status words.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 20   | PMU_LAT     | 4              | PMU Latitude in degrees, 32-bit floating point, WGS84 datum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 21   | PMU_LON     | 4              | PMU Longitude in degrees, 32-bit floating point, WGS84 datum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 22   | PMU_ELEV    | 4              | PMU Elevation in meters, 32-bit floating point, WGS84 datum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 23   | SVC_CLASS   | 1              | Service class, as defined in IEEE Std C37.118.1, a single ASCII character that is Mor P for IEEE Std C37.118.1.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 24   | WINDOW      | 4              | Phasor measurement window length including all filters and estimation windows in effect. Value is in microseconds, 4-byte integer value (to nearest microsecond).                                                                                                                                                                                                                                                                                                                                                                                                  |
| 25   | GRP_DLY     | 4              | Phasor measurement group delay including all filters and estimation windows in effect. Value is in microseconds, 4-byte integer value (to nearest microsecond).                                                                                                                                                                                                                                                                                                                                                                                                    |
| 26   | FNOM        | 2              | Nominal line frequency code and flags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 27   | CFGCNT      | 2              | Configuration change count.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|      | Repeat 9-27 |                | Fields 9-27, repeated for as many PMUs as in field 8 (NUM_PMU).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 28+  | DATA_RATE   | 2              | Rate of data transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 29+  | CHK         | 2              | CRC-CCITT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Table 11 -Word definitions unique to configuration frame 3

| Field     | Size (bytes)   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYNC      | 2              | First byte: AA hex Second byte: 52 hex for configuration 3 Frame is version 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CONT_IDX  | 2              | Continuation index for fragmented frames: 0: only frame in configuration, no further frames 1: first frame in series, more to follow 2-65534: number of each succeeding frame, in order 65535 (hex FFFF): last frame in series                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TIME_BASE | 4              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| NUM_PMU   | 2              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| STN       | 1-256          | Station Name - in UTF-8 format, up to 255 bytes using the name field format (see Table 11).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IDCODE    | 2              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| G_PMU_ID  | 16             | This 128-bit Global PMU ID shall be a user-assigned value. It shall be stored in the PMU or other sending device so it can be sent with this configuration 3 message. It allows uniquely identifying PMUs in a system that has more than 65535 PMUs. The coding for the 16 bytes is left to the user for assignment.                                                                                                                                                                                                                                                                                                                                                                                |
| FORMAT    | 2              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PHNMR     | 2              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ANNMR     | 2              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DGNMR     | 2              | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| CHNAM     | 1-256          | Channel Names - one name for each phasor, analog, and digital channel in UTF-8 using the name field format (see Table 12). Names appear in the same order as they are transmitted: all phasors followed by all analogs followed by all digitals. For digital channels, the order is the same as described for configurations 1 and 2.                                                                                                                                                                                                                                                                                                                                                               |
| PHSCALE   | 12             | Magnitude and angle scaling for phasors with data flags. This factor has three 4-byte long words: the first is bit-mapped flags, the second is a magnitude scale factor, and the third is an angle offset. First 4-byte word First 2 bytes: 16-bit flag that indicates the type of data modification when data is being modified by a continuous process. When no modification process is being applied, all bits shall be set to 0. (Bit 0 is the LSB, Bit 15 is the MSB.) This flag shall be used in conjunction with the data modification bit (Bit 9) in the status word. That bit shall be set in any frame that data has been modified by any process including those indicated in this flag. |

## Table 11 -Word definitions unique to configuration frame 3 (continued)





| Field   | Size (bytes)   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         |                | Bit # Meaning when bit set 0 Not used, reserved 1 Up sampled with interpolation 2 Upsampled with extrapolation 3 Down sampled by reselection (selecting every Nth sample) 4 Down sampled with FIR filter 5 Down sampled with non-FIR filter 6 Filtered without changing sampling 7 Phasor magnitude adjusted for calibration 8 Phasor phase adjusted for calibration 9 Phasor phase adjusted for rotation ( ±30º, ±120º, etc.) 10 Pseudo-phasor value (combined from other phasors) 11-14 Reserved for future assignment 15 Modification applied, type not here defined Third byte: phasor type indication (Bit 0 is the LSB, Bit 7 is the MSB) Bits 07-04: Reserved for future use Bit 03: 0 - voltage; 1 - current. Bits 02-00: Phasor component, coded as follows 111: Reserved 110: Phase C 101: Phase B 100: Phase A 011: Reserved 010: Negative sequence 001: Positive sequence 000: Zero sequence Fourth byte: available for user designation Second and third 4-byte words For phasor X = X m e j φ , this defines the scaling Y and angle offset θ to be applied to the phasor as follows: X' = Y × X m e j ( φ - θ ) The second 4-byte word is the scale factor Y in 32-bit IEEE floating point. This scales phasor data to primary volts or amperes. If phasors are transmitted in floating-point format and scaled already, this value shall be set to 1. The third 4-byte word is the phasor angle adjustment θ in radians represented in |
| ANSCALE | 8              | scaled already, this value shall be set to 0. Linear scaling for analog channels. For analog value X , this defines scale M and offset B for X' = M × X + B . First 4 bytes: Magnitude scaling M in 32-bit floating point. Last 4 bytes: Offset B in 32-bit floating point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DIGUNIT | 4              | Mask words for digital status words. Two 16-bit words are provided for each digital word. The first will be used to indicate the normal status of the digital inputs by returning a 0 when exclusive Ored (XOR) with the status word. The second will indicate the current valid inputs to the PMU by having a bit set in the binary position corresponding to the digital input and all other bits set to 0. See NOTE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

Table 11 -Word definitions unique to configuration frame 3 (continued)

NOTE -If digital status words are used for something other than Boolean status indications, the use of masks is left to the user, such as min or max settings.

| Field                                                                                                                    | Size (bytes)                                                                                                             | Description                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PMU_LAT                                                                                                                  | 4                                                                                                                        | PMU Latitude in degrees, range -90.0 to +90.0. Positive values are N of equator. WGS 84 datum. Number in 32-bit IEEE floating-point format. For unspecified locations, infinity shall be used.                                                                                |
| PMU_LON                                                                                                                  | 4                                                                                                                        | PMU Longitude in degrees, range -179.99999999 to +180. Positive values are E of the prime meridian. WGS 84 datum. Number in 32-bit IEEE floating-point format. For unspecified locations, infinity shall be used.                                                             |
| PMU_ELEV                                                                                                                 | 4                                                                                                                        | PMU Elevation in meters, Positive values are above mean sea level. WGS 84 datum. Number in 32-bit IEEE floating-point format. For unspecified locations, infinity shall be used.                                                                                              |
| SVC_CLASS                                                                                                                | 1                                                                                                                        | Service class, as defined in IEEE Std C37.118.1, a single ASCII character. In 2011 it is Mor P.                                                                                                                                                                               |
| WINDOW                                                                                                                   | 4                                                                                                                        | Phasor measurement window length including all filters and estimation windows in effect. Value is in microseconds, 4-byte signed integer value (to nearest microsecond). (For information only, any required compensation is already applied to the measurement.)             |
| GRP_DLY                                                                                                                  | 4                                                                                                                        | Phasor measurement group delay including all filters and estimation windows in effect. Value is in microseconds, 4-byte signed integer value (to nearest microsecond). (For information only, any required compensation is already applied to the measurement.)               |
| FNOM                                                                                                                     | 2                                                                                                                        | Nominal line frequency code (16 bit unsigned integer) Bits 15-1: Reserved Bit 0: 1 - Fundamental frequency = 50 Hz 0 - Fundamental frequency = 60 Hz                                                                                                                          |
| DATA_RATE                                                                                                                | 2                                                                                                                        | Rate of phasor data transmissions - 2-byte integer word (-32 767 to +32 767) If DATA_RATE > 0, rate is number of frames per second. If DATA_RATE < 0, rate is negative of seconds per frame. E.g.: DATA_RATE = 15 is 15 frames per second; DATA_RATE = -5 is 1 frame per 5 s. |
| CFGCNT                                                                                                                   | 2                                                                                                                        | Same as CFG-1 and CFG-2.                                                                                                                                                                                                                                                      |
| NOTE - If digital status words are used for something other than Boolean status indications, the use of masks is left to | NOTE - If digital status words are used for something other than Boolean status indications, the use of masks is left to | NOTE - If digital status words are used for something other than Boolean status indications, the use of masks is left to                                                                                                                                                      |

Station and signal names shall be listed in fields whose length can vary from 1 to 256 bytes. The first byte in each name field is the length, which is an unsigned 8-bit integer that indicates the length of the name in bytes. A length of 0 indicates no further bytes (no name). All name fields will have at least one byte that is the name length. All names shall use UTF-8 coding.

Table 12 -Name field description

| More names   | Name field (single station or signal name)   | Name field (single station or signal name)                                                                         | More names   |
|--------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------|
| …            | 1 byte                                       | 0-255 bytes                                                                                                        | …            |
| -            | Name length - unsigned 8-bit integer, 0-255  | Name, UTF-8 coding Note that standard 7-bit ASCII characters are the same as UTF-8 and no conversions are required | -            |

## 6.5 Header frame

This  frame  shall  be  human-readable  information  about  the  PMU,  the  data  sources,  scaling,  algorithms, filtering, or other related information. The frame has the same SYNC, FRAMESIZE, SOC, FRACSEC, and CHK as the other frames, and is identified by bits 4-6 the SYNC word as shown in Table 2. The data section has no fixed format (Table 13).

Table 13 -Header frame organization

| No   | Field     |   Size (bytes) | Comment                                                         |
|------|-----------|----------------|-----------------------------------------------------------------|
| 1    | SYNC      |              2 | Sync byte followed by frame type and version number (AA11 hex). |
| 2    | FRAMESIZE |              2 | Number of bytes in frame, defined in 6.2.                       |
| 3    | IDCODE    |              2 | PMU/PDC data stream ID number, 16-bit integer, defined in 6.2.  |
| 4    | SOC       |              4 | SOC time stamp, defined in 6.2.                                 |
| 5    | FRACSEC   |              4 | Fraction of Second and Time Quality, defined in 6.2.            |
| 6    | DATA 1    |              1 | ASCII character, 1st byte.                                      |
| K+6  | DATA k    |              1 | ASCII character, Kth byte, K>0 is an integer.                   |
| K+7  | CHK       |              2 | CRC-CCITT.                                                      |

## 6.6 Command frame

A data sending device (PMU or PDC) shall be able to receive commands and take appropriate actions. This Command Frame  uses  the  same  SYNC,  FRAMESIZE,  SOC,  FRACSEC,  and  CHK  words  as  all  other messages and is identified by bits 4-6 of the SYNC word as shown in Table 2. The command message frame is shown in Table 14. IDCODE shall be a 2-byte identification code assigned to a PMU/PDC data stream output and is the same as field 3 in the configuration frame. The CHK is the 16-bit CRC-CCITT described previously. The PMU/PDC shall match the IDCODE with a valid code stored internally before accepting and executing the command. The IDCODE for each output stream shall be user settable. The PMU/PDC  shall  match  the  command  code  with  that  of  a  configured  output  stream  and  execute  the command for the indicated data stream output, leaving other streams, if there are any, unchanged. CMD shall be a 2-byte command code as defined in 0.

Table 14 -Command frame organization

|   No | Field     | Size (bytes)   | Comment                                                                                            |
|------|-----------|----------------|----------------------------------------------------------------------------------------------------|
|    1 | SYNC      | 2              | Sync byte followed by frame type and version number (AA41 hex).                                    |
|    2 | FRAMESIZE | 2              | Number of bytes in frame, defined in 6.2.                                                          |
|    3 | IDCODE    | 2              | PMU/PDC ID data stream number, 16-bit integer, defined in 6.2.                                     |
|    4 | SOC       | 4              | SOC time stamp, defined in 6.2.                                                                    |
|    5 | FRACSEC   | 4              | Fraction of Second and Time Quality, defined in 6.2.                                               |
|    6 | CMD       | 2              | Command being sent to the PMU/PDC (0).                                                             |
|    7 | EXTFRAME  | 0-65518        | Extended frame data, 16-bit words, 0 to 65518 bytes as indicated by frame size, data user defined. |
|    8 | CHK       | 2              | CRC-CCITT.                                                                                         |

## Table 15 -Commands sent to the PMU/PDC

| Command word bits   | Definition                                               |
|---------------------|----------------------------------------------------------|
| Bits 15-0:          |                                                          |
| 0000 0000 0000 0001 | Turn off transmission of data frames.                    |
| 0000 0000 0000 0010 | Turn on transmission of data frames.                     |
| 0000 0000 0000 0011 | Send HDR frame.                                          |
| 0000 0000 0000 0100 | Send CFG-1 frame.                                        |
| 0000 0000 0000 0101 | Send CFG-2 frame.                                        |
| 0000 0000 0000 0110 | Send CFG-3 frame (optional command).                     |
| 0000 0000 0000 1000 | Extended frame.                                          |
| 0000 0000 xxxx xxxx | All undesignated codes reserved.                         |
| 0000 yyyy xxxx xxxx | All codes where yyyy ≠ 0 available for user designation. |
| zzzz xxxx xxxx xxxx | All codes where zzzz ≠ 0 reserved.                       |

## Annex A

(informative)

## Bibliography

Bibliographical references are resources that provide additional or helpful material but do not need to be understood or used to implement this standard. Reference to these resources is made for informational use only.

- [B1] IEEE Standards Dictionary: Glossary of Terms &amp; Definitions. 7
- [B2] IEEE Std 1012™-1998, IEEE Standard for Software Verification and Validation. 8, 9
- [B3] IEEE Std 1344™-1995, IEEE Standard for Synchrophasors for Power Systems.
- [B4] IEEE  Std  1588™-2008,  IEEE  Standard  for  a  Precision  Clock  Synchronization  Protocol  for Networked Measurement and Control Systems.
- [B5] IEEE  Std  C37.111™-1999,  IEEE  Standard  Common  Format  for  Transient  Data  Exchange (COMTRADE) for Power Systems.
- [B6] IEEE Std C37.118™-2005, IEEE Standard for Synchrophasors for Power Systems.
- [B7] IEEE Std C37.238™-2011, IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications.
- [B8] IRIG  Standard  200-04 -IRIG  Serial  Time  Code  Formats -September  2004,  Timing  Committee, Telecommunications  and  Timing  Group,  Range  Commanders  Council,  US  Army  White  Sands  Missile Range, NM.
- [B9] Tugal, D. A., and Tugal, O., Data Transmission, 2nd. ed. New York: McGraw-Hill, 1989.
- [B10] Wells,  R.  B., Applied  Coding  and  Information  Theory  for  Engineers. Upper  Saddle  River,  NJ: Prentice Hall, 1999.
- [B11] Wicker, S. B., Error Control Systems for Digital Communications and Storage. Upper Saddle River, NJ: Prentice Hall, 1995.
- [B12] Witzke,  K.  A.,  and  Leung,  C.,  'A  Comparison  of  Some  Error  Detecting  CRC  Code  Standards,' IEEE Transactions on Communications, Vol. COM-33, No. 9, September 1985, pp. 996-998.

7 The IEEE Standards Dictionary: Glossary of Terms &amp; Definitions is available at http://shop.ieee.org/

8 IEEE publications are available from the Institute of Electrical and Electronics Engineers, 445 Hoes Lane, Piscataway, NJ 08854, USA (http://standards.ieee.org).

9 The  IEEE  standards  or  products  referred  to  in  Annex  A  are  trademarks  owned  by  the  Institute  of  Electrical  and  Electronics Engineers, Incorporated.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Annex B

(informative)

## Cyclic redundancy codes

## CRC

Cyclic redundancy codes are used to verify (or at least indicate) that a set of data has not been corrupted. They are specified by a polynomial, the initial value of the shift registers, the direction the bits are shifted, and optionally a mask to be XORed with the final register values. The CRC commonly referred to as CRCCCITT is illustrated in Figure B.1.

## CRC-CCITT

This annex describes the CRC calculation used in this standard and commonly referred to as CRC-CCITT. It shall be noted, however, that the CRC-CCITT described here, and which is in common usage, does not seem to be specified in any CCITT/ITU standard. ITU-T Recommendation V.41 describes a very similar CRC calculation; however, that document proscribes a different initial value than is used in the common implementation  of  CRC-CCITT.  Other  ITU  documents  describe  CRC  calculations  using  the  same polynomial and initial conditions, but require a final XOR mask not used in CRC-CCITT.

## CRC-CCITT definition

Since no CCITT/ITU document could be found to describe the CRC calculation commonly referred to as CRC-CCITT, we define it as follows in conjunction with Figure B.1.

Figure B.1-CRC-CCITT encoder

<!-- image -->

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Polynomial

<!-- formula-not-decoded -->

## Initial condition

The Shift registers of Figure B.1 are initialized to 1.

## Final mask

No final mask is XORed with the final register values.

## CRC-CCITT properties

Three  important  properties  of  CRCs  are  often  discussed,  their  error  pattern  coverage,  their  burst  error detection capability, and the probability of an undetected error occurring.

## Error pattern coverage

Error pattern coverage λ is  defined as the ratio of the number of invalid bit patterns over the number of valid bit patterns.

<!-- formula-not-decoded -->

where k is  the  number  of  bits  in  the  message  excluding  the  CRC  value,  and n is  the  number  of  bits including the CRC value. Therefore, the error pattern coverage is solely a function of the size of the CRC value.

## Burst error detection

Another  important  property  of  CRCs  is  their  ability  to  detect  burst  errors.  Burst  errors  are  transient  or intermittent  corruptions  of  several  symbols  in  a  transmitted  data  stream.  By  definition,  there  can  be  no more than one burst error per message. For binary data, the burst spans all corrupted bits and is bounded by ones. In the following example, let V be an uncorrupted bit, 1 be a nonzero bit, and X be a corrupted bit, a zero, or a one with corrupted bits to both its left and right.

<!-- formula-not-decoded -->

Therefore, the burst error length of the above message is 6.

## Burst error detection probability of CRC-CCITT

Both Wells [B10] and Wicker [B11] show that the burst error detection probability of a 16-bit binary CRC is as follows 10 :

- ⎯ 100% of all bursts less &lt; 17 bits long
- ⎯ 99.997% of all bursts which are 17 bits long
- ⎯ 99.9985% of all bursts that are greater than 17 bits long

10 These burst error detection probabilities are valid when the order of transmitted data matches the order of the data during CRC calculation.

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Probability of an undetected error

The lower bound for the probability of an undetected error, over a noisy binary symmetric channel is given in Wicker [B11] as follows:

For any CRC code of length p used for error detection on the binary symmetric channel, the undetected error probability approaches 2 -p as the crossover probability and the dimension k of the code increases.

## Sample 'C' code calculation example

A number of algorithms are available for calculating the CRC-CCITT. Common and probably the fastest are look-up table routines. The following example is very compact, simple, and does not need a look-up table.

```
/* Compute CRC-CCITT. *Message is a pointer to the first character in the message; MessLen is the number of characters in the message (not counting the CRC on the end) */ uint16_t ComputeCRC(unsigned char *Message, unsigned char MessLen) { uint16_t crc=0xFFFF; uint16_t temp; uint16_t quick; int     i; for(i=0;i<MessLen;i++) { temp = (crc>>8) ^ Message[i]; crc <<= 8; quick = temp ^ (temp >> 4); crc ^= quick; quick <<=5; crc ^= quick; quick <<= 7; crc ^= quick; } return crc; }
```

## Examples

Table  B.1  contains  example  data,  shown  both  as  ASCII  characters  and  as  hexadecimal  values,  and  the resulting CRC value.

Table B.1-Example data

| ASCII data   | Equivalent hexadecimal data   | Resultant CRC value   |
|--------------|-------------------------------|-----------------------|
| ABCD         | 0x41 0x42 0x43 0x44           | 0xBFFA                |
| 123456       | 0x31 0x32 0x33 0x34 0x35 0x36 | 0x2EF4                |
| abc          | 0x61 0x62 0x63                | 0x514A                |

## Annex C

(informative)

## System communications considerations

## C.1 Communication bandwidth

This standard does not impose any restriction on the communication system or media itself. It defines four message  typesdata,  configuration,  header, and command -to and from a  PMU or  PDC for real-time synchrophasor communication. It also prescribes the message contents and format. These are detailed in Clause 6.

Typically,  the  receiving  device  requests  a  configuration  and  header  using  the  commands  at  startup  or  a configuration change only. Most of the time the data frame is transmitted continuously from the PMU or PDC at the designated reporting rate. Consequently the required bandwidth is determined by the data frame size, data rate, and communication overheads. The frame size is precisely described in this standard and varies depending on the number of phasors and analog and digital words included in the frame. Typical sizes vary from 40-70 bytes for frames from a single PMU to over 1000 bytes in a frame from a PDC with data from many PMUs. Table C.1 gives some examples in bits per second (bps) for some typical PMU configurations.  Note  that  the  communication  media  will  add  overhead,  which  can  be  considerable. Asynchronous serial communication adds 2 bits per byte (25% overhead) and TCP adds 44 bytes/frame, which can amount to more than 50% overhead.

Table C.1-Estimation of bandwidth requirements for example PMU configurations

| Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   | Transmission rate in bits per second (bps) for example messages using UDP/IP over Ethernet   |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| PMU reporting rate (data frames/second)                                                      | 10                                                                                           | 12                                                                                           | 15                                                                                           | 25                                                                                           | 30                                                                                           | 50                                                                                           | 60                                                                                           |
| Message content: 2 phasors, all quantities integer                                           | 6 720                                                                                        | 8 064                                                                                        | 10 080                                                                                       | 16 800                                                                                       | 20 160                                                                                       | 33 600                                                                                       | 40 320                                                                                       |
| Message content: 2 phasors, all quantities floating point                                    | 7 680                                                                                        | 9 216                                                                                        | 11 520                                                                                       | 19 200                                                                                       | 23 040                                                                                       | 38 400                                                                                       | 46 080                                                                                       |
| Message content: 12 phasors, all integer                                                     | 9 920                                                                                        | 11 904                                                                                       | 14 880                                                                                       | 24 800                                                                                       | 29 760                                                                                       | 49 600                                                                                       | 59 520                                                                                       |
| Message content: 12 phasors, 2 analog, 2 digital, all integer                                | 10 560                                                                                       | 12 762                                                                                       | 15 840                                                                                       | 26 400                                                                                       | 31 680                                                                                       | 52 800                                                                                       | 63 360                                                                                       |

## C.2 Communication delay

An interval of time is required to make a measurement, send the measurement data to a device that will use the measurement, and then use the data. This interval of time from when the signal has a certain value to when the measurement is consumed by the application is called delay in this subclause. The first aspect of this delay is in the measurement process. That includes the window over which data is gathered to make a measurement, the estimation method and filtering, and the time to process that data. The second aspect is the communication of the data including the time to send each bit of the message, the distance and type of communication, and various communication buffering, multiplexing, conversion processes. Finally the last aspect is the processing of the receiving device and application algorithms.

Delay in measurement is largely dependent on the processing window and filtering, which vary with the data reporting rate and the PMU class of service. Processing delays for calculating the measurement are

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

generally very small compared with other delays. Additional delays caused by servicing other processing needs such as a multifunction device may cause large interruptions or may be insignificant.

Communication delay starts with clocking the bits out of the PMU and is easily measured. With RS-232 serial this delay can be in the millisecond range, but at network speeds is insignificant. Once multiplexed onto a communication baseband, data travels at 0.6 to 0.99 times the speed of light. For example, data sent 500 mi would only be delayed 3 ms to 5 ms, a relatively small number that is predictable based on the communication network. However buffering, de-multiplex/multiplex points, forwarding, and routing can add tens to hundreds of milliseconds and may not be very predictable. Error detection/correction can add hundreds of milliseconds to seconds. Data concentration with delays allowed for data with various delays can also add seconds. Some typical values for delays are summarized in Table C.2.

Table C.2-Summary of delays' causes and typical ranges

| Cause of delay                                      | Typical range of delay   |
|-----------------------------------------------------|--------------------------|
| Sampling window (delay ½ of window)                 | 17 ms to100 ms           |
| Measurement filtering                               | 8 ms to 100 ms           |
| PMU processing                                      | 0.005 ms to 30 ms        |
| PDC processing &alignment                           | 2 ms to 2+ s             |
| Serializing output                                  | 0.05 ms to 20 ms         |
| Communication system I/O                            | 0.05 ms to 30 ms         |
| Communication distance                              | 3.4 µs/km to 6 µs/km     |
| Communication system buffering and error correction | 0.05 ms to 8 s           |
| Application input                                   | 0.05 ms to 5 ms          |

Note that while these are typical, actual values can be different and systems need to be evaluated on a caseby-case basis. The minimum overall delay one could anticipate is in the order of 20 ms (no added filtering). The maximum delay in a real-time system could be in the 10 s range or longer. A typical system from PMU to PDC will be in the 20 ms to 50 ms range. Each level above that will add some PDC processing and wait times, probably in the 30 ms to 80 ms range (and in addition to the PMU to PDC time). If delay in data delivery  is  critical  to  applications,  the  designers  need  to  examine  all  communication  aspects  they  are incorporating to make sure delivery time meets specifications and there are no unexpected delays.

## Annex D

(informative)

## Message examples

## D.1 Introduction

IEEE Std C37.118-2005 [B6] describes four message types: data,  configuration,  header, and command. The  configuration,  data,  and  command  messages  are  binary  messages,  and  the  header  message  is  in  a human-readable format.

This annex provides examples of the three binary message types. Command messages control the operation of the synchrophasor measurement device. Data messages contain the actual measurements. Configuration messages contain information required to decode the data messages.

In general, the data communication structure is designed to support the following requirements:

- a) Only  measured  and  computed  data  shall  be  transmitted  in  real  time.  Informational  data  shall  be transmitted only on request.
- b) All  real-time  data  shall  be  traceable  to  an  absolute  time  reference.  This  data  shall  be  in  the  most compact form possible to fit the available channel bandwidth. However, consideration shall be given to optimization of host computer hardware and software.
- c) A wide range of data transmission rates shall be supported.
- d) The format shall support bi-directional real-time control functions in a full-duplex communication mode.
- e) A mechanism to transmit bi-directional status information shall be provided.
- f) Data integrity checks shall be provided.
- g) The amount and type of data transmitted shall be user definable to adjust to the wide range of data requirements.

## D.2 Data message

Table D.1 contains an example data frame. Each row of the table contains a field of the message described in 6.2 and 6.3 of this standard. The first column contains the field name. The second column contains a brief  description  of  the  data  contained  in  the  field  (see  Clause  6  for  details).  The  third  column  contains specific example data. The fourth column contains the number of 8-bit bytes of data in the field. The fifth column contains the hexadecimal equivalent of the example data.

The time of this example is 9:00.016667 AM (UTC) on June 6, 2006. The data frame indicates a balanced 3-phase phase-to-neutral voltage of 134 000 V and a constant system frequency of 62.5 Hz. There are no triggers and the measurement was made referenced to a high quality time source.

Use the information contained in the configuration frame, shown in Table D.2, to decode this data frame. For example, the PHUNIT fields of the configuration frame indicate the scaling of the voltage phasors is 9.15527 (0xDF847) V per bit. The real part of the A phase voltage has a magnitude of 14 635 (0x392B) counts. Multiply 9.15527 V per count by 14 635 counts to get 133 987 V.

## Table D.1-Data message example

| Field     | Short description                                                                                                                                       | Example entry                                                                                    |   Size (bytes) | Hexadecimal value   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------|---------------------|
| SYNC      | Synchronization and Frame Format Field.                                                                                                                 | Data Frame, Version 1                                                                            |              2 | AA 01               |
| FRAMESIZE | Total number of bytes in this frame.                                                                                                                    | 52 bytes in this frame                                                                           |              2 | 00 34               |
| IDCODE    | PMU/PDC data stream ID number, 16-bit integer, 1-65534.                                                                                                 | 7734                                                                                             |              2 | 1E 36               |
| SOC       | Second count. (UNIX time, starting midnight 01-Jan-1970 neglecting leap seconds).                                                                       | 9:00 AMon 6/6/2006 = 1 149 580 800                                                               |              4 | 44 85 36 00         |
| FRACSEC   | Time of phasor measurement in microseconds with Time Quality.                                                                                           | Not a leap second, none pending; time locked. 16817 μ s after the second mark                    |              4 | 00 00 41 B1         |
| STAT      | Bit mapped flags: Data valid?, PMU OK?, PMU sync?, Data align by time?, PMU Trigger?, Reserved, Time Error, Trigger Cause                               | Data valid, no PMU error, PMU sync, data sorted by time stamp, no PMU trigger, best time quality |              2 | 00 00               |
| PHASORS   | Phasor data, 16-bit integer, rectangular format. The first two bytes contain the real part of the phasor and the second two contain the imaginary part. | VA = 14 635 ∠ 0 ° (= 134.0 kV ∠ 0 ° )                                                            |              4 | 39 2B 00 00         |
| PHASORS   | Phasor data, 16-bit integer, rectangular format. The first two bytes contain the real part of the phasor and the second two contain the imaginary part. | VB = 14 635 ∠ -120 ° (= 134.0 kV ∠ -120 ° )                                                      |              4 | E3 6A CE 7C         |
| PHASORS   | Phasor data, 16-bit integer, rectangular format. The first two bytes contain the real part of the phasor and the second two contain the imaginary part. | VC = 14 635 ∠ 120 ° (= 134.0 kV ∠ 120 ° )                                                        |              4 | E3 6A 31 83         |
| PHASORS   | Phasor data, 16-bit integer, rectangular format. The first two bytes contain the real part of the phasor and the second two contain the imaginary part. | I1 = 1092 ∠ 0 ° (= 500 A ∠ 0 ° )                                                                 |              4 | 04 44 00 00         |
| FREQ      | 16-bit signed integer. Frequency deviation from nominal in mHz.                                                                                         | +2500 mHz (nominal 60 Hz with measured 62.5 Hz)                                                  |              2 | 09 C4               |
| DFREQ     | ROCOF.                                                                                                                                                  |                                                                                                  |              2 | 00 00               |
| ANALOG    | 32-bit floating point.                                                                                                                                  | ANALOG1 = 100                                                                                    |              4 | 42 C8 00 00         |
| ANALOG    | 32-bit floating point.                                                                                                                                  | ANALOG2 = 1000                                                                                   |              4 | 44 7A 00 00         |
| ANALOG    | 32-bit floating point.                                                                                                                                  | ANALOG3 = 10000                                                                                  |              4 | 46 1C 40 00         |
| DIGITAL   | Digital data, 16-bit bit fields.                                                                                                                        | 0011 1100 0001 0010                                                                              |              2 | 3C 12               |
| CHK       | CRC-CCITT.                                                                                                                                              | -                                                                                                |              2 | D4 3F               |

## D.3 Configuration message

Use the configuration frame described in Table D.2 to decode the data frame of Table D.1. In the standard, 6.2  and 6.4  describe  the  format  of  the  fields  listed  in  each  row  of Table  D.2.  As  in  Table  D.1,  the  first column of Table D.2 contains the field names, the second column contains brief descriptions of the data in the fields, the third column contains example data, the fourth column indicates the number of bytes of data, and the last column shows the hexadecimal values of the example data.

## Table D.2-Configuration message example

| Field     | Short description                                          | Example                                                                                                               |   Size (bytes) | Hexadecimal value                               |
|-----------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------|
| SYNC      | Synchronization byte and version number.                   | Configuration Frame 2 Version 1                                                                                       |              2 | AA 31                                           |
| FRAMESIZE | Number of bytes in frame.                                  | This frame contains 454 bytes                                                                                         |              2 | 01 C6                                           |
| IDCODE    | PMU/PDC data stream ID number, 16-bit integer, 1-65534.    | 7734                                                                                                                  |              2 | 1E 36                                           |
| SOC       | SOC time stamp (UNIX time, starting midnight 01-Jan-1970). | 8:00 AMon 6/6/2006 = 1 149 577 200                                                                                    |              4 | 44 85 27 F0                                     |
| FRACSEC   | Fraction of second with Time Quality.                      | Leap second pending, to be deleted, clock unlocked but within 100 μ s. Fractional time is 0.463 s.                    |              4 | 56 07 10 98                                     |
| TIME_BASE | Flag and divisor for time stamping the data.               | 1 000 000 μ s                                                                                                         |              4 | 00 0F 42 40                                     |
| NUM_PMU   | The number of PMUs included in the data frame.             | Data from 1 PMU                                                                                                       |              2 | 00 01                                           |
| STN       | Station Name - 16 bytes in ASCII format.                   | The station name for this example is: 'Station A '                                                                    |             16 | 53 74 61 74 69 6F 6E 20 41 20 20 20 20 20 20 20 |
| IDCODE    | PMU/PDC data source ID number, 16-bit integer, 1-65534.    | 7734                                                                                                                  |              2 | 1E 36                                           |
| FORMAT    | Data format within the data frame.                         | Phasors are represented using rectangular coordinates and 16-bit integers. Analogs are 32-bit floating-point numbers. |              2 | 00 04                                           |
| PHNMR     | Number of phasors - 2 byte integer (0 to 32 767).          | This example contains 4 phasors.                                                                                      |              2 | 00 04                                           |
| ANNMR     | Number of analog values - 2 byte integer.                  | This example contains 3 analog values.                                                                                |              2 | 00 03                                           |
| DGNMR     | Number of digital status words - 2 byte integer.           | This example contains 1 set of binary data.                                                                           |              2 | 00 01                                           |

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Table D.2 -Configuration message example (continued)

| Field   | Short description                                                                                                                           | Example                                        |   Size (bytes) | Hexadecimal value                                           |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------|-------------------------------------------------------------|
| CHNAM   | Phasor and channel names - 16 bytes for each phasor, analog, and digital channel in ASCII format in the same order as they are transmitted. | The first phasor name is: 'VA '                |             16 | 56 41 20 20 20 20 20 20 20 20 20 20 20 20 20 20             |
|         |                                                                                                                                             | The second phasor name is: 'VB '               |             16 | 56 42 20 20 20 20 20 20 20 20 20 20 20 20 20 20             |
|         |                                                                                                                                             | The third phasor name is: 'VC '                |             16 | 56 43 20 20 20 20 20 20 20 20 20 20 20 20 20 20             |
|         |                                                                                                                                             | The fourth phasor name is: 'I1 '               |             16 | 49 31 20 20 20 20 20 20 20 20 20 20 20 20 20 20             |
|         |                                                                                                                                             | The first analog name is: 'ANALOG1 '           |             16 | 41 4E 41 4C 4F 47 31 20 20 20 20 20                         |
|         |                                                                                                                                             | The second analog name is: 'ANALOG2 '          |             16 | 20 20 20 20 41 4E 41 4C 4F 47 32 20 20 20 20 20 20 20 20 20 |
|         |                                                                                                                                             | The third analog name is: 'ANALOG3 '           |             16 | 41 4E 41 4C 4F 47 33 20 20 20 20 20 20 20 20 20             |
|         |                                                                                                                                             | Digital channel 1 label is: 'BREAKER 1 STATUS' |             16 | 42 52 45 41 4B 45 52 20 31 20 53 54 41 54 55 53             |
|         |                                                                                                                                             | Digital channel 2 label is: 'BREAKER 2 STATUS' |             16 | 42 52 45 41 4B 45 52 20 32 20 53 54 41 54 55 53             |
|         |                                                                                                                                             | Digital channel 3 label is: 'BREAKER 3 STATUS' |             16 | 42 52 45 41 4B 45 52 20 33 20 53 54 41 54 55 53             |
|         |                                                                                                                                             | Digital channel 4 label is: 'BREAKER 4 STATUS' |             16 | 42 52 45 41 4B 45 52 20 34 20 53 54 41 54 55 53             |
|         |                                                                                                                                             | Digital channel 5 label is: 'BREAKER 5 STATUS' |             16 | 42 52 45 41 4B 45 52 20 35 20 53 54 41 54 55 53             |

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

## Table D.2 -Configuration message example (continued)

| Field   | Short description                                                                                                              | Example                                         | Size (bytes)   | Hexadecimal value                                           |
|---------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|----------------|-------------------------------------------------------------|
|         |                                                                                                                                | Digital channel 6 label is: 'BREAKER 6 STATUS'  | 16             | 42 52 45 41 4B 45 52 20 36 20 53 54                         |
|         |                                                                                                                                | Digital channel 7 label is: 'BREAKER 7 STATUS'  | 16             | 41 54 55 53 42 52 45 41 4B 45 52 20 37 20 53 54             |
|         |                                                                                                                                | Digital channel 8 label is: 'BREAKER 8 STATUS'  | 16             | 41 54 55 53 42 52 45 41 4B 45 52 20 38 20 53 54 41 54 55 53 |
|         |                                                                                                                                | Digital channel 9 label is: 'BREAKER 9 STATUS'  | 16             | 42 52 45 41 4B 45 52 20 39 20 53 54 41 54 55 53             |
|         |                                                                                                                                | Digital channel 10 label is: 'BREAKER A STATUS' | 16             | 42 52 45 41 4B 45 52 20 41 20 53 54                         |
|         |                                                                                                                                | Digital channel 11 label is: 'BREAKER B STATUS' | 16             | 41 54 55 53 42 52 45 41 4B 45 52 20 42 20 53 54 41 54 55 53 |
|         |                                                                                                                                | Digital channel 12 label is: 'BREAKER C STATUS' | 16             | 42 52 45 41 4B 45 52 20 43 20 53 54 41 54 55 53             |
|         |                                                                                                                                | Digital channel 13 label is: 'BREAKER D STATUS' | 16             | 42 52 45 41 4B 45 52 20 44 20 53 54 41 54 55 53             |
|         |                                                                                                                                | Digital channel 14 label is: 'BREAKER E STATUS' | 16             | 42 52 45 41 4B 45 52 20 45 20 53 54 41 54 55 53             |
|         |                                                                                                                                | Digital channel 15 label is: 'BREAKER F STATUS' | 16             | 42 52 45 41 4B 45 52 20 46 20 53 54 41 54 55 53             |
|         |                                                                                                                                | Digital channel 16 label is: 'BREAKER G STATUS' | 16             | 42 52 45 41 4B 45 52 20 47 20 53 54 41 54 55 53             |
| PHUNIT  | Conversion factor for phasor channels. PhasorMAG = PHUNIT X× 0.00001 Voltage PHUNIT = (300 000/32768) × 10E+5 Current PHUNIT = | Factor = 915527 Factor = 45776                  | 4 4            | 00 0D F8 47 01 00 B2 D0                                     |
|         |                                                                                                                                | Factor = 915527                                 | 4              | 00 0D F8 47                                                 |
|         |                                                                                                                                | Factor = 915527                                 | 4              | 00 0D F8 47                                                 |

Table D.2 -Configuration message example (continued)

| Field     | Short description                                                                                                                             | Example                                                                       |   Size (bytes) | Hexadecimal value   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|----------------|---------------------|
| ANUNIT    | Conversion factor for analog channels. Because the analogs are represented by floating-point conversion factor is unity (or simply not used). | This analog is an 'instantaneous' sample of a point on the input waveform     |              4 | 00 00 00 01         |
| ANUNIT    | Conversion factor for analog channels. Because the analogs are represented by floating-point conversion factor is unity (or simply not used). | This analog is an rms calculation                                             |              4 | 01 00 00 01         |
| ANUNIT    | Conversion factor for analog channels. Because the analogs are represented by floating-point conversion factor is unity (or simply not used). | This analog is a peak calculation                                             |              4 | 02 00 00 01         |
| DIGUNIT   | Mask words for digital status words.                                                                                                          | First mask: Normal state is 0 for all bits Second mask: All 16 bits are valid |              4 | 00 00 FF FF         |
| FNOM      | Nominal line frequency code and flags.                                                                                                        | Nominal 60 Hz                                                                 |              2 | 00 00               |
| CFGCNT    | Configuration change count.                                                                                                                   | 22 changes                                                                    |              2 | 00 16               |
| DATA_RATE | Rate of phasor data transmissions.                                                                                                            | 30 messages per second                                                        |              2 | 00 1E               |
| CHK       | CRC-CCITT.                                                                                                                                    | -                                                                             |              2 | D5 D1               |

## D.4 Command message

Command messages affect the behavior of the PMU. They control the transmission of data, configuration, and  header  messages.  The  example  shown  in  Table  D.3  causes  a  PMU  to  begin  transmission  of  data messages. The fields shown are described in 6.2 and 6.6 of the standard.

Table D.3-Command message example

| Field     | Short description                                                                        | Example                                                                    |   Size (bytes) | Hexadecimal value   |
|-----------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------|---------------------|
| SYNC      | Synchronization byte and version number.                                                 | Command Message, Version 1                                                 |              2 | AA 41               |
| FRAMESIZE | Number of bytes in frame.                                                                | 18                                                                         |              2 | 00 12               |
| IDCODE    | Data stream ID number, 16-bit integer, 1-65534.                                          | 7734                                                                       |              2 | 1E 36               |
| SOC       | SOC time stamp.                                                                          | 12:00 AMon 6/6/2006 = 1 149 591 600                                        |              4 | 44 85 60 30         |
| FRACSEC   | Fraction of second with Time Quality.                                                    | No leap second pending or past, clock never locked, fractional time 0.77 s |              4 | 0F 0B BF D0         |
| CMD       | Defined commands are data on, data off, send header, send configuration, extended frame. | Turn on the data stream                                                    |              2 | 00 02               |
| CHK       | CRC-CCITT.                                                                               | -                                                                          |              2 | CE 00               |

## Annex E

(normative)

## Synchrophasor message mapping into communications

## E.1 Serial communications

The  messages  specified  in  Clause  6  shall  be  mapped  in  their  entirety  into  the  serial  communication interface. RS-232 is commonly sent byte by byte with various functions that access the serial interface. The entire  message  as  described  in  Clause  6  shall  be  written  in  the  order  described  to  the  serial  interface. Likewise, when received, it shall be read in its entirety from the serial interface. The serial communication system  may  apply  ordering  or  encoding  within  the  communication  system,  but  as  long  as  compatible devices are used at both ends, the data written into and read from the serial interface will be the same and in the same order. Figure E.1 illustrates this process.

Figure E.1-Phasor message transmission over serial communications

<!-- image -->

## E.2 Network communications using Internet protocol (IP)

Phasor  messages  shall  also  be  mapped  in  their  entirety  into  TCP  (as  defined  in  RFC  793)  or  UDP  (as defined  in  RFC  768).  They  shall  be  written  to  and  read  from  using  standard  IP  input-output  functions. Default port numbers shall be 4712 for TCP and 4713 for UDP, but in all cases, the user shall be provided the means to set port numbers as desired. The IP may be carried over Ethernet or another transport means. With a stacked protocol like IP, each message layer is encapsulated in the next one down to the transport layer where the message is sent. This process is illustrated in Figure E.2.

Figure E.2-Mapping of IEEE C37.118 data into a TCP or UDP packet -A transport layer header and trailer are shown, as it would be when using Ethernet

<!-- image -->

## Annex F

(informative)

## Synchrophasor communication methods for IP

## F.1 Communication introduction

Data  transmission  using  this  standard  is  a  real-time  method,  where  data  is  sent  immediately  after measurement  using  a  predefined  constant  interval.  Data  transmission  for  non-real-time  uses  and  other protocols will have different requirements that are not discussed here. Using this standard, synchrophasor data  can  be  carried  over  any  communication  system  that  has  sufficient bandwidth  and  allows  using  this message  structure.  The  required  bandwidth  will  be  dictated  by  the  reporting  rate  and  the  message  size. Originally, only RS-232 serial communications were used and the data was mapped directly into the serial API. As communications have evolved into network methods, synchrophasor communication has moved as well.  While  not  proscribed  by  the  standard,  several  common  methods  using  IP  have  evolved.  These methods have been followed by vendors and implementers. IP is widely used and commonly available, so these methods are easy to implement with standard equipment and easy to operate by IT personnel. These methods are described in the following subclauses.

Cyber  security  must  be  addressed  with  the  communications  used  to  transport  synchrophasor  data.  This annex  describes  only  methods  that  have  been  implemented  to  date  and  does  not  attempt  to  prescribe measures  that  may  be  applied  in  the  future.  Users  of  these  methods  need  to  be  aware  of  the  risks  of unsecured communications and should consider adopting more secure methods.

## F.2 Transmission using IP over Ethernet

Phasor  measurement  systems  most  commonly  use  the  IP  over  network  communications.  The  previous standard, IEEE Std C37.118-2005 [B6], as well as this standard require that if a stacked protocol such as IP is  used  for  transmitting  the  messages,  that  they  are  included  in  their  entirety  (all  parts  of  the  defined message is included). It further prescribes default ports for using communication by both TCP and UDP, though the user can specify any port assignment they prefer.

The common methods for communication are as follows:

- a) Client-server. The device providing data is the server and the device receiving data is the client. The device providing data can be a PMU, a PDC, or any other device that will output synchrophasor data. The device receiving data can be a PDC or any or other device that receives synchrophasor data.  In  cases  where  data  transmission  is  initiated  by  command,  the  client  initiates  contact  and controls data flow with commands
- b) Basic modes of operation: spontaneous and commanded. With spontaneous, the server sends data by UDP to a designated destination without stopping, whether a receiving device is present or not. The stream  is  initiated  by  a  function  in  the  device  accessed  separately  from  data  operations.  With commanded operation, the server only sends data when a client requests it using the standard Start and Stop commands. Both modes may support commands to retrieve configuration and header data.
- c) TCP,  UDP,  and  multicast  communication.  All  modes  are  supported  in  various  appropriate configurations.

## F.2.1 TCP-only method

This method has a single TCP connection over which commands, data, header, and configuration frames are passed. The client needs to know only the server address and port. The usual TCP data management advantages and benefits apply to all data. The link is easy to administer, troubleshoot, and manage. The main disadvantage is that with the high rate and continuous data transmission, a single dropped data packet can cause data backup in the TCP mechanism that causes an interval of data loss. If the data is recovered, all data will be delayed, which is often much worse for real-time applications than the loss of one packet. There is also more traffic generated by the return acknowledgements. TCP is a connection based protocol, thus is strictly a 1-to-1 connection, so if data is required for more than one client, it has to be sent separately to  each  destination.  This  increases  traffic  and  requires  the  PMU  to  support  multiple  TCP  connections. Another TCP disadvantage comes from the fact it requires two-way communication to make a connection; if security measures block incoming traffic from a protected zone, a TCP client will be unable to connect. Spontaneous UDP can operate with outgoing messages only and avoids this problem.

## F.2.2 UDP-only method

This  method  uses  straight  UDP  for  communication  in  both  directions  for  PMU  messages,  including commands, data, header, and configuration. The client must know the server address and port number. The server can respond to the client port or a different port by prior arrangement. The advantages of using UDP are reduced bandwidth requirements and elimination of a backup delay, due to dropouts as described for TCP in F.2.1. The disadvantage is that server-client communications are not confirmed so it is difficult to locate problems if the communications do not proceed as expected. With UDP, data is not retransmitted in case of error, so errored packets are permanently lost (unless a suitable recovery system is provided by the user). There also can be difficulty with controlling data streams since more than one client can access the connectionless  control  port.  If  data  is  sent  to  a  unicast  IP  address,  it  then  must  be  sent  to  each  client separately. Alternatively, data can be sent to a multicast IP address, allowing numerous clients to receive it, thus  minimizing  network  traffic.  However,  the  user  will  need  to  set  the  multicast  address  and  port separately since the command does not do this. The drawbacks to this method are real but mostly academic, and seem to cause no problems in operational systems.

## F.2.3 TCP/UDP method

This method uses TCP for commands, header, and configuration communications, and UDP for sending data. The server address and port must be known to the client, and the client port UDP port must be known to the server (PMU). If the UDP is sent by multicast, that address must be known to the server as well. The commands, header, and configuration communication is secured through the TCP link and the data is sent by UDP. This minimizes data transmission delay and does not risk backup, though data will not be replaced if corrupted. This method has the advantage of more secure transmission on the critical data portions, and minimal delay  or  backup  risk  on  the  streaming  data.  It  can  also  use  multicast  to  reduce  traffic  and  can support retrieving configuration information without interrupting the data transmission. It is probably the most complete of the phasor communication methods. The disadvantage is that the server must know the destination port in advance

## F.2.4 Spontaneous data transmission method

With this method, a PMU, PDC, or other data serving device sends out data in the IEEE C37.118 format to a preset destination continuously. The data is sent by UDP and can be unicast, multicast, or broadcast. The output is initiated by a device setting or device interface-not through the IEEE C37.118 command set. To be compliant with the standard, command functionality must be provided. While this will make the device technically non-compliant, the user may prefer the benefits of this operation. Since the data is sent by UDP, a destination device does not have to be present. This mode is useful for sending data using multicast to

## IEEE Standard for Synchrophasor Data Transfer for Power Systems

many clients that may be coming online and offline randomly. It allows a steady supply of data without interruption,  and  can  be  used  where  two  way  communication  is  prohibited,  such  as  through  a  firewall. Header and configuration information retrieval may be allowed on the same or a different channel.. In some cases, a configuration frame is sent spontaneously at a preset interval, such as once a minute, along with the data. The drawback to this method is lack of ability to turn the data stream on and off, and possibly limited ability for a client to retrieve configuration information using normal IEEE  C37.118 methods. Accountability can be difficult to implement, as there is no way to tell who is listening to the data stream. This method is generally used over a small private or secured network.