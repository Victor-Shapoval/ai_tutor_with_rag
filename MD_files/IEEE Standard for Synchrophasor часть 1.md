<!-- image -->

## IEEE Standard for Synchrophasor Measurements for Power Systems

## IEEE Power &amp; Energy Society

Sponsored by the Power System Relaying Committee

## IEEE Standard for Synchrophasor Measurements for Power Systems

Sponsor

## Power System Relaying Committee of the IEEE Power &amp; Energy Society

Approved 7 December 2011

## IEEE-SA Standards Board

Abstract: Synchronized phasor (synchrophasor) measurements for power systems are presented.  This  standard  defines  synchrophasors,  frequency,  and  rate  of  change  of  frequency (ROCOF) measurement under all operating conditions. It specifies methods for evaluating these measurements and requirements for compliance with the standard under both steady-state and dynamic  conditions.  Time  tag  and  synchronization  requirements  are  included.  Performance requirements are confirmed with a reference model, provided in detail. This document defines a phasor measurement unit (PMU), which can be a stand-alone physical unit or a functional unit within another physical unit. This standard does not specify hardware, software, or a method for computing phasors, frequency, or ROCOF.

Keywords: data concentrator, DC, FE, frequency error, IEEE C37.118.1, IRIG-B, PDC, phasor, phasor measurement, phasor measurement unit, PMU, RFE, ROCOF, ROCOF  error, synchronized phasor, synchrophasor, total vector error, TVE

•

The Institute of Electrical and Electronics Engineers, Inc.

3 Park Avenue, New York, NY 10016-5997, USA

Copyright © 2011 by the Institute of Electrical and Electronics Engineers, Inc. All rights reserved. Published 28 December 2011. Printed in the United States of America.

IEEE is a registered trademark in the U.S. Patent &amp; Trademark Office, owned by the Institute of Electrical and Electronics Engineers, Incorporated.

PDF:

ISBN 978-0-7381-6811-1

STD97167

Print:

ISBN 978-0-7381-6812-8

STDPD97167

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

This introduction is not part of IEEE Std C37.118.1-2011, IEEE Standard for Synchrophasor Measurements for Power Systems.

The original synchrophasor standard was IEEE Std 1344™-1995 [B5]. a It was replaced by IEEE Std C37.118-2005 [B8]. This has now been split into two standards: IEEE Std 37.118.1-2011 (this standard), covering measurement  provisions, and IEEE  Std 37.118.2™-2011  [B9],  covering data communication. Both standards contain the previous material with updates and additional provisions.

In this standard, additional clarification is provided for the phasor and synchronized phasor definitions. The concepts of total vector error (TVE) and compliance tests are retained and expanded, tests over temperature variation have been added, and dynamic performance tests have been introduced. In addition, limits and characteristics  of  frequency  measurement  and  rate  of  change  of  frequency  (ROCOF)  measurement  have been developed. Annex C includes a system model intended to verify the ability to implement the required performance measures. The model is meant as a reference benchmark only; it is assumed that many real implementations will surpass this model in performance.

Phasors are used in many protection and data acquisition functions. By referencing them to a common time base  they  become  comparable  over  a  wide  area  of  measurement.  A  synchrophasor  is  a  phasor  value obtained from voltage or current waveforms and precisely referenced to a common time base. Simultaneous measurement sets derived from synchronized phasors provide a vastly improved method for tracking power system dynamic phenomena for improved power system monitoring, protection, operation, and control.

The intent of any instrument connected to the power grid is to monitor power system parameters. The intent of  this  standard  is  to  describe  and  quantify  the  performance  of  the phasor  measurement  unit (PMU) instrument deployed to monitor the power grid. The PMU extracts the parameters magnitude, phase angle, frequency, and ROCOF from the signals appearing at its input terminals. These signals may be corrupted by  harmonic  content,  noise,  and  changes  in  state  caused  by  system  loads,  and  control  and  protective actions.  Some  examples  are  harmonics  introduced  by  large  non-linear  loads,  step  changes  in  phase introduced by switched reactive elements, and random noise from arc furnaces. These artifacts complicate the  process  of  measuring  the  generation  and  load  characteristics  at  or  near  the  system  fundamental frequency.

The  filtering  associated  with  the  computation  of  the  synchrophasors  rejects  the  undesirable  signal components appearing at the PMU input within the limits provided by the filter attenuation. The frequency is  computed  as  the  first  derivative  of  the  synchrophasor  phase  angle,  and  ROCOF  is  computed  as  the second derivative of the same phase angle. These two quantities are less reliable measurements, particularly ROCOF, because  they  are  more  sensitive  to  undesirable  components  in  the  signal  like  harmonics,  offnominal components, or noise.

This standard presents a set of PMU performance requirements to ensure that compliant instruments will perform similarly when presented with this suite of test signals. The user shall be aware that in the presence of the previously mentioned undesirable components in the input signal, higher measurement errors could result. These errors may be substantial, particularly where higher order derivatives (such as ROCOF) are used. Signal processing alternatives may be employed to reduce or eliminate these errors. They are difficult to  implement  in  a  real-time  environment  and  could  adversely  affect  the  measurement  latency  or  the synchrophasor  measurement  response  time.  Alternatives  are  neither  described  nor  evaluated  in  this document.

a The numbers in brackets correspond to those of the bibliography in Annex A.

## Notice to users

## Laws and regulations

Users  of  these  documents  should  consult  all  applicable  laws  and  regulations.  Compliance  with  the provisions  of  this  standard  does  not  imply  compliance  to  any  applicable  regulatory  requirements. Implementers  of  the  standard  are  responsible  for  observing  or  referring  to  the  applicable  regulatory requirements.  IEEE  does  not,  by  the  publication  of  its  standards,  intend  to  urge  action  that  is  not  in compliance with applicable laws, and these documents may not be construed as doing so.

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

At the time this standard was submitted to the IEEE-SA Standards Board for approval, the Synchrophasor Measurements for Power Systems Working Group had the following membership:

## Kenneth Martin , Chair Bogdan Kasztenny , Vice Chair

| Mark Adamiak      | Juan Gers        | Krish Narendra   |
|-------------------|------------------|------------------|
| Scott Anderson    | Allen Goldstein  | Arun Phadke      |
| Galina Antonova   | Hank Hechun      | Tevfik Sezi      |
| Miroslav Begovic  | Yi Hu            | Veselin Skendzic |
| Gabriel Benmouyal | Mladen Kezunovic | Jerry Stenbakken |
| Gustavo Brunello  | Harold Kirkham   | Eric Udren       |
| Bill Dickerson    | Jay Murphy       | John Wang        |

The following members of the individual balloting committee voted on this standard. Balloters may have voted for approval, disapproval, or abstention.

| William J. Ackerman   | Roger Hedding        | Farnoosh Rahmatian         |
|-----------------------|----------------------|----------------------------|
| Mark Adamiak          | Jerry Hohn           | Michael Roberts            |
| Eric Allen            | C. Huntley           | Charles Rogers             |
| M. Victoria Alonso    | Gerald Johnson       | Miriam Sanders             |
| Galina Antonova       | Innocent Kamwa       | Steven Sano                |
| James Ariza           | Bogdan Kasztenny     | Bartien Sayogo             |
| Jack Arnold           | Yuri Khersonsky      | Thomas Schossig            |
| Ali Al Awazi          | James Kinney         | Robert Seitz               |
| David Bassett         | Joseph L. Koepfinger | Jose Antonio De La O Serna |
| Philip Beaumont       | Jim Kulchisky        | Gil Shultz                 |
| Kenneth Behrendt      | Chung-Yiu Lam        | Mark Simon                 |
| Oscar Bolado          | Raluca Lascu         | Veselin Skendzic           |
| Gustavo Brunello      | Kenneth Martin       | James Smith                |
| Arvind K. Chaudhary   | Pierre Martin        | Jerry Smith                |
| Luis Coronado         | John McDonald        | Gary Stoedter              |
| Randall Crellin       | Michael McDonald     | Charles Sufana             |
| Gary Donner           | Harish Mehta         | Richard Taylor             |
| Michael Dood          | Gary Michel          | William Taylor             |
| Randall Dotson        | Adi Mulawarman       | Demetrios Tziouvaras       |
| Gary Engmann          | Jerry Murphy         | Joe Uchiyama               |
| Herbert Falk          | R. Murphy            | Eric Udren                 |
| Fredric Friend        | Bruce Muschlitz      | John Vergis                |
| Vasudev S. Gharpure   | Michael S. Newman    | Ilia Voloh                 |
| Jeffrey Gilbert       | Mohamed Omran        | Roel Vries                 |
| Mietek Glinkowski     | Dean Ouellette       | John Wang                  |
| Jalal Gohari          | Lorraine Padden      | Kenneth White              |
| Allen Goldstein       | Donald Parker        | Thomas Wiedman             |
| Roman Graf            | Mark Peterson        | Ray Young                  |
| Stephen Grier         | Robert Pettigrew     | Jian Yu                    |
| Randall C. Groves     | Bruce Pickett        | Sergio Zimath              |

When the IEEE-SA Standards Board approved this standard on 7 December 2011, it had the following membership:

Richard H. Hulett ,

Chair

John Kulick ,

Vice Chair

Robert M. Grow

, Past Chair

Judith Gorman ,

Secretary

| Masayuki Ariyoshi   | Jim Hughes            | Gary Robinson      |
|---------------------|-----------------------|--------------------|
| William Bartley     | Joseph L. Koepfinger* | Jon Walter Rosdahl |
| Ted Burse           | David J. Law          | Sam Sciacca        |
| Clint Chaplin       | Thomas Lee            | Mike Seavey        |
| Wael Diab           | Hung Ling             | Curtis Siller      |
| Jean-Philippe Faure | Oleg Logvinov         | Phil Winston       |
| Alexander Gelman    | Ted Olsen             | Howard L. Wolfman  |
| Paul Houzé          |                       | Don Wright         |

*Member Emeritus

Also included are the following nonvoting IEEE-SA Standards Board liaisons:

Satish K. Aggarwal, NRC Representative Richard DeBlasio, DOE Representative Michael Janezic, NIST Representative

Don Messina IEEE Standards Program Manager, Document Development

Soo H. Kim IEEE Standards Project Manager

## Contents

| 1. Overview ....................................................................................................................................................   | 1                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1 Scope ...................................................................................................................................................      | 1                                                                                                                                             |
| 1.2 Purpose ................................................................................................................................................       | 1                                                                                                                                             |
| 1.3 General overview.................................................................................................................................              | 2                                                                                                                                             |
| 1.4 Need for this standard..........................................................................................................................               | 2                                                                                                                                             |
| 2. Normative references..................................................................................................................................          | 3                                                                                                                                             |
| 3. Definitions, acronyms, and abbreviations ..................................................................................................                     | 3                                                                                                                                             |
| 3.1 Definitions                                                                                                                                                    | ........................................................................................................................................... 3 |
| 3.2 Special terms........................................................................................................................................          | 4                                                                                                                                             |
| 3.3 Acronyms and abbreviations ...............................................................................................................                     | 4                                                                                                                                             |
| 4. Synchrophasor measurement......................................................................................................................                 | 5                                                                                                                                             |
| 4.1 Phasor definition..................................................................................................................................            | 5                                                                                                                                             |
| 4.2 Synchrophasor definition.....................................................................................................................                  | 5                                                                                                                                             |
| 4.3 Measurement time synchronization.....................................................................................................                          | 7                                                                                                                                             |
| 5. Synchrophasor measurement requirements and compliance verification...................................................                                           | 8                                                                                                                                             |
| 5.1 Synchrophasor estimation....................................................................................................................                   | 8                                                                                                                                             |
| 5.2 Frequency and rate of change of frequency estimation .......................................................................                                   | 8                                                                                                                                             |
| 5.3 Measurement evaluation......................................................................................................................                   | 9                                                                                                                                             |
| 5.4 Measurement reporting......................................................................................................................                    | 10                                                                                                                                            |
| 5.5 Measurement compliance..................................................................................................................                       | 12                                                                                                                                            |
| B (informative) Time tagging and dynamic response.......................................................................                                           | 25                                                                                                                                            |
| Annex                                                                                                                                                              |                                                                                                                                               |
| Annex C (informative) Reference signal processing models .......................................................................                                   | 29                                                                                                                                            |
| Annex D (informative) Time and synchronization communication.............................................................                                          | 38                                                                                                                                            |
| Annex E (informative) TVE evaluation and PMU testing............................................................................                                   | 44                                                                                                                                            |
| Annex F (informative) Generator voltage and power angle measurement...................................................                                             | 48                                                                                                                                            |

## IEEE Standard for Synchrophasor Measurements for Power Systems

IMPORTANT  NOTICE:  This  standard  is  not  intended to ensure safety, security, health, or environmental  protection.  Implementers  of  the  standard  are  responsible  for  determining  appropriate safety, security, environmental, and health practices or regulatory requirements.

This  IEEE  document  is  made  available  for  use  subject  to  important  notices  and  legal  disclaimers. These notices and disclaimers appear in all publications containing this document  and  may be found under the heading 'Important Notice' or 'Important Notices and Disclaimers Concerning  IEEE  Documents.'  They  can  also  be  obtained  on  request  from  IEEE  or  viewed  at http://standards.ieee.org/IPR/disclaimers.html.

## 1. Overview

## 1.1 Scope

This standard is for synchronized phasor measurement systems in power systems. It defines a synchronized phasor (synchrophasor), frequency, and rate of change of frequency (ROCOF) measurements. It describes time  tag  and  synchronization  requirements  for  measurement  of  all  three  of  these  quantities.  It  specifies methods for evaluating these measurements and requirements for compliance with the standard under both static and dynamic conditions. It defines a phasor measurement unit (PMU), which can be a stand-alone physical unit or a functional unit within another physical unit. This standard does not specify hardware, software, or a method for computing phasors, frequency, or ROCOF.

## 1.2 Purpose

This standard defines synchronized phasor and frequency measurements in substations along with methods and requirements for measurement verification. Measurements compliant with the standard and taken at various locations in the power system can be readily and accurately combined for power system analysis and operations. Time tag and other essential associations are also described to facilitate communication and reliable  data  application.  Communication  and  recording  of  phasor  measurements  are  covered  in  other standards, such as the companion standard IEEE Std C37.118.2™-2011 [B9]. 1

1 The numbers in brackets correspond to those of the bibliography in Annex A.

## IEEE Standard for Synchrophasor Measurements for Power Systems

## 1.3 General overview

This  standard  covers  synchronized  phasor  measurements  used  in  electric  power  systems.  It  defines  the measurement, provides methods of quantifying the measurements, defines performance tests, and specifies acceptable limits. The following clauses are provided:

- ⎯ Clause 1 provides the scope and needs for the standard.
- ⎯ Clause 2 references other standards that are related or may be useful in the study and application of this standard.
- ⎯ Clause 3 defines terms and abbreviations found in this standard.
- ⎯ Clause 4 defines the measurement.
- ⎯ Clause  5  defines  measurement  requirements,  a  method  of  quantifying  the  measurement,  a  test method, and accuracy limits.

Six  informative  annexes  are  also  provided  to  clarify  the  standard  and  give  supporting  information,  as follows:

- ⎯ Annex A is a bibliography.
- ⎯ Annex B explores the effects of time tagging and transient response relevant to this measurement technique.
- ⎯ Annex C provides the algorithms that were used to confirm the performance requirements.
- ⎯ Annex D discusses time synchronization.
- ⎯ Annex E explains the total vector error (TVE) concept of measurement quality and gives plots of error results.
- ⎯ Annex F describes two methods that can be used for measuring the internal voltages and power angles of generators.

## 1.4 Need for this standard

The 2005 version of the standard, commonly followed by equipment manufacturers and system integrators, specifies  the  performance  of  phasor  measurements  only  under  steady-state  conditions.  Synchrophasor applications, particularly during severe system disturbances, will utilize dynamic synchronized measurements. This revision of the standard extends the synchrophasor definition and specifies measurement requirements and test conditions to include practical dynamic power system conditions.

The original synchrophasor standard, IEEE Std 1344™-1995 [B5], and its successor, IEEE Std C37.118™2005  [B8],  provide  for  reporting  of  system  frequency  and  rate  of  change  of  system  frequency.  These quantities are not defined, however, and no measurement requirements are mandated.

This revision provides definition and measurement requirements for power system frequency and ROCOF under  practical  power  system  conditions.  A  number  of  issues  in  the  standard  have  been  identified  that require  clarification  or  modification.  This  revision  also  separates  the  measurement  and  communication subclauses of IEEE Std C37.118-2005 [B8] into individual standards. This simplifies widespread adoption and aids deployment by allowing freer use of other standards for synchrophasor communication.

## IEEE Standard for Synchrophasor Measurements for Power Systems

## 2. Normative references

The following referenced documents are indispensable for the application of this document (i.e., they must be understood and used, so each referenced document is cited in text and its relationship to this document is explained). For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments or corrigenda) applies.

IEEE Std 754™-1985, IEEE Standard for Binary Floating-Point Arithmetic. 2, 3

## 3. Definitions, acronyms, and abbreviations

For  the  purposes  of  this  document,  the  following  terms  and  definitions  apply.  The IEEE  Standards Dictionary: Glossary of Terms &amp; Definitions [B2] should be consulted for terms not defined in this clause. 4

## 3.1 Definitions

anti-aliasing: The process of filtering a signal before sampling to remove components of that signal whose frequency is equal to or greater than the Nyquist frequency (one-half the sample rate). If not removed, these signal components would appear as a lower frequency component (an alias).

Coordinated Universal Time (UTC): (Initials are ordered based on French language.) The time of day at the  Earth's  prime  meridian  (0°  longitude).  It  is  distributed  by  various  media,  including  the  Global Positioning System (GPS) system.

data concentrator (DC): A device that combines data from several measurement devices.

frequency  error  (FE): The  measure  of  error  between  the  theoretical  frequency  and  the  measured frequency for the given instant of time.

Global Positioning System (GPS): A U.S. Department of Defense (DoD) navigation system that uses a constellation of 24 satellites broadcasting a precision signal for location and time synchronization. Basic time synchronization accuracy is ± 0.2 microseconds ( μ s).

IEEE floating point: A 32-bit representation of a real number.

NOTE-This definition is in accordance with IEEE Std 754-1985. 5

leap second: A positive or negative one-second adjustment to the Coordinated Universal Time (UTC) that keeps it close to mean solar time.

Nyquist frequency: A  frequency that is one-half the sampling frequency of a discrete signal processing system.

Nyquist rate: A  sampling  rate  that  is  twice  the  bandwidth  of  a  band-limited  signal.  It  is  the  minimum sample rate that will result in an alias-free representation of a signal. It must therefore be greater than twice the highest frequency component in the signal.

2 IEEE publications are available from the Institute of Electrical and Electronics Engineers, 445 Hoes Lane, Piscataway, NJ 08854, USA (http://standards.ieee.org).

3 The IEEE standards or products referred to in Clause 2 are trademarks owned by the Institute of Electrical and Electronics Engineers, Incorporated.

4 The IEEE Standards Dictionary: Glossary of Terms &amp; Definitions is available at http://shop.ieee.org/.

5

Information on references can be found in Clause 2.

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

phasor: A complex equivalent of a sinusoidal wave quantity such that the complex modulus is the cosine wave amplitude, and the complex angle (in polar form) is the cosine wave phase angle.

phasor data concentrator (PDC): A data concentrator (DC) used in phasor measurement systems.

rate  of  change  of  frequency  (ROCOF)  error  (RFE): The  measure  of  error  between  the  theoretical ROCOF and the measured ROCOF for the given instant of time.

synchronism: The  state  in  which  connected  alternating-current  systems,  machines,  or  a  combination operate at the same frequency, and in which the phase angle displacements between voltages in them are constant or vary about a steady and stable average value.

synchronized phasor or synchrophasor: A  phasor  calculated  from  data  samples  using  a  standard time signal as the reference for the measurement.

NOTE-In this standard, the phasors from remote sites have a defined common phase relationship.

total vector error (TVE): The measure of error between the theoretical phasor value of the signal being measured and the phasor estimate.

NOTE-See 5.2.

## 3.2 Special terms

frame: In this standard, a data frame or a frame of data is a set of synchrophasor, frequency, and ROCOF measurements that  corresponds  to  the  same  time  stamp.  The  term frame is  used  to  differentiate  it  from samples, which are understood as points on an analog waveform.

phasor  measurement  unit  (PMU): In  this  standard,  a  device  that  produces  synchronized  phasor, frequency,  and  ROCOF  estimates  from  voltage  and/or  current  signals  and  a  time  synchronizing  signal. Note  that  the  same  device  may  perform  other  functions  and  include  another  functional  name  [e.g.,  the device may also record power system waveforms and be called a digital fault recorder (DFR)].

## 3.3 Acronyms and abbreviations

| BCD    | binary coded decimal                                                                                                                                                                                             |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DoD    | U.S. Department of Defense                                                                                                                                                                                       |
| f 0    | system nominal frequency, either 50 Hz or 60 Hz                                                                                                                                                                  |
| f in   | Input frequency of the fundamental; this is the frequency of the measurement input that is normally at or very close to nominal (50 Hz or 60 Hz) but may vary considerably during major disturbances or testing. |
| fps    | frames per second, the rate that frames of synchrophasor data are transmitted                                                                                                                                    |
| F s    | frequency of measurement data reporting, in frames per second (fps)                                                                                                                                              |
| IRIG-B | InterRange Instrumentation Group Time Code Format B                                                                                                                                                              |
| PPS    | pulse per second                                                                                                                                                                                                 |
| rms    | root mean square                                                                                                                                                                                                 |

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

ROCOF

rate of change of frequency

SBS

straight binary seconds

SCADA

Supervisory Control and Data Acquisition

SOC

second of century

THD

total harmonic distortion

## 4. Synchrophasor measurement

## 4.1 Phasor definition

Phasor representation of sinusoidal signals is commonly used in ac power system analysis. The sinusoidal waveform defined in Equation (1):

<!-- formula-not-decoded -->

is commonly represented as the phasor as shown in Equation (2):

<!-- formula-not-decoded -->

where the magnitude is the root-mean-square (rms) value, X m / √ 2, of the waveform, and the subscripts r and i signify real and imaginary parts of a complex value in rectangular components. The value of φ depends on the  time  scale,  particularly  where t =  0.  It  is  important  to  note  this  phasor  is  defined  for  the  angular frequency ω ; evaluation with other phasors must be done with the same time scale and frequency.

## 4.2 Synchrophasor definition

The synchrophasor representation of the signal x ( t ) in Equation (1) is the value X in Equation (2) where φ is the instantaneous phase angle relative to a cosine function at the nominal system frequency synchronized to UTC.

Under this definition, φ is the offset from a cosine function at the nominal system frequency synchronized to UTC. A cosine has a maximum at t = 0, so the synchrophasor angle is 0 degrees when the maximum of x ( t )  occurs  at  the  UTC  second  rollover  (1  PPS  time  signal),  and  -90  degrees  when  the  positive  zero crossing occurs at the UTC second rollover (sin waveform). Figure 1 illustrates the phase angle/UTC time relationship.

## IEEE Standard for Synchrophasor Measurements for Power Systems

Figure 1  -Convention for synchrophasor representation

<!-- image -->

The sinusoid is shown in Equation (3):

<!-- formula-not-decoded -->

where f 0  is  the nominal angular system frequency (50 Hz or 60 Hz) directly represented by the phasor in Equation (2). In the general case where the amplitude is a function of time X m( t ) and the sinusoid frequency is also a function of time f(t) , we can define the function g = f -f 0 where f 0 is the nominal frequency and g is the difference between the actual and nominal frequencies (note that g will also be a function of time, e.g., g(t) = f(t) -f 0. The sinusoid can then be written as shown in Equation (4):

<!-- formula-not-decoded -->

The synchrophasor representation for this waveform is shown in Equation (5):

<!-- formula-not-decoded -->

For  the  special  case  where X m( t )  = X m  is  constant  and g = Δ f is  a  constant  offset  from  the  nominal frequency, ∫ g ( t ) d t = ∫ Δ f d t = Δ f t so the synchrophasor is simply as shown in Equation (6):

<!-- formula-not-decoded -->

that will rotate at the uniform rate Δ f , the difference between the actual and off-nominal frequency.

This concept is illustrated in Figure 2. Consider that a sinusoid off-nominal system frequency is observed at intervals  {0, T 0 ,  2 T 0 ,  3 T 0 ,..,n T 0, …}  where T 0 ,=  1/ f 0  (the  nominal  power  system  period)  and  the corresponding phasor representations are { X 0 , X 1 , X 2 , X 3, … X n, … }. If the sinusoid frequency f ≠ f 0 and f &lt; 2 f 0,  the observed phasor will have a constant magnitude, but the phase angles of the sequence of phasors { X 0 , X 1 , X 2 , X 3, … X n, … } will change uniformly at a rate 2 π ( f -f 0 ) T 0 , as illustrated. If these values were reported  over  time,  they  would  continuously  increase  until  they  reached  180  degrees  where  they  would wrap around to -180 degrees and continue to increase as shown in Figure 3 (synchrophasors are commonly reported in angles -180 degrees to +180 degrees rather than 0 to 360 degrees).

Figure 2  -A sinusoid with a frequency f &gt; f 0 is observed at instants that are T 0 seconds apart -the phase angle Φ increases uniformly in relation to the frequency difference, f -f 0

<!-- image -->

Figure 3  -Sampling a power frequency sinusoid at off-nominal frequency

<!-- image -->

Several details of the synchrophasor definition shall be emphasized. All measurements are on a common time base and related to a common frequency, so the phase angle measurements are directly comparable. Differences in the actual frequency are included in the phase angle estimation. The synchrophasor estimate also includes the effects of all other signal contributions such as oscillations and local frequency swings. Synchrophasors are functions of time and will change from one value to the next unless the signal is a pure sinusoid at nominal system frequency. A precise time reference (clock) is required to provide the UTC time to determine the phase angle φ .

## 4.3 Measurement time synchronization

The  PMU  shall  be  capable  of  receiving  time  from  a  reliable  and  accurate  source,  such  as  the  Global Positioning System (GPS), that can provide time traceable to UTC with sufficient accuracy to keep the total vector error (TVE), the frequency error (FE), and the rate of change of frequency (ROCOF) error (RFE) within the required limits. All measurements shall be synchronized to UTC time with accuracy sufficient to meet the requirements of this standard. Note that a time error of 1 µs corresponds to a synchrophasor phase

## IEEE Standard for Synchrophasor Measurements for Power Systems

error of 0.022 degrees for a 60 Hz system and 0.018 degrees for a 50 Hz system. A phase error of 0.57 degrees (0.01 radian) will by itself cause 1% TVE as defined in Equation (12). This corresponds to a time error of ± 26 μ s for a 60 Hz system and ± 31 μ s for a 50 Hz system. A time source FE of 0.083 MHz in a 60 Hz system or 0.1 MHz in a 50 Hz system will cause the maximum allowed steady-state FE of 0.005 Hz. Similarly,  a  time  source  with  a  varying  frequency  will  cause  a  corresponding  error  in  ROCOF  (the relationship  is  not  as  direct  as  those  above).  A  time  source  that  reliably  provides  time,  frequency,  and frequency  stability  at  least  10  times  better  than  these  values  corresponding  to  1%  TVE  is  highly recommended. The time source shall also provide an indication of traceability  to  UTC  and  leap  second changes.

For each measurement, the PMU shall assign a time tag that includes the time and time quality at the time of  measurement.  The  time  tag  shall  accurately  resolve  time  of  measurement  to  at  least  1 μ s  within  a specified 100 year period. The time status shall include time quality that clearly indicates traceability to UTC, time accuracy, and leap second status. Time and time quality for reporting and recording shall be derived from the PMU time tag and converted to the format and content as required.

## 5. Synchrophasor measurement requirements and compliance verification

## 5.1 Synchrophasor estimation

A PMU shall calculate and be capable of reporting synchrophasor estimates as defined and described in Clause 4 The estimates shall include single phase or positive sequence synchrophasors, or both. Provision shall be made for the user selection of the measured values. Measurement accuracy, reporting times, and evaluation criteria are given in this clause. Note that measurements are actually estimates of a certain value; the terms measurement and estimate are used somewhat interchangeably in this standard.

## 5.2 Frequency and rate of change of frequency estimation

A  PMU  shall  calculate  and  be  capable  of  reporting  frequency  and  ROCOF.  For  this  measurement,  the following standard definitions shall be used. Given a sinusoidal signal, as shown in Equation (7):

<!-- formula-not-decoded -->

Frequency is defined as shown in Equation (8):

<!-- formula-not-decoded -->

The ROCOF is defined shown in Equation (9):

<!-- formula-not-decoded -->

Synchrophasors  are  always  computed  in  relation  to  the  system  nominal  frequency  ( f 0 ).  If  the  cosine argument is represented as ψ ( t ) = ω 0 t + φ ( t ) = 2 π f 0 t + φ ( t ) = 2 π [ f 0 t + φ ( t )/2 π ], the formula for frequency becomes, as shown in Equation (10):

<!-- formula-not-decoded -->

where Δ f ( t ) is the deviation of frequency from nominal, and, as shown in Equation (11):

## IEEE Standard for Synchrophasor Measurements for Power Systems

<!-- formula-not-decoded -->

Frequency  in  phasor  measurements  may  be  reported  as  the  actual  frequency f ( t )  or  the  deviation  of frequency from nominal, Δ f ( t ). In steady-state conditions, Δ f ( t ) can be represented as a scalar number Δ f .

## 5.3 Measurement evaluation

## 5.3.1 Synchrophasor measurement evaluation

The theoretical values of a synchrophasor representation of a sinusoid and the values obtained from a PMU may  include  differences  in  both  amplitude  and  phase.  While  they  could  be  separately  specified,  the amplitude and phase differences are considered together in this standard in the quantity called total vector error (TVE).  TVE  is  an  expression  of  the  difference  between  a  'perfect'  sample  of  a  theoretical synchrophasor  and  the  estimate  given  by  the  unit  under  test  at  the  same  instant  of  time.  The  value  is normalized and expressed as per unit of the theoretical phasor.

TVE is defined in Equation (12):

<!-- formula-not-decoded -->

Where and are the sequences of estimates given by the unit under test, and X r ( n ) and X i ( n ) are the sequences of theoretical values of the input signal at the instants of time ( n ) assigned by the unit to those values. The values X r ( n ) and X i ( n ) can be determined in closed form in certain well-defined situations, such as constant frequency or phase offsets, and these situations are explored in this standard. ) ( ˆ n X r ) ( ˆ n X i

Synchrophasor measurements shall be evaluated using the TVE criterion of Equation (12).

## 5.3.2 Frequency and ROCOF measurement evaluation

Frequency  and  ROCOF  measurements  shall  be  evaluated  using  the  following  definitions.  With  these criteria,  frequency,  and  ROCOF  errors  are  the  absolute  value  of  the  difference  between  the  theoretical values and the estimated values given in Hz and Hz/s respectively. See Equation (13) and Equation (14).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The measured and true values are for the same instant of time, which will be given by the time tag of the estimated values.

## 5.3.3 Measurement response time and delay time

Measurement response time is the time to transition between two steady-state measurements before and after a step change is applied to the input. It shall be determined as the difference between the time that the measurement leaves a specified accuracy limit and the time it reenters and stays within that limit when a step change is applied to the PMU input. This shall be measured by applying a positive or negative step change in phase or magnitude to the PMU input signal. The input signal shall be held at a steady-state condition  before  and  after  the  step  change.  The  only  input  signal  change  during  this  test  shall  be  the

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

parameter(s)  that  have  been  stepped.  Accuracy  limits  are  the  TVE,  FE,  and  RFE  values  for  the  phasor, frequency,  and  ROCOF  measurements,  respectively.  The  limits  are  specified  in  5.5.8.  Note  that  the response time is determined from the accuracy evaluation of the measurements, not step time or the stepped parameters themselves.

Measurement delay time is defined as the time interval between the instant that a step change is applied to the  input  of  a  PMU  and  measurement  time  that  the  stepped  parameter  achieves  a  value  that  is  halfway between the initial and final steady-state values. Both the step time and measurement time are measured on the UTC time scale. This measurement shall be determined by applying a positive or negative step change in phase or magnitude to the PMU input signal. The input signal shall be held at a steady-state condition before and after the step change. The only input signal change during this test shall be the parameter(s) that have  been  stepped.  Note  this  measurement  requires  comparing  a  step  in  magnitude  with  the  magnitude measurement and a step in phase angle with the phase angle measurement.

The  purpose  of  evaluating  the  measurement  delay  time  is  to  verify  that  the  time  tagging  of  the synchrophasor measurement (measurement time) has been properly compensated for the filtering system group delay. It is expected that the time tag as provided by the PMU has been properly compensated for the filtering system group delay, so that the delay will be near zero.

A step  change  is  instantaneous  by  definition;  however,  if  the  slewing  rate  of  an  applied  signal  is  slow enough to introduce significant uncertainty in the time of application, the time of the midpoint of the step shall be used as the step time.

## 5.3.4 Measurement reporting latency

Latency in measurement reporting is the time delay from when an event occurs on the power system to the time that it is reported in data. This latency includes many factors, such as the window over which data is gathered to make a measurement, the estimation method, measurement filtering, the PMU processing time, and where the event occurs within the reporting interval. The reporting rate and performance class are often the  largest  factors,  since  these  will  determine  the  measurement  window,  filtering,  and  the  length  of  the interval over which an event will be reported.

For purposes of this standard, PMU reporting latency is defined as the maximum time interval between the data report time as indicated by the data time stamp, and the time when the data becomes available at the PMU output (denoted by the first transition of the first bit  of  the output  message  at the  communication interface point).

## 5.3.5 Measurement and operational errors

The PMU shall assign a flag to each measurement to indicate internal problems encountered during the measurement process. This flag shall include errors detectable by the PMU including A/D errors, memory overflow, calculation overflow and any other condition that could cause an error in the measurement. When IEEE C37.118.2 reporting  is  used,  this  flag  shall  be  reported  as  bit  14,  PMU  error,  in  the  status  word. (Under this requirement all measurement and operational error conditions shall be combined into a single error indication bit.)

## 5.4 Measurement reporting

Synchrophasor, frequency, and ROCOF estimates shall be made so they can be reported at a constant rate, Fs,  which  is  an  integer  number  of  times  per  second  when  the  rate  is  greater  than  one  per  second,  or  an integer number of seconds between measurements when the measurement rate is equal to or slower than one  per  second.  All  three  measurements  shall  be  made  and  reported  for  the  same  reporting  time.  The

## IEEE Standard for Synchrophasor Measurements for Power Systems

reporting times shall be evenly spaced so the intervals between reports are all the same. The PMU may make  other  measurements  synchronously  with  these  specified  measurements,  such  as  Boolean  status, waveform sampling, or other calculated data.

## 5.4.1 Reporting rates

The PMU shall support data reporting (by recording or output) at sub-multiples of the nominal power-line (system) frequency. Required rates for 50 Hz and 60 Hz systems are listed in the Table 1:

Table 1  -Required PMU reporting rates

| System frequency                          |   50 Hz |   50 Hz |   50 Hz |   60 Hz |   60 Hz |   60 Hz |   60 Hz |   60 Hz |   60 Hz |
|-------------------------------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Reporting rates (F s - frames per second) |      10 |      25 |      50 |      10 |      12 |      15 |      20 |      30 |      60 |

The actual  rate  to  be  used  shall  be  user  selectable.  Support  for  other  reporting  rates  is  permissible,  and including higher rates like 100/s or 120/s or rates lower than 10/s such as 1/s is encouraged. Note that rates lower than 10/s are not subject to the dynamic requirements of this standard (see 5.5.2). This means no filtering is required, so lower rate data (&lt; 10/s) can be provided directly by selecting every nth sample from a higher rate stream.

## 5.4.2 Reporting times

For a reporting rate N frames per second (fps) where N is a positive integer, the reporting times shall be evenly spaced through each second with frame number 0 (numbered 0 thru N-1) coincident with the UTC second rollover (e.g., coincident with a 1 PPS provided by GPS). These reporting times (time tags) are to be used for determining the instantaneous values of the synchrophasor as defined in 4.2. This is illustrated in Figure 2 where the reporting times are at 0, T 0 , 2 T 0 , 3 T 0 , 4 T 0 , etc. If rates lower than 1/s are used, there shall be one report on the hour (xx:00:00) and evenly spaced thereafter with an integer number of seconds between reports according to the chosen rate in the absence of leap seconds. If a leap second occurs, the last interval in the hour shall be shorter or longer by that leap second.

## 5.4.3 Example results

Table  2  gives  the  synchrophasor  values  as  defined  in  Equation  (1)  for  the  waveforms  shown  in Figure 2. The values are derived for a 10 fps reporting rate with a system frequency of 50 Hz and 60 Hz. Synchrophasor values are shown for base phase angles of 0 degrees and -90 degrees at the 1 PPS time mark as shown in Figure 1 for both 50 Hz and 60 Hz, and then 51 Hz and 61 Hz signals. The values in this example depend only on the magnitude, the reporting rate, and the signal frequency relative to the system frequency, so they are identical for 50 Hz and 60 Hz systems.

## IEEE Standard for Synchrophasor Measurements for Power Systems

Table 2  -Table of synchrophasor values at a 10 fps reporting rate

| Time   | Fractional time   | Fractional time   | Synchrophasor values for: 50 Hz frequency - 50 Hz system 60 Hz frequency - 60 Hz system   | Synchrophasor values for: 50 Hz frequency - 50 Hz system 60 Hz frequency - 60 Hz system   | Synchrophasor values for: 51 Hz frequency - 50 Hz system 61 Hz frequency - 60 Hz system   | Synchrophasor values for: 51 Hz frequency - 50 Hz system 61 Hz frequency - 60 Hz system   |
|--------|-------------------|-------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Second | Frame num- ber    | Fractional second | Synchrophasor (0 degrees)                                                                 | Synchrophasor (-90 degrees)                                                               | Synchrophasor (0 degrees)                                                                 | Synchrophasor (-90 degrees)                                                               |
| k-1    | 9                 | 0.900000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ -36º                                                                         | X m / √ 2, ∠-126 º                                                                        |
| k      | 0                 | 0.000000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         |
| k      | 1                 | 0.100000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 36º                                                                          | X m / √ 2, ∠-54 º                                                                         |
| k      | 2                 | 0.200000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 72º                                                                          | X m / √ 2, ∠-18 º                                                                         |
| k      | 3                 | 0.300000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 108º                                                                         | X m / √ 2, ∠18 º                                                                          |
| k      | 4                 | 0.400000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 144º                                                                         | X m / √ 2, ∠54 º                                                                          |
| k      | 5                 | 0.500000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 180º                                                                         | X m / √ 2, ∠90 º                                                                          |
| k      | 6                 | 0.600000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠-144 º                                                                        | X m / √ 2, ∠126 º                                                                         |
| k      | 7                 | 0.700000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ -108º                                                                        | X m / √ 2, ∠162 º                                                                         |
| k      | 8                 | 0.800000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ -72º                                                                         | X m / √ 2, ∠-162 º                                                                        |
| k      | 9                 | 0.900000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ -36º                                                                         | X m / √ 2, ∠-126 º                                                                        |
| k+1    | 0                 | 0.000000          | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         | X m / √ 2, ∠ 0º                                                                           | X m / √ 2, ∠ -90º                                                                         |

## 5.5 Measurement compliance

## 5.5.1 Introduction

To  be  compliant  with  this  standard,  a  PMU  shall  provide  synchrophasor,  frequency,  and  ROCOF measurements that meet the requirements in this subclause. These requirements shall be met at all times and under all configurations whether the PMU function is a stand-alone physical unit or included as part of a multifunction unit. This subclause details the requirements and conditions under which  those requirements shall be met. The first subclauses describe the test equipment needs and conditions for test. The  following  subclauses  describe  the  test  conditions  and  requirements  for  steady-state  and  dynamic measurement conditions.

## 5.5.2 Performance classes

Compliance with the requirements shall be evaluated by class of performance. This standard defines two classes of performance: P class and M class.

P class is intended for applications requiring fast response and mandates no explicit filtering. The letter P is used since protection applications require fast response.

M class is intended for applications that could be adversely effected by aliased signals and do not require the fastest reporting speed. The letter M is used since analytic measurements often require greater precision but do not require minimal reporting delay.

However  these  two  class  designations  do  not  indicate  that  either  class  is  adequate  or  required  for  a particular  application.  The  user  must  choose  a  performance  class  that  matches  the  requirements  of  each application.

## IEEE Standard for Synchrophasor Measurements for Power Systems

All compliance requirements are specified by performance class. A PMU shall meet all the requirements as specified for a class, in order to be considered as compliant with this standard for that class. If the vendor provides both P and M class performance, these shall be user selectable.

## 5.5.3 Compliance verification

A calibration  device  used  to  verify  performance  in  accordance  with  this  subclause  shall  be  traceable  to national  standards,  and  have  a test  uncertainty  ratio of  at  least  four  (4)  compared  with  these  test requirements (for example, provide a TVE measurement within 0.25% where TVE is 1%). In cases where there  is  no  national  standard  available  for  establishing  traceability,  a  detailed  error  analysis  shall  be performed to demonstrate compliance with these requirements.

Documentation shall be provided by any vendor claiming compliance with this standard that shall include the following information:

- a) Performance class
- b) Measurements that meet this class of performance
- c) Test results demonstrating performance
- d) Equipment settings that were used in testing
- e) Environmental conditions during the testing
- f) Error analysis if the verification system is based on an error analysis as previously called for

Compliance verification is by PMU and class of performance. A PMU verified for a particular performance class shall meet all performance requirements specified for that class at all required reporting rates.

## 5.5.4  Reference and test conditions

All compliance tests are to be performed with all parameters set to standard reference conditions, except those being varied as specified for the test. The reference condition specified for each test is the value of the quantity being tested when not being varied. Only the parameters specified for each requirement shall be varied as the effects shall be considered independent. Reference conditions for all tests are as follows:

- a) Voltage at nominal
- b) Current at nominal
- c) Frequency at nominal
- d) Voltage, current, phase, and frequency constant
- e) Signal total harmonic distortion (THD) &lt; 0.2% of the fundamental
- f) All interfering signals &lt; 0.2% of the fundamental

Measurements  at  reporting  rates  (Fs)  lower  than  10/s  shall  not  be  subject  to  dynamic  performance requirements. Such measurements shall be subject to all steady-state requirements (Table 3) except out-ofband rejection. This paragraph applies to all performance classes.

Unless otherwise specified, all testing to certify compliance shall be performed at standard laboratory test conditions that include the following:

- a) Temperature 23 ºC ± 3 ºC
- b) Humidity &lt; 90%

## IEEE Standard for Synchrophasor Measurements for Power Systems

Unless otherwise specified, the TVE, FE, and RFE for each performance requirement shall be the average, rms, or maximum value observed over a minimum of 5 s of test duration. Each test specifies whether the average, rms, or maximum value shall be used, and whether the period of observation shall be longer or shorter than 5 s. Note that some tests do not allow continued measurements at a specific value and specific methods are described with the test.

In the following subclauses, f in is the frequency of the fundamental signal component. It is normally 50 Hz or 60 Hz, but in the course of testing may be varied from nominal. Also, f 0 always represents the nominal frequency,  exactly  50  Hz  or  60  Hz.  Similarly, ω 0 =  2 π f 0 always  represents  the  nominal  frequency  in radians/s.

## 5.5.5 Steady-state compliance

Steady-state  compliance  shall  be  confirmed  by  comparing  the  synchrophasor,  frequency,  and  ROCOF estimates obtained under steady-state conditions to the corresponding theoretical values of X r , X i , F ,  and ROCOF. Steady-state conditions are where X m, ω , and φ of the test signal, and all other influence quantities are fixed for the period of the measurement. (Note that for off-nominal frequencies, the measured phase angle will change even though the test signal phase φ is constant.) The same tests are used for phasor and frequency/ROCOF measurements but the tables of requirements are separated for clarity.

Table 3  -Steady-state synchrophasor measurement requirements

|                                                                                                                                                                                       |                                                                                                                                                                                       | Minimum range of influence quantity over which PMU shall be within given TVE limit                                                                                                    | Minimum range of influence quantity over which PMU shall be within given TVE limit                                                                                                    | Minimum range of influence quantity over which PMU shall be within given TVE limit                                                                                                    | Minimum range of influence quantity over which PMU shall be within given TVE limit                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Influence quantity                                                                                                                                                                    | Reference condition                                                                                                                                                                   | P class                                                                                                                                                                               | P class                                                                                                                                                                               | Mclass                                                                                                                                                                                | Mclass                                                                                                                                                                                |
|                                                                                                                                                                                       |                                                                                                                                                                                       | Range                                                                                                                                                                                 | Max TVE (%)                                                                                                                                                                           | Range                                                                                                                                                                                 | Max TVE (%)                                                                                                                                                                           |
| Signal frequency range - f dev (test applied nominal + deviation: f 0 ± f dev )                                                                                                       | F nominal ( f 0 )                                                                                                                                                                     | ± 2.0 Hz                                                                                                                                                                              | 1                                                                                                                                                                                     | ± 2.0 Hz for F s <10 ± F s /5 for 10 ≤ F s < 25 ± 5.0 Hz for F s ≥ 25                                                                                                                 | 1                                                                                                                                                                                     |
| The signal frequency range tests above are to be performed over the given ranges and meet the given requirements at three temperatures: T = nominal (~23 ºC), T = 0 ºC, and T = 50 ºC | The signal frequency range tests above are to be performed over the given ranges and meet the given requirements at three temperatures: T = nominal (~23 ºC), T = 0 ºC, and T = 50 ºC | The signal frequency range tests above are to be performed over the given ranges and meet the given requirements at three temperatures: T = nominal (~23 ºC), T = 0 ºC, and T = 50 ºC | The signal frequency range tests above are to be performed over the given ranges and meet the given requirements at three temperatures: T = nominal (~23 ºC), T = 0 ºC, and T = 50 ºC | The signal frequency range tests above are to be performed over the given ranges and meet the given requirements at three temperatures: T = nominal (~23 ºC), T = 0 ºC, and T = 50 ºC | The signal frequency range tests above are to be performed over the given ranges and meet the given requirements at three temperatures: T = nominal (~23 ºC), T = 0 ºC, and T = 50 ºC |
| Signal magnitude - Voltage                                                                                                                                                            | 100% rated                                                                                                                                                                            | 80% to 120% rated                                                                                                                                                                     | 1                                                                                                                                                                                     | 10% to 120% rated                                                                                                                                                                     | 1                                                                                                                                                                                     |
| Signal magnitude - Current                                                                                                                                                            | 100% rated                                                                                                                                                                            | 10% to 200% rated                                                                                                                                                                     | 1                                                                                                                                                                                     | 10% to 200% rated                                                                                                                                                                     | 1                                                                                                                                                                                     |
| Phase angle with | f in - f 0 | <0.25 Hz (See NOTE 1)                                                                                                                                 | Constant or slowly varying angle                                                                                                                                                      | ± π radians                                                                                                                                                                           | 1                                                                                                                                                                                     | ± π radians                                                                                                                                                                           | 1                                                                                                                                                                                     |

## IEEE Standard for Synchrophasor Measurements for Power Systems

## Table 3 -Steady-state synchrophasor measurement requirements (continued)

|                                                                 |                                 | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   |
|-----------------------------------------------------------------|---------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Influence quantity                                              | Reference condition             | P class                                                                              | P class                                                                              | Mclass                                                                               | Mclass                                                                               |
|                                                                 |                                 | Range                                                                                | Max TVE (%)                                                                          | Range                                                                                | Max TVE (%)                                                                          |
| Harmonic distortion (single harmonic)                           | <0.2% (THD)                     | 1%, each harmonic up to 50th                                                         | 1                                                                                    | 10%, each harmonic up to 50th                                                        | 1                                                                                    |
| Out-of-band interference as described below (See NOTES 2 and 3) | <0.2% of input signal magnitude |                                                                                      | None                                                                                 | 10% of input signal magnitude for F s ≥ 10. No requirement for F s < 10.             | 1.3                                                                                  |

Out-of-band interference testing: The passband at each reporting rate is defined as | f -f 0 |  &lt; F s /2.  An interfering signal outside the filter passband is a signal at frequency f where: | f -f 0 | ≥ F s /2

For test the input test signal frequency f in is varied between f 0 and ± (10%) of the Nyquist frequency of the reporting rate.

That is: f 0 - 0.1 ( F s /2) ≤ f in ≤ f 0 + 0.1 ( F s /2)

where

F s = phasor reporting rate f 0 = nominal system frequency

f in = fundamental frequency of the input test signal

NOTE 1The phase angle test can be performed with the input frequency f in offset from f 0 where | f in -f 0 |&lt;0.25  Hz.  This  provides  a  slowly  varying  phase  angle  that  simplifies  compliance  verification  without causing significant other effects.

NOTE 2A signal whose frequency exceeds the Nyquist rate for the reporting rate F s can alias into the passband. The  test  signal  described  for  the  out-of-band  interference  test  verifies  the  effectiveness  of  the  PMU  anti-alias filtering.  The  test  signal  shall  include  those  frequencies  outside  of  the  bandwidth  specified  above  that  cause  the greatest TVE.

NOTE 3Compliance with out-of-band rejection can be confirmed by using a single frequency sinusoid added to the  fundamental power signal at the required magnitude level. The signal frequency is varied over a range from below the passband (at least down to 10 Hz) and from above the passband up to the second harmonic (2 × f 0 ). If the positive sequence measurement is being tested, the interfering signal is a positive sequence.

## IEEE Standard for Synchrophasor Measurements for Power Systems

## Table 4  -Steady-state frequency and ROCOF measurement requirements

| Influence quantity                                      | Reference                                          | Error requirements for compliance   | Error requirements for compliance   | Error requirements for compliance                                                 | Error requirements for compliance                                                 |
|---------------------------------------------------------|----------------------------------------------------|-------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
|                                                         | condition                                          | P class                             | P class                             | Mclass                                                                            | Mclass                                                                            |
| Signal frequency                                        | Frequency = f 0 ( f nominal ) Phase angle constant | Range: f 0 ± 2.0                    | Range: f 0 ± 2.0                    | Range: f 0 ± 2.0 Hz for F s ≤ 10 ± F s /5 for 10 ≤ F s < 25 ± 5.0 Hz for F s ≥ 25 | Range: f 0 ± 2.0 Hz for F s ≤ 10 ± F s /5 for 10 ≤ F s < 25 ± 5.0 Hz for F s ≥ 25 |
|                                                         |                                                    | Max FE                              | Max RFE                             | Max FE                                                                            | Max RFE                                                                           |
|                                                         |                                                    | 0.005 Hz                            | 0.01 Hz/s                           | 0.005 Hz                                                                          | 0.01 Hz/s                                                                         |
| Harmonic distortion (same as Table 3) (single harmonic) | <0.2% THD                                          | 1% each harmonic up to 50th         | 1% each harmonic up to 50th         | 10% each harmonic up to 50th                                                      | 10% each harmonic up to 50th                                                      |
| Harmonic distortion (same as Table 3) (single harmonic) |                                                    | Max FE                              | Max RFE                             | Max FE                                                                            | Max RFE                                                                           |
| Harmonic distortion (same as Table 3) (single harmonic) | F s > 20                                           | 0.005 Hz                            | 0.01 Hz/s                           | 0.025 Hz                                                                          | 6 Hz/s                                                                            |
| Harmonic distortion (same as Table 3) (single harmonic) | F s ≤ 20                                           | 0.005 Hz                            | 0.01 Hz/s                           | 0.005 Hz                                                                          | 2 Hz/s                                                                            |
| Out-of-band interference (same as Table 3)              | <0.2% of input signal                              | No requirements                     | No requirements                     | Interfering signal 10% of signal magnitude                                        | Interfering signal 10% of signal magnitude                                        |
| Out-of-band interference (same as Table 3)              | magnitude                                          |                                     |                                     | Max FE                                                                            | Max RFE                                                                           |
| Out-of-band interference (same as Table 3)              |                                                    | None                                | None                                | 0.01 Hz                                                                           | 0.1 Hz/s                                                                          |

Note that frequency and ROCOF are required to comply with the measurement limits only over the same range  of  frequencies  specified  for  phasors.  However  most  frequency  and  ROCOF  measurements  will operate  successfully  over  a  much  wider  range.  Vendors  are  encouraged  to  extend  their  measurement reporting over the widest practical range.

## 5.5.6 Dynamic compliance -measurement bandwidth

The  synchrophasor  measurement  bandwidth  shall  be  determined  by  sweeping  the  input  with  sinusoidal amplitude  and  phase  modulation.  This  shall  be  done  by  modulating  balanced  three-phase  input  signals (voltages and currents) with sinusoidal signals applied to signal amplitudes and phase angles simultaneously  in  accordance  with  Table  5  and  Table  6.  Mathematically  the  input  signals  may  be represented by Equation (15), Equation (16), and Equation (17):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where X m  is  the  amplitude  of  the  input  signal, ω 0  is  the  nominal  power  system  frequency, ω is  the modulation  frequency  in  radians/s, f m  = ω /2 π is  the  modulation  frequency  in  Hz,  k x is  the  amplitude modulation factor, and ka is the phase angle modulation factor.

The positive sequence signal corresponding to the above three-phase inputs is given by Equation (18):

<!-- formula-not-decoded -->

## IEEE Standard for Synchrophasor Measurements for Power Systems

At reporting time tags t = nT (where n is an integer and T is the phasor reporting interval) the PMU shall produce a positive sequence measurement of:

<!-- formula-not-decoded -->

within the error limits given in Table 5.

Frequency and ROCOF measurement performance shall also be determined during this test. For the input signals defined above and at reporting times t = nT , frequency, frequency deviation, and ROCOF are given respectively by Equation (20), Equation (21), and Equation (22):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The modulation tests shall be performed with ω , kx, and ka over the frequency ranges specified in Table 5. The modulation frequency shall be varied in steps of 0.2 Hz or smaller over the range specified in the table. The TVE, FE, and RFE shall be measured over at least two full cycles of modulation. The maximum is the highest value observed at the given reporting rate over the full test interval. This maximum shall be within the specified limits for P class and M class compliance at the given reporting rate. An adequate settling time  shall  be  allowed  for  each  test  signal  change  to  prevent  parameter  change  transient  effects  from distorting the measurement.

Table 5  -Synchrophasor measurement bandwidth requirements using modulated test signals

| Modulation level            | Reference                              | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   |
|-----------------------------|----------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|                             | condition                              | P class                                                                              | P class                                                                              | Mclass                                                                               | Mclass                                                                               |
|                             |                                        | Range                                                                                | Max TVE                                                                              | Range                                                                                | Max TVE                                                                              |
| k x = 0.1, k a = 0.1 radian | 100% rated signal magnitude, f nominal | Modulation frequency 0.1 to lesser of F s /10 or 2 Hz                                | 3%                                                                                   | Modulation frequency 0.1 to lesser of F s /5 or 5 Hz                                 | 3%                                                                                   |
| k x = 0, k a = 0.1 radian   | 100% rated signal magnitude, f nominal |                                                                                      | 3%                                                                                   |                                                                                      | 3%                                                                                   |

## IEEE Standard for Synchrophasor Measurements for Power Systems

## Table 6  -Frequency and ROCOF performance requirements under modulation tests

| Modulation level, reference condition, range (use the same modulation and ranges under the conditions specified in Table   | Error requirements for compliance   | Error requirements for compliance   | Error requirements for compliance   | Error requirements for compliance   |
|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|
|                                                                                                                            | P class                             | P class                             | Mclass                              | Mclass                              |
| levels reference 5)                                                                                                        | Max FE                              | Max RFE a                           | Max FE                              | Max RFE a                           |
| F s > 20                                                                                                                   | 0.06 Hz                             | 3 Hz/s                              | 0.3 Hz                              | 30 Hz/s                             |
| F s ≤ 20                                                                                                                   | 0.01 Hz                             | 0.2 Hz/s                            | 0.06 Hz                             | 2 Hz/s                              |

a Frequency and ROCOF follow the modulated signal just as the phasor estimate does, and measure the combined effects of the fundamental signal and the modulation. The errors in both measurements are a small fraction of the measured values, but since ROCOF (the second derivative of phase) becomes a large value, the expected error is also large. Note from the given formulas that the magnitude of frequency deviation increases linearly with frequency, but ROCOF increases by frequency squared.

## 5.5.7 Dynamic compliance -performance during ramp of system frequency

Measurement performance during system frequency change shall be tested with linear ramp of the system frequency applied as balanced three-phase input signals (voltages and currents). Mathematically the input signals may be represented by Equation (23), Equation (24), and Equation (25):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where X m is the amplitude of the input signal, ω 0 is the nominal power system frequency, and R f (= d f /d t ) is the frequency ramp rate in Hz/s (fixed value in this equation).

The positive sequence signal corresponding to the above three-phase inputs is given by Equation (26):

<!-- formula-not-decoded -->

At reporting time tags t = nT (where n is an integer and T is the phasor reporting interval) the PMU shall produce a positive sequence measurement as shown in Equation (27):

<!-- formula-not-decoded -->

During ramp tests, the true values of frequency, frequency deviation, and ROCOF for the specified test signals  at  reporting  time  tags t = nT are  given,  respectively,  by  Equation  (28),  Equation  (29),  and Equation (30):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

The  ramp  rate  and  frequency  range  as  well  as  the  measurement  error  limits  are  shown  in  Table  7  and Table 8. Note that the allowed TVE, FE, and RFE may be exceeded during a 'transition time' before and after a sudden change in ROCOF is made. The error calculation shall exclude measurements during the first two sample periods before and after a change in the test ROCOF. Sample periods are the reporting interval, 1/ F s , of the given test. For example, if the reporting rate F s = 30 fps, then measurements reported during a period  of  67  ms  before  and  after  a  transition  shall  be  discarded.  The  test  shall  not  include  frequency discontinuities (frequency steps).

Table 7  -Synchrophasor performance requirements under frequency ramp tests

|                       |                                                                                | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   | Minimum range of influence quantity over which PMU shall be within given TVE limit   |
|-----------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Test signal           | Reference condition                                                            | Ramp rate (R f ) (positive and negative ramp)                                        | Performance class                                                                    | Ramp range                                                                           | Max TVE                                                                              |
| Linear frequency ramp | 100% rated signal magnitude, &f nominal at start or some point during the test | ± 1.0 Hz/s                                                                           | P class                                                                              | ± 2 Hz                                                                               | 1%                                                                                   |
| Linear frequency ramp | 100% rated signal magnitude, &f nominal at start or some point during the test | ± 1.0 Hz/s                                                                           | Mclass                                                                               | Lesser of ± ( F s /5) or ± 5 Hz a                                                    | 1%                                                                                   |

a For F s = 12 fps, ramp range shall be ±2 1/3 (two and one-third) Hz to allow for an integer number of samples in the result.

Table 8  -Frequency and ROCOF performance requirements under frequency ramp tests

| Signal specification                      | Reference condition                                 | Transition time                        | Error requirements for compliance   | Error requirements for compliance   | Error requirements for compliance   | Error requirements for compliance   |
|-------------------------------------------|-----------------------------------------------------|----------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|
| Ramp tests - same as specified in Table 7 | 100% rated signal magnitude and 0 radian base angle | ± 2/ F s for the start and end of ramp | P class                             | P class                             | Mclass                              | Mclass                              |
| Ramp tests - same as specified in Table 7 | 100% rated signal magnitude and 0 radian base angle | ± 2/ F s for the start and end of ramp | Max FE                              | Max RFE                             | Max FE                              | Max RFE                             |
| Ramp tests - same as specified in Table 7 | 100% rated signal magnitude and 0 radian base angle | ± 2/ F s for the start and end of ramp | 0.01 Hz                             | 0.1 Hz/s                            | 0.005 Hz                            | 0.1 Hz/s                            |

## 5.5.8 Dynamic compliance -performance under step changes in phase and magnitude

Performance during step changes in magnitude and phase shall be determined by applying balanced threephase step changes to balanced three-phase input signals (voltages and currents). This test is mathematically represented in Equation (31), Equation (32), and Equation (33):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where X m is the amplitude of the input signal, ω 0 is the nominal power system frequency, f 1 ( t ) is a unit step function, kx is the magnitude step size and ka phase step size. This test is a transition between two steady states used to determine response time, delay time, and overshoot in the measurement. Step functions with parameters as specified in Table 9 shall be applied and the measurements shall meet the requirements in Table 9 and Table 10. 0 illustrates the measurements.

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

Response time and delay time are defined in 5.3.3. The steady-state error limits from Table 3 and Table 4 shall be used for determining the response time. These limits are 1% TVE, 0.005 Hz FE, and 0.01 Hz/s RFE. The delay time is determined by the time when the stepped parameter achieves a value that is halfway between  the  starting  and  ending  steady-state  values.  The  times  when  error  limits  are  crossed  and  the measurement crosses the 50% line shall be determined to an accuracy of one-tenth of the reporting rate that is being tested ( F s/10). Achievement of this accuracy shall be confirmed by test analysis.

NOTE-The PMU response times and delay times are small compared to the PMU reporting intervals. The specified response times (in Table 9 and Table 10) are less than three or five reporting intervals, and delay times are less than a quarter of a reporting interval. It is unlikely that reported data points will fall on the specified measurement points, so determining those points with a single step test may be insufficient. A series of tests with the step applied at varying times relative to the reporting times can be used to achieve this result.

This equivalent time sampling approach can achieve the required measurement resolution. In effect, this technique  moves  the  step  time  to  derive  points  on  the  measurement  to  'fill  in'  a  curve.  The  PMU measurement reports are at fixed points in time relative to the UTC second, so moving the steps a fraction of the reporting interval gives reports at different points on the measurement curve. These measurements are  combined to give a step response result with a time resolution less than the reporting interval. This technique controls the relation between the step time t in the unit step function f 1 ( t ) and one of the reporting times. The unit step function time is adjusted to fall on a reporting time for one step test. Successive step tests are performed with the unit step function times falling at increasing fractions of a reporting interval after a reporting time. Thus, if t r is a general reporting time, T is the reporting interval, and n is the number of tests to be performed, one test is performed with a f 1 ( t r). The next test is performed with a f 1 ( t r + T / n ), and the next with a f 1 ( t r + 2 T / n ), and so on until the n th test is performed with a f 1 ( t r + ( n - 1) T / n ). The resulting measurement  points  are  interleaved  by  aligning  all  of  the  steps  at  the  same  point  and  combining  the measurements with their corresponding offsets from the step. This gives an equivalent measurement step response with a time resolution of T / n . In general, an accurate measurement of the PMU response time, the delay time, and the overshoot percentage can be made with n = 10.

## IEEE Standard for Synchrophasor Measurements for Power Systems

<!-- image -->

Reported values are represented by the dots on a vertical line. The continuous response line will be determined by the equivalent time sampling described above. This figure illustrates response time, delay time, and overshoot measurements. Response time is determined from the error measurement (here TVE, but FE and RFE are done similarly). Delay and overshoot are determined by the curve of the parameter being stepped. Note that maximum overshoot may be over or under the final value, and the delay time may be positive or negative.

Figure 4  -Example of step change measurements using a magnitude step at t = 0

## IEEE Standard for Synchrophasor Measurements for Power Systems

Table 9  -Phasor performance requirements for input step change

| Step                                    |                                                     | Maximum response time, delay time, and overshoot   | Maximum response time, delay time, and overshoot   | Maximum response time, delay time, and overshoot   | Maximum response time, delay time, and overshoot   | Maximum response time, delay time, and overshoot   | Maximum response time, delay time, and overshoot   |
|-----------------------------------------|-----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| change                                  | Reference                                           | P class                                            | P class                                            | P class                                            | Mclass                                             | Mclass                                             | Mclass                                             |
| specifica- tion                         | condition                                           | Response time (s)                                  | |Delay time| (s)                                   | Max overshoot/ undershoot                          | Response time (s)                                  | |Delay time| (s)                                   | Max Overshoot/ undershoot                          |
| Magnitude = ± 10%, k x = ± 0.1, k a = 0 | All test conditions nominal at start or end of step | 1.7/ f 0                                           | 1/(4 × F s )                                       | 5% of step magnitude                               | See Table 11                                       | 1/(4 × F s)                                        | 10% of step magnitude                              |
| Angle ± 10°, k x = 0, k a = ± π /18     | All test conditions nominal at start or end of step | 1.7/ f 0                                           | 1/(4 × F s )                                       | 5% of step magnitude                               | See Table 11                                       | 1/(4 × F s)                                        | 10% of step magnitude                              |

Table 10 -Frequency and ROCOF performance requirements for input step change

|                              |                    | Maximum response time       | Maximum response time   | Maximum response time       | Maximum response time   |
|------------------------------|--------------------|-----------------------------|-------------------------|-----------------------------|-------------------------|
| Signal                       | Reference          | P class                     | P class                 | Mclass                      | Mclass                  |
| specification                | condition          | Frequency response time (s) | ROCOF response time (s) | Frequency response time (s) | ROCOF response time (s) |
| Magnitude test as in Table 9 | Same as in Table 9 | 3.5/ f 0                    | 4/ f 0                  | See Table 11                | See Table 11            |
| Phase test as in Table 9     | Same as in Table 9 | 3.5/ f 0                    | 4/ f 0                  | See Table 11                | See Table 11            |

Table 11 -Response time for M class phasor, frequency, and ROCOF for input step change

| Maximum response time in step change test for Mclass, in seconds   |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds |   Maximum response time in step change test for Mclass, in seconds | Maximum response time in step change test for Mclass, in seconds   | Maximum response time in step change test for Mclass, in seconds   |
|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Reporting rate ( F s )                                             |                                                             10     |                                                             12     |                                                             15     |                                                             20     |                                                             25     |                                                             30     |                                                             50     |                                                             60     | 100 a                                                              | 120 a                                                              |
| Phasor (TVE)                                                       |                                                              0.595 |                                                              0.493 |                                                              0.394 |                                                              0.282 |                                                              0.231 |                                                              0.182 |                                                              0.199 |                                                              0.079 | 0.050                                                              | 0.035                                                              |
| Frequency (FE)                                                     |                                                              0.869 |                                                              0.737 |                                                              0.629 |                                                              0.478 |                                                              0.328 |                                                              0.305 |                                                              0.13  |                                                              0.12  | 0.059                                                              | 0.053                                                              |
| ROCOF (RFE)                                                        |                                                              1.038 |                                                              0.863 |                                                              0.691 |                                                              0.52  |                                                              0.369 |                                                              0.314 |                                                              0.134 |                                                              0.129 | 0.061                                                              | 0.056                                                              |

a Rates higher than 60 are not required, so this listing is advisory only. Rates even higher will be limited by the measurement window. Rates lower than 10/s are not expected to be used for dynamic measurement and are not included in this table.

## 5.5.9 Measurement reporting latency compliance

The latency in measurement reporting is a critical factor for measurements used in real-time applications, particularly controls. In addition to measurement latency there are many factors contributing to reporting delay, such as communication coding and transmission distance. The application using the data shall take into  account all delays  to  determine  system  performance.  As  defined  in  5.3.4,  measurement  latency includes not only the various computation delays, but the effect of where an event occurs relative to the

## IEEE Standard for Synchrophasor Measurements for Power Systems

reporting time so that it will always be greater than one reporting period (1/ F s). These factors are included in this performance requirement.

PMU real-time output reporting latency shall be determined for each reporting rate F s using at least 1000 consecutive  messages.  The  reporting  latency  is  the  maximum  of  these  values.  The  latency  shall  be determined to an accuracy of at least 0.0001 s. See Table 12.

Table 12 -Measurement reporting latency

| Performance class   | Maximum measurement reporting latency (s)   |
|---------------------|---------------------------------------------|
| P class             | 2/ F s                                      |
| Mclass              | 5/ F s                                      |

## Annex A

(informative)

## Bibliography

Bibliographical references are resources that provide additional or helpful material but do not need to be understood or used to implement this standard. Reference to these resources is made for informational use only.

- [B1] Brigham, E. O., The Fast Fourier Transform. New York, Prentice Hall, 1974.
- [B2] IEEE Standards Dictionary: Glossary of Terms &amp; Definitions. 6
- [B3] IEEE Std 115™-2009, IEEE Guide for Test Procedures for Synchronous Machines, Part I -Acceptance and Performance Testing; Part II -Test Procedures and Parameter Determination for Dynamic Analysis. 7, 8
- [B4] IEEE Std 1012™-1998, IEEE Standard for Software Verification and Validation.
- [B5] IEEE Std 1344™-1995, IEEE Standard for Synchrophasors for Power Systems.
- [B6] IEEE  Std  1588™-2008,  IEEE  Standard  for  a  Precision  Clock  Synchronization  Protocol  for Networked Measurement and Control Systems.
- [B7] IEEE  Std  C37.111™-1999,  IEEE  Standard  Common  Format  for  Transient  Data  Exchange (COMTRADE) for Power Systems.
- [B8] IEEE Std C37.118™-2005, IEEE Standard for Synchrophasors for Power Systems.
- [B9] IEEE Std C37.118.2™-2011, IEEE Standard for Synchrophasor Data Transfer for Power Systems.
- [B10] IEEE Std C37.238™-2011, IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications.
- [B11] IEEE Std C57.13™-2008, IEEE Standard Requirements for Instrument Transformers.
- [B12] Synchrophasor Measurement Standard, WAMS &amp; Time Synchronization Working Group of SAC 82, China (PRC), 2010.
- [B13] Wicker, S. B., Error Control Systems for Digital Communications and Storage. Upper Saddle River, NJ: Prentice Hall, 1995.

6 The IEEE Standards Dictionary: Glossary of Terms &amp; Definitions is available at http://shop.ieee.org/.

7 IEEE publications are available from the Institute of Electrical and Electronics Engineers, 445 Hoes Lane, Piscataway, NJ 08854, USA (http://standards.ieee.org).

8 The  IEEE  standards  or  products  referred  to  in  Annex  A  are  trademarks  owned  by  the  Institute  of  Electrical  and  Electronics Engineers, Incorporated.

## IEEE Standard for Synchrophasor Measurements for Power Systems

## Annex B

(informative)

## Time tagging and dynamic response

## B.1 Dynamic response

As defined in 1.2, the primary purpose of this standard is to ensure PMU  interoperability. IEEE  Std C37.118-2005 [B8] introduced measurement compliance specifications for steady-state operation. This standard expands that context to dynamic response to transient conditions so all operational measurements shall be comparable. This annex discusses aspects of time tags and measurement errors.

Identical  PMUs  (defined  as  having  identical  hardware  and  algorithms)  should  yield  the  same  phasor measurement under all conditions. However, two PMUs with different algorithms and/or different analog circuitry can be expected to yield somewhat different results for the same phasor measurement in transient state  (the  time  during  which  a  change  in  magnitude,  phase  angle,  or  frequency  takes  place).  Test requirements and measurement evaluation in Clause 5 detail requirements to assure that measurements in both steady-state and transient conditions are comparable.

## B.2 Time tags

Phasor measurements are the estimated phasor representation of a sinusoidal signal. The estimation is made for the signal at a particular instant of time, and that time is represented by the phasor time tag. The process of making a phasor estimate will require sampling the waveform over some interval of time that can lead to some confusion as to which time within that window is the correct time tag for the phasor.

In the original synchrophasor standard, IEEE Std 1344-1995 [B5], this was defined as the last sample in the window. While this yields a measurement that appears causal, it also yields ambiguity in response due to the length of the window. Further investigation also showed that this provides an undesirable phase angle measurement error with change in frequency.

Consequently in the succeeding standard, IEEE Std C37.118-2005 [B8], the time tag was defined as the time of the theoretical phasor that the estimated phasor represents. This acknowledges  that the synchrophasor is  actually  an  estimate  of  the  sinusoid  parameters  over  the  window  of  observation  rather than a response to the input. The estimate covers a short period of time, so will represent some kind of 'average' of the parameters that may be changing during that window. In most cases the phasor estimate will be best represented by a time at the center of the estimation window. It is up to the designer to create a conversion process that assures that the magnitude and phase angle are properly represented, according to the TVE evaluation defined in 5.3.

If  the power system frequency is different from its nominal value, the phasor will rotate as illustrated in Table 2 in 5.4.3. Although this represents a steady-state condition (as defined in 5.5.5), it is easy to show that the instantaneous value of the phasor phase angle will be determined by the choice of the time tag and the inherent group delay associated with the actual measurement algorithm. This behavior is illustrated in Figure B.2, where a step in frequency from f 0 to f 0 +  5  Hz  is  applied  at t =  0.  The  curves  illustrate  the estimate produced by three different algorithms without group delay compensation.

## IEEE Standard for Synchrophasor Measurements for Power Systems

## IEEE Standard for Synchrophasor Measurements for Power Systems

Figure B.1-Frequency step test phase response without group delay compensation -+5 Hz frequency step at t = 0

<!-- image -->

By relying on the TVE concept defined in 5.3, this standard eliminates the off-nominal frequency phase angle ambiguity and ensures the compatibility between different PMUs. All compensation for group delay or other deficiencies of the estimation shall be compensated by the manufacturer. Figure B.2 shows multiple device output (from Figure B.1) after group delay compensation. In this figure, devices closely track each other, with four traces virtually indistinguishable from each other.

Figure B.2-Frequency step test phase response after group delay compensation (Ideal +3 algorithms, corresponding to Figure B.1)

<!-- image -->

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

Figure B.3 shows the results of these same three algorithms with group delay compensation under a 10% negative step in magnitude. This shows there will be differences in responses even though the group delay is compensated. The differences are small and will be imperceptible under most data reporting rates since sample rates are much slower than what is illustrated here. The responses are centered at the step ( t = 0), they  meet  the  response  time  requirement  for  P  class  at  180  fps  (and  all  lower  reporting  rates),  and  all overshoot requirements.

Figure B.3-Magnitude step test results for three different algorithms (group delay compensated, corresponding to Figure B.2) -per unit (PU) voltage or current is normalized to the reference ( V / V ref or I / I ref )

<!-- image -->

Group delay of a Finite Impulse Response (FIR) filter based algorithm with symmetric or anti-symmetric coefficients  is  equal  to  one-half  of  the  window  length  (time  tag  in  the  center  of  the  window).  Infinite Impulse Response (IIR) filters, asymmetric FIR filters, and optimization-based algorithms may stretch the trailing  edge,  making  the  time  response  asymmetrical.  Furthermore,  as  indicated  in  Figure  B.3,  the transient behavior  will  vary  depending  on  the  type  of  algorithm  used  for  phasor  estimation.  Instead  of mandating  a  single  measurement  algorithm,  this  standard  defines  the  performance  under  a  variety  of conditions and the use of TVE as the primary tool for phasor measurement device performance assurance.

## B.3 Magnitude step test example

Results of a simulated magnitude step test obtained with the P class algorithm presented in Annex C are illustrated in Figure B.4. TVE limits defined in 5.3 are indicated by thin horizontal lines. It is clear that under  steady-state  conditions,  simulated  PMU  response  stays  within  the  prescribed  TVE  requirement. However, during the step the TVE significantly exceeds the steady-state requirement. For this reason, the performance requirements in 5.5.8 do not specify a maximum TVE during a specified time period before and after the step time for both the P class and M class devices.

Figure B.4-Magnitude step test example (10% step, P class algorithm)

<!-- image -->

## Annex C

(informative)

## Reference signal processing models

## C.1 Introduction

This  annex  presents  the  reference  signal  processing  models  used  to  develop  and  verify  performance requirements in this standard. It is given for information purposes only, and does not imply being the only (or recommended) method for estimating synchrophasors. Its purpose is to establish common ground for understanding performance requirements and confirming their achievability.

Subclause C.2 includes a reference model for the general synchrophasor derivation. This model is the same for both algorithms presented in this subclause.

Subclause  C.3  has  the  specific  model  and  formulas  for  P  class  verification.  This  is  a  simple  derivation based on a fixed frequency two-cycle estimator designed to remove the second (and higher) harmonics in order to meet frequency deviation requirements. The P class filter length is constant for all output rates, meaning that PMU output generated at lower rates (&lt;50 msg/s or 60 msg/s) may contain additional aliasing components.

Subclause C.4 has the specific model and related equations for the M class verification. This model uses a low-pass filter for 20 dB of out-of-band rejection in all signals.

## C.2 Basic synchrophasor estimation model

Figure C.1 shows typical processing steps performed within the PMU. It assumes fixed frequency sampling synchronized  to  an  absolute  time  reference,  followed  by  complex  multiplication  with  the  nominal frequency carrier. Other implementations using frequency tracked sampling, frequency tracked carrier, or nonlinear  estimation  methods  are  also  possible  and  are  permitted  by  the  standard.  Depending  on  the algorithm and windowing, the output from this conversion may be at the original sample rate or lower.

Figure C.1-Single phase section of the PMU phasor signal processing model

<!-- image -->

Given a set of samples of a single phase of the power signal { x i}, the synchrophasor estimate X ( i ) at the i th sample time is:

## IEEE Standard for Synchrophasor Measurements for Power Systems

## IEEE Standard for Synchrophasor Measurements for Power Systems

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where

ω 0 = 2 π f 0 where f 0 is the nominal power system frequency (50 Hz or 60 Hz)

N = FIR filter order (number of filter taps is equal to N + 1)

Δ t = 1/sampling frequency x i = sample of the waveform at time t = i Δ t , where the time t = 0 coincides with a 1 s rollover

W(k) = low-pass filter coefficients (depending on P or M class filtering)

Equation (C.1) represents the complex demodulation and low-pass filtering shown in Figure C.1. Note that 0 ) ( exp( ω t k i Δ + -j ) is Euler's equation and includes multiplication of the input by the quadrature oscillator (sine and cosine) shown in Figure C.1. The low-pass filtering ( W(k) ) can be applied individually to the real and imaginary outputs of the complex demodulator as shown in Figure C.1.

## C.3 Time-stamp compensation for low-pass filter group delay

The time-stamp of the PMU output represents the phasor equivalent, frequency, and ROCOF of the power system signal at the time it is applied to the PMU input. All of these estimates must be compensated for PMU  processing  delays  including  analog  input  filtering,  sampling,  and  estimation  group  delay.  If  the sample  time  tags  are  compensated  for  all  input  delays,  the  time  tag  of  the  sample  in  the  middle  of  the estimation  window  can  be  used  for  the  phasor  estimation  (output)  time  tag  as  long  as  the  filtering coefficients are symmetrical across the filtering window. This method of group delay compensation is used with both the P class and the M class algorithms presented in this annex.

The filter  coefficients  for  P  class  and  M  class  low-pass  filters  are  derived  in  C.5  and  C.6,  respectively. Filter order for FIR filters is determined by the number of elements in the filter; the order is one less than the number of elements (taps) of the filter. For example, a 1 cycle Fourier filter using 15 samples/cycle is an N = 15 - 1 = 14th order filter. Examples provided in this annex use even order filters (odd number of taps). Resulting filter group delay is an integer multiple of the sampling frequency: Gd = N /2 × Δ t .

## IEEE Standard for Synchrophasor Measurements for Power Systems

## C.4 Positive sequence, frequency, and ROCOF

Figure C.2-Complete PMU signal processing model -all processing shown is at the A/D sampling rate; reporting rate is produced by resampling at the system output (decimator stage)

<!-- image -->

The normal positive sequence is calculated using the symmetrical component transformation. Frequency is then calculated from the rate of change of phase angle. Since phase angle changes relative to the difference between the actual frequency and the nominal frequency, this approach yields the offset from nominal. This algorithm  uses  differences  among  the  four  most  recent  angles  weighted  strongly  to  the  last  two  angle differences. It is set up this way to smooth out the estimate, particularly for the case of limited resolution as would be found in a real PMU. For this modeling, there was little difference in the performance of this algorithm and a frequency estimate derived from the angle difference between the two most recent angles. The frequency estimation algorithm is shown in Equation (C.3):

<!-- formula-not-decoded -->

where θ ( i )  is  the  angle  of  the  ith  positive  sequence  estimate X ( i ), θ ( i -  1)  is  the  angle  of  the  previous estimate, etc. The ROCOF estimate is then computed as the rate of change of the frequency estimate shown in Equation (C.4):

<!-- formula-not-decoded -->

Due to using angles behind (older than) the current phasor estimate, the frequency estimate lags the phasor. The frequency estimate could be exactly aligned with the phasor by waiting for the next phasor estimate and  then  computing  frequency  using  one  angle  ahead  and  one  angle  behind  the  current  phasor.  This requires delaying the output of the phasor value while waiting for the next phasor. The delay is only one sample period ( Δ t), which is small; however the differences caused by the delay using the given method are small also. The point here is that values computed using the given formula easily pass the requirements, and many other methods such as second order fit or weighted least squares will also, but all methods will require trade-offs, which are discussed in C.6. Note that simple finite difference equations like these are also very sensitive to noise.

## IEEE Standard for Synchrophasor Measurements for Power Systems

## C.5 P class reference model for phasor and frequency derivation

The P class phasor estimation algorithm presented here uses fixed length two-cycle triangular weighted FIR filter that is not changed for different PMU reporting rates. In order to simplify time stamp generation and phase compensation, the algorithm uses an odd number of samples (filter taps). This allows conversions and filtering to use a sample time stamp at the center of the window without adjustment. This reference algorithm implementation uses a sample rate of 15 samples/cycle,  which  becomes  60  × 15 = 900 samples/s for a 60 Hz system or 50 × 15 = 750 samples/s for a 50 Hz system. This algorithm can be implemented using a two-cycle FIR filter with triangular window coefficients shown in Figure C.3 [with filter order N being equal to N = 2 × (15 - 1) = 28] or in two stages with a one-cycle Fourier conversion followed by uniform averaging over one cycle (cascaded boxcar filter approach). As long as the sample times are compensated for input delays, the time stamp at the center of the window produces an estimate whose  phase  follows  the  actual  power  system  frequency  and  does  not  need  further  phase  or  delay correction. It does require magnitude correction for off-nominal frequency that is applied to the final phasor based on the frequency estimate. The complete process is diagrammed in Figure C.2.

## C.5.1 P class filter details

The P class filter coefficients W(k) are defined as shown in Equation (C.5):

<!-- formula-not-decoded -->

where k = -N /2 : N /2 (integer values only)

N = filter order [ N = (15 - 1) × 2 = 28 for sampling frequency example with 15 samples per cycle]

Example filter coefficients are shown in Figure C.3.

Figure C.3-P class filter coefficient example [ N = 2 x (15 - 1) = 28]

<!-- image -->

The P class filter works well at the nominal frequency for all but out-of-band rejection. For off-nominal frequency, the period of estimation does not match the actual period of the signal. Phase estimation works well because the signal is centered on the estimate. However, the estimate magnitude rolls off and needs compensation.  The  harmonic  rejection  is  excellent  when  the  conversion  matches  the  system  frequency.

## IEEE Standard for Synchrophasor Measurements for Power Systems

When it does not, such as under off-nominal frequency, harmonics are not suppressed very well, which causes some problems with frequency and ROCOF estimation.

When PMU implementation is made with a fixed conversion frequency f 0, the phasor magnitude will roll off as the signal frequency deviates from f 0 . The result is a (sin ( x )/ x ) 2 curve determined by the two-cycle low-pass filter response shown in Figure C.4.

Figure C.4-P class filter response as a function of frequency [example shows: f 0 = 60 Hz, f sampling = 15 x 60 = 900 Hz, N = 2 x (15 - 1) = 28]

<!-- image -->

Over a limited frequency range, this deviation can be compensated by dividing the phasor magnitude by the P  class  filter  response  at  the  measured  frequency.  With  this  algorithm,  the  phase  angle  measurement  is accurately  computed  at  all  frequencies  using  the  estimate  centered  in  the  window.  The  magnitude  is compensated  by  dividing  the  magnitude  with  a  sine  at  the  actual  signals  frequency.  The  two-cycle triangular window produces a faster rolloff than a standard one-cycle rectangular window, so the frequency deviation  is  spread  with  an  additional  factor  of  1.625  to  increase  compensation  (the  factor  was  derived experimentally) as shown in Equation (C.6):

<!-- formula-not-decoded -->

where

Δ F ( i ) = deviation of frequency from nominal computed at point i as shown in Equation (C.3)

Equation (C.6), Equation (C.3), and Equation (C.4) are used for synchrophasor, frequency, and ROCOF estimation, respectively, in the P class model.

## C.6 M class reference model for phasor and frequency derivation

The principal difference between P class and M class is that the M class has a requirement for filtering to attenuate by at least 20 dB signals that are above the Nyquist frequency for the given reporting rate. This filtering will result in longer reporting delays but will also reduce the likelihood of aliasing. Because of the

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

required  filtering,  the  M  class  can  produce  somewhat  higher  accuracy,  a  fact  that  is  reflected  in  the requirements.

The M class requirements for passband and stopband filtering are shown in Figure C.5. The figure is based on the M class requirements given in Table 3 and Table 5 in Clause 5, with corner frequency specifications linked to the PMU reporting rate. This mask is used as the mask for designing the reference filter. An FIR filter  implementation  was  used  to  achieve  linear  phase  response.  The  reference  filter  coefficients  were obtained  by  using  well-known  'brick  wall'  filter  design  methodology  based  on  'sinc'  function

sin(

x

multiplied  with  a  Hamming  window.  The  filter  order  (length)  is  adjusted  to  meet  frequency  response requirements. This model assumes correct implementation of the front end scaling, anti-aliasing filter, A/D converter and adequate sampling rate that was set to 960 Hz in this example.

Figure C.5-Reference algorithm filter frequency response mask specification for M class (frequency response curve within unshaded region)

<!-- image -->

For Figure C.5, the filter response shall remain outside the shaded areas.

Equation (C.7) calculates a vector of filter coefficients:

<!-- formula-not-decoded -->

where

k =  - N /2 : N /2

N =  filter order from Table C.1

F fr

=  low-pass filter reference frequency from Table C.1

F sampling =   sampling frequency of the system (960 samples/second for the reference model)

h(k)

=  Hamming function

W (0)      =  1 (note when k = 0, W

= 0/0, which is 'not a number' and must be replaced by 1)

x

)

Figure C.6-M class filter coefficient example ( F s = 60 fps, F sampling = 960 Hz, N = 96)

<!-- image -->

Table  C.1 shows  input  parameters  to  generate  the  filter  coefficients  used  to  verify  limits  in  this specification.  It  is  given  for  information  purposes  only,  and  does  not  imply  being  the  only  (or recommended) filter:

Table C.1-M class low-pass filter parameters (example)

| Reporting rate F s   |   Reporting rate F s |   Filter reference frequency F fr (Hz) |   Filter order N |
|----------------------|----------------------|----------------------------------------|------------------|
| 50 Hz                |                   10 |                                  1.92  |              700 |
| 50 Hz                |                   25 |                                  4.8   |              280 |
| 50 Hz                |                   50 |                                  8.85  |              100 |
| 50 Hz                |                  100 |                                 16     |               44 |
| 60 Hz                |                   10 |                                  1.92  |              794 |
| 60 Hz                |                   12 |                                  2.304 |              660 |
| 60 Hz                |                   15 |                                  2.88  |              528 |
| 60 Hz                |                   20 |                                  3.84  |              396 |
| 60 Hz                |                   30 |                                  5.616 |              238 |
| 60 Hz                |                   60 |                                 10.32  |               96 |
| 60 Hz                |                  120 |                                 18.96  |               40 |

## C.7 Data rate reduction model

The reference model shown in Figure C.1 and Figure C.2 can be used to directly produce any of the output rates shown in Table C.1. If the PMU produces phasors, frequency, and ROCOF internally at a high rate and reduces the data stream for output, similar filters can be used to perform further decimation (derive lower  rates)  for  M  class  outputs  as  shown  in  Figure  C.7.  This  method  can  be  used  when  multiple  rate outputs are required from the same PMU and in the case of a phasor data concentrator (PDC) application. It is important to note that the out-of-band rejection requirements specified in this standard for M class apply equally to lower frequency (decimated) synchrophasor data streams produced by both PMUs and PDCs. Consequently,  decimated  output  data  (lower  rates)  generated  by  the  PDC  are  expected  to  remain comparable (have the same dynamic behavior) as those generated by the PMU. These same methods can be

## IEEE Standard for Synchrophasor Measurements for Power Systems

used for P class, but the additional filtering is not required. P class data reduction can be accomplished by a simple 1/ N resampling (i.e., taking every N th sample).

Figure C.7-Data rate reduction signal processing model

<!-- image -->

## C.8 Tradeoffs in the reference model

## C.8.1 Immunity to off-nominal components, reporting latency, and time alignment

Designers and users of PMUs need to consider three interrelated factors affecting the estimation of phasors, frequency, and ROCOF. The three factors, shown in Figure C.8, are as follows:

- ⎯ Immunity  to  noise  such  as  harmonics,  interharmonics  (out-of-band  interfering signals), or modulations on the input signal
- ⎯ Alignment of the frequency and ROCOF estimation to the time stamp of the phasor estimation
- ⎯ Reporting  latency  (the  time  for  the  estimations  to  be  completed  and  ready  to  transmit  from  the PMU

Figure C.8-Factors affecting estimation

<!-- image -->

## IEEE Standard for Synchrophasor Measurements for Power Systems

The PMU reference model was designed to have relatively short reporting latency and good time alignment between the phasor, frequency, and ROCOF estimates. Good alignment and short latency comes at the cost of some immunity, as illustrated in Figure C.8. This model is meant to verify PMU performance limits, be relatively  simple  to  understand  and  implement,  and  leave  margin  for  actual  PMUs.  It  is  not  intended  to illustrate the ideal solution.

## C.8.2 Response time and the accuracy of synchrophasors, frequency, and ROCOF measurements

The  accuracy  of  the  synchrophasors,  frequency,  and  ROCOF  measurements,  when  non-fundamental components  are  present  in  the  signals,  is  directly  affected  by  the  reference  filter  gain  and  frequency response.  In  particular,  the  frequency  components  beyond  the  Nyquist  frequency  (half  the  value  of  the applied reporting rate) should be attenuated.

Figure C.9 exhibits the gain/frequency response of the reference filter with a reporting rate F s = 60 fps and a data acquisition sampling frequency of 960 Hz. The attenuation level beyond the Nyquist frequency of 30 Hz is greater than 20 db.

Figure C.9-Reference filter magnitude frequency response with F s = 60 fps

<!-- image -->

Let us assume as an example that the voltage signals are at fundamental frequency with some added second harmonic component. After the demodulation has taken place when applying the reference algorithm, the second harmonic component will translate into two frequency components at 60 Hz and 180 Hz that are above the Nyquist frequency. The impact of the second harmonic on the synchrophasors, frequency, and ROCOF measurements accuracy depends on the attenuation provided by the reference filter at these two specific components: the higher the attenuation, the better the measurement accuracy. The same rationale could be applied to any non-fundamental component.

The  model  reference  filter  has  been  designed  so  that  it  allows  a  fast  response  time  (65  ms  for  a  10% magnitude change at F s = 60 fps) together with a good accuracy for the synchrophasor measurement. Better accuracy  figures  could  be  obtained  for  the  frequency  and  ROCOF  measurements  by  increasing  the attenuation level beyond the Nyquist frequency, but that would be done at the expense of the synchrophasor measurement response time, which would become slower.

## Annex D

(informative)

## Time and synchronization communication

## D.1 PMU time input

A  PMU  requires  a  source  of  UTC  time  synchronization.  This  may  be  supplied  directly  from  a  time broadcast such as GPS or from a local clock using a standard time code. IRIG-B is commonly used for local time dissemination. It may be provided in a level shift, a 1 kHz amplitude modulated signal, or in the bi-phase Manchester modulated format (modulation type 2, B2xx). If the amplitude modulation is used it may  need  to  be  supplemented  with  a  1  PPS  pulse  train  to  achieve  the  required  accuracy.  The  IRIG-B amplitude modulated format is commonly available and hence is the most readily implemented. The newer Manchester  format  is  more  compatible  with  fiber  optic  and  digital  systems  and  provides  complete synchronization  without  additional  signals.  Other  forms  of  precise  time  distribution,  such  as  standard Ethernet using IEEE Std 1588-2008 [B6], are emerging and will become increasingly available with new technology developments.

1 PPS. A common feature of timing systems is a pulse train of positive pulses at a rate of one pulse per second (1 PPS). The rising edge of the pulses coincides with the seconds change in the clock and provides a very precise time reference. The pulse widths vary from 5 μ s  to  0.5  s,  and  the  signal  is  usually  a  5.0  V magnitude driving a 50 ohm load. A 1 PPS timing signal must be used with another system such as a serial timing message or IRIG-B to supply the full time synchronization.

IEEE 1588. IEEE Std 1588-2008 [B6] allows timing accuracies better than 1 μ s for devices connected via a network such as Ethernet. IEEE Std C37.238-2011 [B10] specifies a subset of IEEE 1588 functionality to be  supported  for  power  system  protection,  control,  automation,  and  data  communication  applications utilizing an Ethernet communication architecture. At the time of this writing (2011) several commercially available  Ethernet  switches,  grandmaster  clocks,  and  slave  clocks  have  implemented  the  IEEE  C37.238 functionality  and demonstrated this performance. Both standards may be obtained through the IEEE-SA web site.

IRIG-B. IRIG-B is fully described in IRIG Standard 200-04 published by the Range Commanders Council of the U. S. Army White Sands Missile Range. Time is provided once per second in seconds through day of year in a binary coded decimal (BCD) format and an optional binary second-of-day count. The standard allows a number of configurations that are designated as Bxyz where x indicates the modulation technique, y indicates the counts included in the message, and z indicates the interval. The most commonly used form is  B122, which has seconds through day-of-year coded in BCD and is amplitude modulated on a 1 kHz carrier. The amplitude should be a peak-to-peak amplitude of 1 V to 6 V for the mark (peak) with a markto-space amplitude ratio 10:3 as provided in the standard. A block of 27 control bits is available for user assignment and can be used to supplement the standard code for continuous timekeeping. The time code format is:

## &lt;sync&gt; SS:MM:HH:DDD &lt;control&gt; &lt;binary seconds&gt;

where

&lt;sync&gt; = the on-time sync marker SS = the second of the minute [00 to 59 (60 during leap seconds)] MM = the minute of the hour (00 to 59) HH = the hour of day in 24 format (00 to 23) DDD = the day of year (001 to 366)

## IEEE Standard for Synchrophasor Measurements for Power Systems

&lt;control&gt; = a block of 27 binary control characters

- &lt;binary seconds&gt; = a 17 bit second of day in binary

## D.2 IRIG-B time code extensions

IRIG-B includes 27 control bits for user provided information in addition to the specified time codes. This subclause details assignments for these control bits that enable coding the year of century, non-sequential changes (leap seconds and daylight savings time), local time offsets, and time quality into the message. These  assignments  extend  IRIG-B  to  a  complete  time  message  as  needed  by  the  utility  industry.  These extensions were first introduced with the IEEE synchrophasor standard, IEEE Std 1344-1995 [B5]. They were included in the succeeding standard, IEEE Std C37.118-2005 [B8], with a change in the sign of the local  time  offset.  They  are  again  carried forward  to  this  standard  with  an  added  continuous  time  quality code.

Table D.1-Control bit assignments

| IRIG-B Pos ID   | CTRLBIT#   | Designation                       | Explanation                                                                                                                                           |
|-----------------|------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| P 50            | 1          | Year, BCD 1                       | Last 2 digits of year in BCD.                                                                                                                         |
| P 51            | 2          | Year, BCD 2                       | IBID                                                                                                                                                  |
| P 52            | 3          | Year, BCD 4                       | IBID                                                                                                                                                  |
| P 53            | 4          | Year, BCD 8                       | IBID                                                                                                                                                  |
| P 54            | 5          | Not Used                          | Unassigned                                                                                                                                            |
| P 55            | 6          | Year, BCD 10                      | Last 2 digits of year in BCD.                                                                                                                         |
| P 56            | 7          | Year, BCD 20                      | IBID                                                                                                                                                  |
| P 57            | 8          | Year, BCD 40                      | IBID                                                                                                                                                  |
| P 58            | 9          | Year, BCD 80                      | IBID                                                                                                                                                  |
| P 59            | -          | P6                                | Position identifier # 6                                                                                                                               |
| P 60            | 10         | Leap Second Pending (LSP)         | Becomes 1 s up to 59 s BEFORE leap second insert                                                                                                      |
| P 61            | 11         | Leap Second (LS)                  | 0 = Add leap second, 1 = Delete leap second                                                                                                           |
| P 62            | 12         | Daylight Saving Pending(DSP)      | Becomes 1 s up to 59 s BEFORE DST change                                                                                                              |
| P 63            | 13         | Daylight Savings Time (DST)       | Becomes 1 s during Daylight Savings Time (DST)                                                                                                        |
| P 64            | 14         | Time Offset sign                  | Time offset sign - 0 = +, 1 = - .                                                                                                                     |
| P 65            | 15         | Time Offset-binary 1              | Offset from coded IRIG-B time to UTC time. IRIG coded time minus time offset (including sign) equals UTC time at all times (offset will change during |
| P 66            | 16         | Time Offset-binary 2              | Offset from coded IRIG-B time to UTC time. IRIG coded time minus time offset (including sign) equals UTC time at all times (offset will change during |
| P 67            | 17         | Time Offset-binary 4              | Offset from coded IRIG-B time to UTC time. IRIG coded time minus time offset (including sign) equals UTC time at all times (offset will change during |
| P 68            | 18         | Time Offset-binary 8              | daylight savings).                                                                                                                                    |
| P 69            | -          | P7                                | Position identifier # 7                                                                                                                               |
| P 70            | 19         | Time Offset-0.5 h                 | 0 = none, 1 = additional 0.5 h time offset 4-bit code representing approx. clock time 0000 = clock locked to a traceable UTC                          |
| P 71            | 20         | Time Quality-binary 1             | error. source 1111 = clock failed, data unreliable                                                                                                    |
| P 72            | 21         | Time Quality-binary 2             | error. source 1111 = clock failed, data unreliable                                                                                                    |
| P 73            | 22         | Time Quality-binary 4             | error. source 1111 = clock failed, data unreliable                                                                                                    |
| P 74            | 23         | Time Quality-binary 8             | Use Table D.2.                                                                                                                                        |
| P 75            | 24         | PARITY                            | Parity on all preceding data bits.                                                                                                                    |
| P 76            | 25         | Continuous Time Quality- binary 1 | 3-bit code representing the estimated maximum time error in the transmitted message. This CTQ indicates error at all times. Use Table D.3.            |
| P 77            | 26         | Continuous Time Quality- binary 2 | 3-bit code representing the estimated maximum time error in the transmitted message. This CTQ indicates error at all times. Use Table D.3.            |
| P 78            | 27         | Continuous Time Quality- binary 4 | 3-bit code representing the estimated maximum time error in the transmitted message. This CTQ indicates error at all times. Use Table D.3.            |
| P79             | -          | P8                                | Position identifier # 8                                                                                                                               |

NOTE-The interpretation of the UTC offset encoded in control bits 14-19 changed between IEEE 1344-1995 [B5] and IEEE Std C37.118-2005 [B8]. In IEEE 1344-1995 the offset defined in those control bits was added to the IRIG time to get UTC time. In IEEE Std C37.118-2005 this was changed to subtracting the offset so the listed offset sign would be consistent with standard practice. In standard practice, time zones to the east of the Greenwich Meridian are positive and those to the west are negative. This standard retains the IEEE C37.118 method-the listed offset must be subtracted from IRIG to determine UTC time.

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

Virtually every timekeeping system is run by some kind of processor. Since IRIG time code numbers arrive after the on-time mark, the timekeeping system must generate the time tag based on the anticipated number rather  than  on  what  it  just  received.  Consequently,  time  counts  that  are  not  in  exact  sequence  require advance  notice.  Non-sequence  clock  counts  include  leap  year,  leap  second,  and  daylight  savings  time changes. The leap second and daylight savings change bits warn of impending special clock counts, and the last two digits of the year alert the timing system of leap year changes.

As an interpretation of the IRIG standard, BCD time and straight binary seconds (SBS) shall be consistent. If BCD time changes by an hour for a daylight time change, SBS shall change at the same time to reflect a consistent count. The year will roll over with BCD time regardless of whether it corresponds with UTC time.

Year : The last two digits of the year is in straight BCD in the same format as the rest of the IRIG-B code and follows first after day of year. It will roll over with the day of year in the BCD time count.

Leap second : The leap second pending (LSP) and polarity (LS) bits show that one is about to happen and whether it will be inserted or deleted. Leap seconds have only been positive for the last 20 years, so LS = 0 is almost certain. The LSP bit shall be asserted between 1 s and 60 s before the hour it is to be inserted. The bit shall go to 0 when the second count goes to 00. Leap seconds are always inserted at UTC midnight by altering the second time count only. Thus in UTC time, the time count goes from 23:59:59 to 23:59:60 to 00:00:00 to add the extra second. In another time zone, say Pacific Standard Time,  which  is 8 h behind UTC, the same count will be 15:59:59 to 15:59:60 to 16:00:00. SBS shall give the count 57 600 (=16:00:00) twice.

Daylight savings :  The  Daylight Savings Pending (DSP) and Daylight Savings Time (DST) bits indicate that a change is about to happen and whether daylight savings is in effect. If DST = 0, then the impending change will be to ON, which will delete 1 h from the time scale (leap forward 1 h in the spring) and the Daylight Savings bit will go to one. If DST = 1, the opposite will occur. Daylight time changes will be 1 h and are asserted at the minute rollover. The DSP bit shall be asserted between 1 s and 60 s before time is to be changed. The DSP and DST bits shall change at the same time between the 59 s and 00 s counts. In the United States where the time change is put into effect at 2:00 AM, the time count in the Spring is 01:59:59 to 03:00:00. In the Fall, the count is 01:59:59 to 01:00:00.

Local time offset : The local time offset is a 5-bit binary count with a sign bit. The last bit is a fractional half-hour, which is used by a few countries. The offset gives the hours difference (up to ± 15.5 h) between UTC time and the IRIG-B time (both BCD and SBS codes). Subtracting the offset from the IRIG-B time using  the  included  sign  gives  UTC  time  [e.g.,  if  the  IRIG-B  time  is  109:14:43:27  and  the  offset  is -06 given by the code 0110.0 (Central Standard Time in North America), then UTC time is 109:20:43:27.] The local time offset shall always give the true difference between IRIG code and UTC time, so the offset changes whenever a daylight savings time change is made. This follows the standard convention of positive time offsets east of the GMT meridian and negative offsets west of the meridian.

Time quality (TQ): A 4-bit TQ indicator code is used by several manufacturers and is in several existing standards. It is an indicator of time accuracy or synchronization relative to UTC and is based on the clock's internal parameters. The code recommended here is by order of magnitude relative to 1 ns. It is basically the same as used in the HaveQuick and STANAG 4430 (NATO) time codes but with a more practical scale. The 1 ns basic reference is fine enough to accommodate all present industry uses now and into the foreseeable future. When locked to a UTC traceable source (such as GPS), all 4 bits of the TQ code shall be cleared to 0. All 4 bits shall be set to 1 during a clock failure and at startup before achieving a stable  locked  condition.  Note  that  this  flag  cannot  provide  a  time  quality  indication  while  the  clock  is locked to a UTC traceable source since all bits will be set to 0.

Table D.2-Four-bit Time Quality indicator code

|   Binary | Hex   | Value (worst-case accuracy)               |
|----------|-------|-------------------------------------------|
|     1111 | F     | Fault - clock failure, time not reliable  |
|     1011 | B     | Time within 10 s of UTC                   |
|     1010 | A     | Time within 1 s of UTC                    |
|     1001 | 9     | Time within 10 -1 s of UTC                |
|     1000 | 8     | Time within 10 -2 s of UTC                |
|     0111 | 7     | Time within 10 -3 s of UTC                |
|     0110 | 6     | Time within 10 -4 s of UTC                |
|     0101 | 5     | Time within 10 -5 s of UTC                |
|     0100 | 4     | Time within 10 -6 s of UTC                |
|     0011 | 3     | Time within 10 -7 s of UTC                |
|     0010 | 2     | Time within 10 -8 s of UTC                |
|     0001 | 1     | Time within 10 -9 s of UTC                |
|     0000 | 0     | Clock is locked to a UTC traceable source |

Parity: This  parity  covers  all  the  preceding  bits  in  the  message  from  BCD  seconds  (P1)  through  time quality  in  the  control  bits  (P74).  SBS  and  P76-79  are  not  included.  The  value  is  equal  to  the  modulo-2 addition of all the preceding bits (P1 through P74) in the message. The total number of 1's in the message (P1 through P75) is thereby made an even number. This results in EVEN parity.

Continuous time quality (CTQ) :  This  CTQ  is  a  3-bit  Time  Quality  indicator  code  that  is  provided  in addition to the TQ given above. This additional code is active at all times, during both locked and unlocked conditions. It uses control bits 25, 26, and 27, which were unused in the previous version of this profile. These bits were previously set to 0 by default when this profile was implemented. These bits will never be all zero in this version of the profile, so an all zero code indicates implementation of the previous version of the profile. A time code receiver using CTQ can therefore identify if there is a valid CTQ present or not. Similarly, a time code receiver using the previous profile does not look at these bits, so the presence of a new code will not interfere with its operation. Since there are only seven codes available, they were chosen to best fit power system applications.

Table D.3-Three-bit Time Quality indicator code

|   Binary |   Hex | Value (worst-case accuracy)                                |
|----------|-------|------------------------------------------------------------|
|      111 |     7 | Estimated maximum time error > 10 ms or time error unknown |
|      110 |     6 | Estimated maximum time error < 10 ms                       |
|      101 |     5 | Estimated maximum time error < 1 ms                        |
|      100 |     4 | Estimated maximum time error < 100 μ s                     |
|      011 |     3 | Estimated maximum time error < 10 μ s                      |
|      010 |     2 | Estimated maximum time error < 1 μ s                       |
|      001 |     1 | Estimated maximum time error < 100 ns                      |
|      000 |     0 | Not used (indicates code from previous version of profile) |

## D.3 IRIG-B high-precision time code format

IRIG-B format transmitted using modified Manchester modulation is recommended as an alternative to the AM modulated IRIG-B with separate 1 PPS sync. This modulation is better adapted for both fiber  and metallic  digital  systems.  With  the  previous  control  bit  assignments,  this  time  code  format  can  serve  all power industry requirements now and in the foreseeable future.

## IEEE Std C37.118.1-2011

## IEEE Standard for Synchrophasor Measurements for Power Systems

Manchester  coding  provides  a  zero  mean  code  that  is  easy  to  decode,  even  at  low  signal  levels.  The 1  kHz  clock  provides  a  precise  on-time  mark  that  is  always  present.  The  coding  method  mimics  1  kHz modulated IRIG-B with binary 1's and 0's in place of high and low amplitude cycles. A Manchester binary 1 is equivalent to a high amplitude cycle in the AM modulation and a binary 0 indicates a low amplitude cycle. Using this modulation, an IRIG-B code '0' will be two ones followed by eight zeroes. An IRIG-B code  '1'  will  be  five  ones  followed  by  five  zeroes  (Figure  D.1).  This  conversion  keeps  the  codes compatible and makes translation or regeneration of the AM IRIG-B very simple.

Figure D.1-IRIG-B coding comparisons: level shift, 1 kHz AM, and modified Manchester

<!-- image -->

Modified Manchester coding. Manchester modulation or encoding is a return-to-zero type where the pulse transition indicates binary 0 or 1. In this case, a 1 kHz square wave is the basic clock modulated by the data to produce a rising edge to indicate a binary one (1) and a falling edge to indicate a binary zero (0). The transition at every data bit provides good receiver synchronization. Each bit period is half high and half low, so the mean is always one-half, making it easy to decode, even at low levels. In standard Manchester coding,  the  data  edge  occurs  in  the  middle  of  the  clock  window  to  indicate  a  binary  one  or  zero.  The 'modification' moves the data window so the data is at the edge of the clock window that is on time with UTC (Figure  D.2).  In  another  view,  the  modification  simply  defines  the  middle  of  the  window  as  'on time.'  What  is  important  is  that  the  data  edge  is  the  on  time  mark  in  the  code.  This  simplifies  the construction of readers and regeneration of the other IRIG code forms. Modified Manchester modulation is designated type 2 in the IRIG standard (B2xx).

<!-- image -->

## Annex E

(informative)

## TVE evaluation and PMU testing

## E.1 TVE measurement technique

The  total  vector  error  (TVE)  is  a  measure  of  the  difference  between  the  information  from  a  PMU  that describes  a  phasor  and  the  true  phasor  itself. 9 As  with  most  measurements,  the  relation  between  the measurand and the observation is determined by calibration. It is assumed that if the error observed during calibration is within some limits of acceptability, it will remain so until the next calibration is performed, and that the measurement can therefore be 'trusted.' (The behavior of systems in this regard can be used to determine an appropriate calibration interval.)

In the case of instrument transformers, applied to the metering and protective relaying of power systems, the acceptable errors are expressed (for example, in IEEE Std C57.13-2008 [B11]) separately in terms of the allowed phase angle error and the allowed magnitude error. These allowable errors are expressed, for example, in terms of ratio correction factor, the number by which the observation must be multiplied to obtain the true value.

To simplify compliance specification, magnitude and angle error bounds have been combined into a single error quantity called total vector error. This allowable error criterion combines all error sources, including time synchronization, phasor  angle, and  phasor  magnitude  estimation  errors. TVE  is  defined  by Equation  (7)  in  5.3.1.  Since  the  'true'  value  cannot  be  precisely  known,  we  rely  on  a  calibration  to establish the bounds within which the measurement (the vector) has a high probability of lying.

For calibration purposes, a signal that meets any required level of precision can be generated electronically. This standard establishes a criterion of 1% for the value of the TVE during calibration. That means that the value found by substitution into Equation (7) shall not exceed 1% if the PMU is to be deemed compliant.

The 1% criterion established by setting TVE = 0.01 in Equation (7) can be visualized as a small circle drawn on the end of the phasor. The maximum magnitude error is 1% when the error in phase is zero, and the  maximum  error  in  angle  is  just  under  0.573º.  Provided  the  observed  samples  do  not  lie  outside  the circle, the device is compliant. Figure E.1 shows the circle, with size greatly exaggerated for clarity.

Note that measurement of the properties of an ac signal requires some non-zero interval of observation. For an  assessment  of  steady-state  performance,  the  calibration  signal  properties  will  be  held  constant throughout the measurement interval. The observation can be compared with the input signal regardless of the measurement time.

9 According to the Guide to the Expression of Uncertainty in Measurements (GUM), the 'true' value of a quantity (the measurand ) is not something that can ever be known. GUM recognizes that the observer has incomplete knowledge of the measurand, and the best one can do is quantify the probability that the measurand is within a certain range of the observation. However, it will be convenient and not misleading here to use the term 'true' value, so we shall continue to use it.

## IEEE Standard for Synchrophasor Measurements for Power Systems

Figure E.1-The 1% TVE criterion shown on the end of a phasor

<!-- image -->

For  dynamic  measurement  requirements,  the  input  signal  will  not  be  a  perfect  sine  wave,  and  the observation (sampling) time is important. The standard requires comparison between the input signal taken at the same time as the PMU output report. If an input signal parameter (such as phase angle) is uniformly increasing  or  decreasing  across  the  measurement  interval  and  the  phasor  estimator  is  symmetric,  the estimate  and  the  actual  value  will  compare  most  closely  if  the  measurement  time  is  the  middle  of  the interval.

For example, if the phase angle increases linearly from 10º to 12º across the measurement window, it will be 11º at the center. If the measurement time is the center of the window, the true value at that time is assumed to be 11º. This is therefore the value to be used during calibration to determine the TVE.

If the parameters are not constant or changing across the time window, achieving a suitable estimate of the true value becomes more difficult. If an input parameter is changing across the interval, a constant model centered on the interval will not necessarily give the best estimate. The best estimates will be achieved with a signal model that assumes the type of changes present in the time window.

However, the situation is moderated by the limited range of power system frequency response. Changes to the power signal usually occur at rates less than 3 Hz/s; where they are at a higher frequency, they are quite small. With a 1 cycle estimation window, a slower change (under 3 Hz/s) appears as short segments that are nearly  linear  so  the  center  of  window  makes  a  good  approximation.  With  higher  frequencies,  the magnitudes of the changes are small, so even if the time representation is not ideal, the error is small and within the TVE limit.

## E.2 Phase-magnitude relation in TVE and timing

TVE  combines  magnitude and phase errors. While the phasor representation in Figure E.1 is straightforward to understand conceptually, it does not reveal the interaction of the two parameters in terms of their relative contribution to TVE. Figure E.2 shows the variation in TVE as a function of magnitude for various  phase  errors  and  Figure  E.3  shows  the  variation  in  TVE  as  a  function  of  phase  for  various magnitude  errors.  Each  parameter  has  the  same  parabolic  influence  on  the  other,  only  differing  in  the intercept values for TVE.

Figure E.2-TVE as a function of magnitude for various phase errors

<!-- image -->

1

Figure E.3-TVE as a function of phase for various magnitude errors

<!-- image -->

Phase angle is determined by the relation of the given signal to a time synchronized reference at nominal system frequency. If the reference is displaced by a certain time interval, the angle of the given signal will be displaced by that same time interval, creating an error in the estimated phase angle. Thus timing errors translate directly to phase errors. The TVE is computed relative to measurement magnitude and phase at the given  system  frequency.  Consequently  timing  errors  will  result  in  different  TVE  depending  on  system frequency. A cycle at system frequency is 20 ms at 50 Hz and 16.67 ms at 60 Hz. One degree of phase angle at 50 Hz is 55.6 μ s and at 60 Hz is 46.3 μ s. Therefore the timing error that will cause a 1% TVE error at 50 Hz is ±31.7 μ s and at 60 Hz is ±26 μ s.

## E.3 Testing

Testing  requires  confirming  the  measurement  from  a  PMU  matches  the  input  signal.  A  signal  with parameters matching a particular phasor specification is applied to the PMU input. The phasor, frequency, and ROCOF measurements (estimates) output from the PMU are then compared with the input using the TVE, FE, and RFE criteria. The comparison is done between the phasor, frequency, and ROCOF values of the input at the exact time that matches the measurement output time stamp. Since the output measurement time  is  synchronized  to  UTC  time,  the  signal  provided  at  the  input  must  also  be  UTC  synchronized  (to determine  the  values  for  comparison).  Signal  generators  are  available  that  provide  precise  phase  angle, magnitude, and frequency settings that are GPS synchronized. Complete test procedures are being produced by IEEE and other organizations. They are not part of this standard.

Refer to Evaluation of measurement data -Guide to the expression of uncertainty in measurement , JCGM 100:2008 (GUM 1995 with minor corrections). 10

10 Available from http://www.bipm.org/en/publications/guides/gum.html (accessed January 26, 2011).

## IEEE Standard for Synchrophasor Measurements for Power Systems

## Annex F

(informative)

## Generator voltage and power angle measurement 11

## F.1 Introduction

The synchronized and near real-time acquisition of signals relevant to the dynamic performance of power systems provides a basis for the dynamic monitoring, control, and protection of these systems over wide areas. Synchronized estimation of voltage and current phasors are an important set of signals required to track the dynamic performance of power systems. However, there are a number of other relevant signals, including the rotor-angle, power angle, and rotor-speed of synchronous machines.

Although the acquisition of these other signals is beyond the scope of this standard, this annex is provided to  indicate  a  way  phasor  measurement  can  be  used  with  other  measurement  techniques  for  future development of synchronized measurements for power systems.

## F.2 Measurement methods

- a) Electrical  calculation  method: The  internal  voltage  and  the  power  angle  of  a  generator  can  be derived from knowledge of the direct-axis reactance X d, the quadrature-axis reactance X q , and realtime PMU or Supervisory Control and Data Acquisition (SCADA) data measurements representing the terminal voltage and current. This method may lead to errors because the values of X d and X q might vary with the generator operating conditions.
- b) Rotor  position  measurement  method: The  angle  of  internal  voltage  and  the  power  angle  of  a generator can be calibrated against the rotor position and the terminal voltage angle. This method has good accuracy and is suitable for real-time power angle measurement when the power system is subject  to  a  disturbance.  The  rotor  position  measurement  method  may  be  therefore  considered advantageous for measurement of the generator power angle and frequency.

## F.3 Input signal

For measurements of internal voltage and power angles, the input signals to the PMU include the terminal voltages and currents of the generator, and a signal representing the rotor position, all with respect to the same time reference.

## F.4 Measuring process

The rotor position of a generator may be monitored by optical or magnetic means. In the optical method, some kind of shaft encoder can be used. In the magnetic method, a periodic pulse signal may be produced by  a  slot  added  for  the  purpose  at  some  arbitrary  location  on  the  rotor,  and  a  sensor  on  the  stator.  By comparing the rotor position signal with the reference time signal, the rotor position angle (called α ) of the generator can be calculated. When the generator runs with no load, the power angle of the generator is zero, and any offset between the rotor position signal and the internal voltage angle can be calibrated as follows.

11 The concept and basis for this annex has been kindly contributed by the WAMS &amp; Time Synchronization Working Group of SAC 82, Beijing, China. See Synchrophasor Measurement Standard [B12].

## IEEE Standard for Synchrophasor Measurements for Power Systems

Under no-load conditions, the voltage angle at the terminals of the generator is the same as the angle of the internal  voltage  angle  of  the  generator.  Measured  relative  to  the  reference  time  signal,  the  angle  of  the terminal voltage under no-load is indicated as angle β in Figure F.1. The rotor position, which depends on the position of shaft encoder or the slot on the rotor of the generator, is at some angle α . The angular offset ( γ )  between  the  angles α and β can  be  obtained. This  angle γ remains  constant  unless  something  in  the physical machine is changed; for example, the coil assembly is rebuilt during maintenance.

Thus  the  angle γ does  not  change  when  the  machine  is  under  load.  Therefore,  when  the  generator  is operating, the angle of the internal voltage can be calculated from knowledge of the rotor angle and the calibration  offset γ .  See  Figure  F.2.  The  voltage  angle β is  found  by  subtracting γ from α (which  is observable). The generator power angle δ is then given by the difference between the internal voltage angle β and the terminal voltage of the generator, as shown in Figure F.2.

Figure F.1-Phasor diagram under no-load conditions

<!-- image -->

Figure F.2-Phasor diagram with load on generator

<!-- image -->