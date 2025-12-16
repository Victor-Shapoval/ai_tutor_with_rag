## IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications

## IEEE Power and Energy Society

Sponsored by the Power System Relaying Committee and the

Substations Committee

<!-- image -->

IEEE Std C37.238™-2017 (Revision of IEEE Std C37.238-2011)

## IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications

Sponsor

## Power System Relaying Committee and Substations Committee of the

IEEE Power and Energy Society

Approved 23 March 2017

IEEE-SA Standards Board

Abstract: An  extended  profile  is  specified  for  the  use  of  Precision  Time  Protocol  of  IEEE  Std 1588-2008 in power system protection, control, automation, and data communication applications utilizing an Ethernet communications architecture.

Keywords: grandmaster  clock,  IEEE  1588™,  IEEE  C37.238™,  power  substation,  precise time  synchronization,  Precision  Time  Protocol,  PTP,  sample  synchronization,  slave-only  clock, synchrophasors, transparent clock

The Institute of Electrical and Electronics Engineers, Inc.

3 Park Avenue, New York, NY 10016-5997, USA

Copyright © 2017 by The Institute of Electrical and Electronics Engineers, Inc. All rights reserved. Published 19 June 2017. Printed in the United States of America.

IEEE is a registered trademark in the U.S. Patent &amp; Trademark Office, owned by The Institute of Electrical and Electronics Engineers, Incorporated.

PDF:

ISBN 978-1-5044-2326-7

STD21113

Print:

ISBN 978-1-5044-2327-4

STDPD21113

IEEE prohibits discrimination, harassment, and bullying.

For more information, visit http://  www  .ieee  .org/  web/  aboutus/  whatis/  policies/  p9  -26  .html.

No part of this publication may be reproduced in any form, in an electronic retrieval system or otherwise, without the prior written permission of the publisher.

## Important Notices and Disclaimers Concerning IEEE Standards Documents

IEEE documents are made available for use subject to important notices and legal disclaimers. These notices and disclaimers, or a reference to this page, appear in all standards and may be found under the heading 'Important Notices and Disclaimers Concerning IEEE Standards Documents.' They can also be obtained on request from IEEE or viewed at http://  standards  .ieee  .org/  IPR/  disclaimers  .html.

## Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents

IEEE Standards  documents  (standards,  recommended  practices,  and  guides),  both  full-use  and  trial-use, are developed within IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association ('IEEE-SA') Standards Board. IEEE ('the Institute') develops its standards through a consensus development  process,  approved  by  the  American  National  Standards  Institute  ('ANSI'),  which  brings together volunteers representing varied viewpoints and interests to achieve the final product. IEEE Standards are  documents  developed  through  scientific,  academic,  and  industry-based  technical  working  groups. Volunteers in IEEE working groups are not necessarily members of the Institute and participate without compensation from IEEE. While IEEE administers the process and establishes rules to promote fairness in the consensus development process, IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the soundness of any judgments contained in its standards.

IEEE Standards do not guarantee or ensure safety, security, health, or environmental protection, or ensure against  interference  with  or  from  other  devices  or  networks.  Implementers  and  users  of  IEEE  Standards documents are responsible for determining and complying with all appropriate safety, security, environmental, health, and interference protection practices and all applicable laws and regulations.

IEEE does not warrant or represent the accuracy or content of the material contained in its standards, and expressly disclaims all warranties (express, implied and statutory) not included in this or any other document relating to the standard, including, but not limited to, the warranties of: merchantability; fitness for a particular purpose; non-infringement; and quality, accuracy, effectiveness, currency, or completeness of material. In addition, IEEE disclaims any and all conditions relating to: results; and workmanlike effort. IEEE standards documents are supplied 'AS IS' and 'WITH ALL FAULTS.'

Use of an IEEE standard is wholly voluntary. The existence of an IEEE standard does not imply that there are no other ways to produce, test, measure, purchase, market, or provide other goods and services related to the scope of the IEEE standard. Furthermore, the viewpoint expressed at the time a standard is approved and issued is subject to change brought about through developments in the state of the art and comments received from users of the standard.

In publishing and making its standards available, IEEE is not suggesting or rendering professional or other services for, or on behalf of, any person or entity nor is IEEE undertaking to perform any duty owed by any other person or entity to another. Any person utilizing any IEEE Standards document, should rely upon his or her own independent judgment in the exercise of reasonable care in any given circumstances or, as appropriate, seek the advice of a competent professional in determining the appropriateness of a given IEEE standard.

IN NO EVENT SHALL IEEE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,  OR  CONSEQUENTIAL  DAMAGES  (INCLUDING,  BUT  NOT  LIMITED  TO: PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR  BUSINESS  INTERRUPTION)  HOWEVER  CAUSED AND  ON ANY  THEORY  OF  LIABILITY, WHETHER  IN  CONTRACT,  STRICT  LIABILITY,  OR  TORT  (INCLUDING  NEGLIGENCE  OR OTHERWISE)  ARISING  IN  ANY  WAY  OUT  OF  THE  PUBLICATION,  USE  OF,  OR  RELIANCE UPON ANY STANDARD, EVEN IF ADVISED OF THE POSSIBILITY OF  SUCH  DAMAGE AND REGARDLESS OF WHETHER SUCH DAMAGE WAS FORESEEABLE.

## Translations

The IEEE consensus development process involves the review of documents in English only. In the event that an IEEE standard is translated, only the English version published by IEEE should be considered the approved IEEE standard.

## Official statements

A statement, written or oral, that is not processed in accordance with the IEEE-SA Standards Board Operations Manual shall not be considered or inferred to be the official position of IEEE or any of its committees and shall not be considered to be, or be relied upon as, a formal position of IEEE. At lectures, symposia, seminars, or educational courses, an individual presenting information on IEEE standards shall make it clear that his or her views should be considered the personal views of that individual rather than the formal position of IEEE.

## Comments on standards

Comments for revision of IEEE Standards documents are welcome from any interested party, regardless of  membership affiliation with IEEE. However, IEEE does not provide consulting information or advice pertaining to IEEE Standards documents. Suggestions for changes in documents should be in the form of a proposed change of text, together with appropriate supporting comments. Since IEEE standards represent a consensus of concerned interests, it is important that any responses to comments and questions also receive the concurrence of a balance of interests. For this reason, IEEE and the members of its societies and Standards Coordinating Committees are not able to provide an instant response to comments or questions except in those cases where the matter has previously been addressed. For the same reason, IEEE does not respond to interpretation requests. Any person who would like to participate in revisions to an IEEE standard is welcome to join the relevant IEEE working group.

Comments on standards should be submitted to the following address:

Secretary, IEEE-SA Standards Board 445 Hoes Lane Piscataway, NJ 08854  USA

## Laws and regulations

Users of IEEE Standards documents should consult all applicable laws and regulations. Compliance with the provisions of any IEEE Standards document does not imply compliance to any applicable regulatory requirements.  Implementers  of  the  standard  are  responsible  for  observing  or  referring  to  the  applicable regulatory requirements. IEEE does not, by the publication of its standards, intend to urge action that is not in compliance with applicable laws, and these documents may not be construed as doing so.

## Copyrights

IEEE draft and approved standards are copyrighted by IEEE under U.S. and international copyright laws. They are made available by IEEE and are adopted for a wide variety of both public and private uses. These include both use, by reference, in laws and regulations, and use in private self-regulation, standardization, and the promotion of engineering practices and methods. By making these documents available for use and adoption by public authorities and private users, IEEE does not waive any rights in copyright to the documents.

## Photocopies

Subject to payment of the appropriate fee, IEEE will grant users a limited, non-exclusive license to photocopy portions of any individual standard for company or organizational internal use or individual, non-commercial use only. To arrange for payment of licensing fees, please contact Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978 750 8400. Permission to photocopy portions of any individual standard for educational classroom use can also be obtained through the Copyright Clearance Center.

## Updating of IEEE Standards documents

Users of IEEE Standards documents should be aware that these documents may be superseded at any time by the issuance of new editions or may be amended from time to time through the issuance of amendments, corrigenda, or errata. An official IEEE document at any point in time consists of the current edition of the document together with any amendments, corrigenda, or errata then in effect.

Every IEEE standard is subjected to review at least every ten years. When a document is more than ten years old and has not undergone a revision process, it is reasonable to conclude that its contents, although still of some value, do not wholly reflect the present state of the art. Users are cautioned to check to determine that they have the latest edition of any IEEE standard.

In order to determine whether a given document is the current edition and whether it has been amended through the issuance of amendments, corrigenda, or errata, visit the IEEE Xplore at http://  ieeexplore  .ieee  .org/ or contact IEEE at the address listed previously. For more information about the IEEE-SA or IEEE's standards development process, visit the IEEE-SA Website at http://  standards  .ieee  .org.

## Errata

Errata, if any, for all IEEE standards can be accessed on the IEEE-SA Website at the following URL: http:// standards  .ieee  .org/  findstds/  errata/  index  .html. Users are encouraged to check this URL for errata periodically.

## Patents

Attention is called to the possibility that implementation of this standard may require use of subject matter covered by patent rights. By publication of this standard, no position is taken by the IEEE with respect to the existence or validity of any patent rights in connection therewith. If a patent holder or patent applicant has filed a statement of assurance via an Accepted Letter of Assurance, then the statement is listed on the IEEESA Website at http://  standards  .ieee  .org/  about/  sasb/  patcom/  patents  .html. Letters of Assurance may indicate whether the Submitter is willing or unwilling to grant licenses under patent rights without compensation or under reasonable rates, with reasonable terms and conditions that are demonstrably free of any unfair discrimination to applicants desiring to obtain such licenses.

Essential Patent Claims may exist for which a Letter of Assurance has not been received. The IEEE is not responsible for identifying Essential Patent Claims for which a license may be required, for conducting inquiries into the legal validity or scope of Patents Claims, or determining whether any licensing terms or conditions provided in connection with submission of a Letter of Assurance, if any, or in any licensing agreements are reasonable  or  non-discriminatory.  Users  of  this  standard  are  expressly  advised  that  determination  of  the validity of any patent rights, and the risk of infringement of such rights, is entirely their own responsibility. Further information may be obtained from the IEEE Standards Association.

## Participants

At the time this standard was submitted to the IEEE-SA Standards Board for approval, the IEEE 1588 Profile for Power System Applications Working Group had the following membership:

## Galina S. Antonova, Chair William Dickerson, Vice Chair

Didier Giarratano Herb Falk Richard Harada Christopher R. Huntley David M. E. Ingram Hubert Kirrmann Bruce Muschlitz

Mark Adamiak Alex Apostolov Christoph Brunner James Bougie Michael Dood Roman Graf

R. Jay Murphy Markus Renz Greg Rzepka Veselin Skendzic Timothy Tibbals Sergiu Zimath

The following members of the individual balloting committee voted on this standard. Balloters may have voted for approval, disapproval, or abstention.

William Ackerman Mark Adamiak Ali Al Awazi M. Victoria Alonso Galina S. Antonova Douglas Arnold Roberto Asano Philip Beaumont Robert Beresh William Bloethe Klaus Brand Gustavo Brunello William Byrd Paul Cardinal Randall Crellin Ratan Das William Dickerson Michael Dood Neal Dowling Denis Dufournet Dan Dwyer Lee Eccles John Egan Christian Frei Fredric Friend Frank Gerleve Jalal Gohari

Roman Graf Randall Groves Ajit Gwal James Hackett Roger Hedding Werner Hoelzl Yi Hu Richard Hunt C. Huntley David M.E. Ingram Innocent Kamwa Piotr Karocki Yuri Khersonsky Hubert Kirrmann Jim Kulchisky Marc Lacroix Chung-Yiu Lam John Mackay Pierre Martin William McBride David Mcginn R. Murphy Bruce Muschlitz Michael Newman Lorraine Padden Charles Petras

Donald Platts Farnoosh Rahmatian Michael Roberts Silvana Rodrigues M. Sachdev Bartien Sayogo Thomas Schossig Maik Seewald Veselin Skendzic Brian Smellie John Spare Walter Struppler Stefan Svensson David Tepen Eric Thibodeau Timothy Tibbals Joe Uchiyama Eric Udren Benton Vandiver John Vergis Stephen Webb Karl Weber Roger Whittaker Philip Winston Oren Yuen Daidi Zhong Sergio Zimath

When  the  IEEE-SA  Standards  Board  approved  this  standard  on  23  March  2017,  it  had  the  following membership:

## Jean-Philippe Faure, Chair Gary Hoffman, Vice Chair John D. Kulick, Past Chair Konstantinos Karachalios, Secretary

Chuck Adams Masayuki Ariyoshi Ted Burse Stephen Dukes Doug Edwards J. Travis Griffith Michael Janezic Thomas Koshy Joseph L. Koepfinger* Kevin Lu Daleep Mohla Damir Novosel Ronald C. Petersen Annette D. Reilly Yu Yuan

*Member Emeritus

Robby Robson Dorothy Stanley Adrian Stephens Mehmet Ulema Phil Wennblom Howard Wolfman

## Introduction

This introduction is not part of IEEE Std C37.238-2017, IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications.

This standard specifies a profile that extends the capabilities of IEC/IEEE 61850-9-3 profile for the use of the IEEE 1588 Precision Time Protocol (PTP) in power system protection, control, automation, and data communication applications utilizing an Ethernet communications architecture.

This revision was generated to respond in a timely manner to comments brought forward by IEC Technical Committee 57 Working Group 10 and others after publication of IEEE Std C37.238-2011, as a result of first implementations.

To provide base-level interoperability, IEEE Std C37.238-2011 was divided into a base profile specified in IEC/IEEE 61850-9-3:2016 and the profile that extends the capabilities of the IEC/IEEE 61850-9-3 profile, which is specified in this standard. As a result, this standard is compliant with the IEC/IEEE 61850-9-3:2016 standard.

The following main changes are incorporated into this revision:

- -PTP parameters and performance specifications that are part of the base profile were replaced with references to IEC/IEEE 61850-9-3:2016. Refer to 5.2 to 5.11 and Annex B of IEEE Std C37.238-2011.
- -Definitions were revisited; some definitions were removed and replaced with references. Refer to 3.1.
- -New Clause 5 was added to explain the relationship between different standards, namely IEEE Std 1588-2008, IEC/IEEE 61850-9-3:2016, and this standard.
- -The Best Master Clock Algorithm (BMCA) requirement to check for the presence of profile-specific type, length, and value (TLV) was removed, to keep the BMCA as specified in 9.3 of IEEE Std 15882008. Refer to 5.12 of IEEE Std C37.238-2011 and new subclause 6.2 of this standard.
- The  field  definition  in  the  IEEE\_C37\_238\_TLV  was  modified  while  keeping  backwards compatibility with the previous version's data fields. Refer to 5.12.2 of IEEE Std C37.238-2011 and new subclause 6.2.1 of this standard.
- organizationSubType has been changed from 1 to 2.
- GrandmasterTimeInaccuracy is replaced with Total time inaccuracy.
- -grandmasterID field field's range restriction has been removed (all 16 bits are now usable), for the following reasons:
- -IEC 61850 applications will now be using the 64-bit grandmaster clock identity, so they do not require a short grandmasterID.
- -For applications that use Inter-Range Instrumentation Group B (IRIG-B), keeping this field, with an expansion to 16 bits, provides compatibility with IEEE Std C37.2382011, a user-settable ID that does not change when the clock's hardware is replaced (see C.4, C.4.2, and D.3.3 ), and the use of grandmasterID field is now optional (zero if unused).
- -The fields of the IEEE 1588 Alternate Time Offset Indicator TLV are clarified for providing the local time. TLV support is mandatory and use is optional. Refer to 6.2.2.
- -Description  of  TimeInaccuracy  concept  is  expanded  and  terms  are  redefined  for  clarity.  Refer to 5.13 of IEEE Std C37.238-2011, new subclause 6.3 of this standard, and Clause 3 of IEC/IEEE 61850-9-3:2016.

- -Guidance on compatibility with the previous version of this standard is provided in new Annex B.
- -Additional guidance is provided on mapping between IEEE Std C37.238 and IRIG-B formats (see Annex C).
- -Appropriate changes are made to Annex C and Annex D to include a new profile-specific TLV format.
- -Guidance on the use of multiple PTP profiles in a single timing network, particularly, using IEC/IEEE 61850-9-3 slave devices in an IEEE C37.238 network, can be found in Annex E.

Necessary  definitions  are  provided.  Typical  Ethernet-based  time  distribution  architecture  consists  of  a reference clock, bridges, and end devices. Bridges with boundary clock functionality may also be used at interconnection points between different PTP domains or PTP profiles.

In addition to distributing global time that is traceable to a recognized standard time source, for the cases when connectivity to recognized standard time sources is lost, a timing island is formed. The master clock is now in holdover mode and continues to distribute its time to the local area (all devices receiving the same time can be construed as being on a timing island), with the master clock's ID (64-bit globally unique and 16-bit userconfigurable choices are available) allowing verification of which subsequent timestamps may be correctly compared.

The profile can be used for precise time synchronization of the devices in a substation, and between substations in a larger geographical area, if performance requirements of this standard are met.

The use of different physical layer communication technologies to carry Ethernet frames, including SONET/ SDH and wireless technologies, is not precluded if they can meet performance requirements of this standard.

Time distribution specified in this standard is based on the following basic assumptions:

- -All devices that participate in time distribution support this standard (except that slave devices may be IEC/IEEE 61850-9-3).
- -All devices are in the same time distribution domain.
- -All devices have point-to-point connections to their neighbors.
- -Transmit and receive cable delay for each point-to-point connection is assumed to be symmetrical. Known asymmetry in cable delay can be configured and corrected.

Cyber security is important in power system design. The scope of this standard does not include that topic. However, other standards and works in progress do address these concerns. For instance, the IEEE 1588 Revision Working Group at the time of this publication was actively investigating methods to secure PTP. Other standards regarding this subject include IEEE Std C37.240™, IEEE Std 1686™-2013, and IEC 62351-6.

Redundancy is an important consideration; some applications recommend or mandate support for different time distribution technologies, e.g., Global Positioning System (GPS) and IRIG-B. Support for multiple time distribution technologies at the same time is out of scope for this standard. Redundancy may be provided using this standard (multiple grandmasters and/or diverse network paths) using domains.

Specific environmental requirements are out of scope for this profile. However, devices conforming to this profile may also follow environmental standards such as IEEE Std 1613™ and IEC 61850-3. Vendors are encouraged to provide information regarding the effect of environmental influences on device performance, perhaps including the pass/fail criteria used when determining environmental compliance.

## Contents

1.  Overview  ................................................................................................................................................... 11

1.1  Scope  .................................................................................................................................................. 11

1.2  Purpose  ............................................................................................................................................... 11

2.  Normative references ................................................................................................................................ 11

3.  Definitions, special terms, and word usage

3.1  Definitions

................................................................................................ 12

.......................................................................................................................................... 12

3.2  Special terms ...................................................................................................................................... 15

3.3  Word usage ......................................................................................................................................... 15

4.  Abbreviations ............................................................................................................................................ 15

5.  Relationship to other standards ................................................................................................................. 16

5.1  IEEE Std 1588:2008 ........................................................................................................................... 16

5.2  IEC/IEEE 61850-9-3:2016  ................................................................................................................. 16

5.3  IEEE Std C37.238 .............................................................................................................................. 17

5.4  Configuration

...................................................................................................................................... 17

5.5  Compatibility with IEC/IEEE 61850-9-3:2016 .................................................................................. 17

5.6  Slave-only clocks

............................................................................................................................... 17

6.  Standard profile for power system applications

6.1  Identification

......................................................................................... 18

...................................................................................................................................... 18

6.2  TLVs  ................................................................................................................................................... 18

6.3  TimeInaccuracy  .................................................................................................................................. 20

Annex A (informative) Timing requirements for power system applications ................................................. 22

Annex B (informative) Compatibility with IEEE Std C37.238-2011 ............................................................. 24

Annex C (informative) Time performance parameters and their use for IEC 61850, IEEE C37.118, and

IRIG-B applications .................................................................................................................................. 25

Annex D (informative) Use of IEEE C37.238 messages for end devices (IRIG-B replacement) ................... 31

Annex E (informative) Mixed profile operation

............................................................................................. 35

Annex F (normative)  IEEE C37.238 PICS .................................................................................................... 36

Annex G (informative) Bibliography ............................................................................................................. 42

Copyright © 2017 IEEE. All rights reserved.

Authorized licensed use limited to: UNIVERSITY OF CONNECTICUT. Downloaded on June 25,2017 at 04:42:47 UTC from IEEE Xplore.  Restrictions apply.

## IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications

## 1.  Overview

## 1.1  Scope

This standard specifies an extended profile for the use of IEEE Std 1588-2008 1 in power system protection, control, automation, and data communication applications utilizing an Ethernet communications architecture.

The profile specifies a well-defined subset of IEEE 1588 mechanisms and settings aimed at enabling device interoperability, robust response to network failures, and deterministic control of delivered time quality. It is compliant with IEC/IEEE 61850-9-3:2016, which specifies the preferred physical layer, Ethernet; the higher level protocol used for message exchange, Precision Time Protocol (PTP); and the PTP protocol configuration parameters. Special attention is given to ensuring consistent and reliable time distribution within substations, between  substations,  and  across  wide  geographic  areas. As  such,  this  profile  extends  IEC/IEEE  618509-3:2016 with continuous monitoring of time inaccuracy, and optionally local time based on Coordinated Universal Time (UTC).

## 1.2  Purpose

The purpose of this standard is to facilitate adoption of IEEE Std 1588-2008 for power system applications requiring high-precision time synchronization. IEC/IEEE 61850-9-3:2016 and this standard specify a common subset of PTP parameters and options to provide global time availability, device interoperability, and failure management. This set of PTP parameters and options allows IEEE 1588-based time synchronization to be used in mission critical power system protection, control, automation, and data communication applications.

## 2.  Normative references

The following referenced documents are indispensable for the application of this document (i.e., they must be understood and used, so each referenced document is cited in the text and its relationship to this document is explained). For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments or corrigenda) applies.

IEC/IEEE 61850-9-3:2016, Communication networks and systems for power utility automation - Part 9-3: Precision time protocol profile for power utility automation. 2

1 Information on references can be found in Clause 2.

2 IEC/IEEE publications are available from the International Electrotechnical Commission (http://  www  .iec  .ch) and The Institute of Electrical and Electronics Engineers (http://  standards  .ieee  .org).

IEEE  Std  1588™-2008,  IEEE  Standard  for  a  Precision  Clock  Synchronization  Protocol  for  Networked Measurement and Control Systems. 3,4

## 3.  Definitions, special terms, and word usage

For the purposes of this document, the following terms and definitions apply. The IEEE Standards Dictionary Online should be referenced for terms not defined in this clause. 5

## 3.1  Definitions

absolute  time :  Time  maintained  by  the  international  standards  laboratories  that  form  the  basis  for  the International Atomic Time and Coordinated Universal Time timescales.

boundary clock (BC) :  A clock that has multiple Precision Time Protocol ports in a domain and maintains the timescale used in the domain. It may serve as the source of time, i.e., be a master clock, and may synchronize to another clock, i.e., be a slave clock. (IEEE Std 1588-2008)

clock :  A device participating in the Precision Time Protocol (PTP) that is capable of providing a measurement of the passage of time since a defined epoch. (adapted from IEEE Std 1588-2008)

NOTEIn the case of PTP ordinary and boundary clocks that are properly synchronized, the epoch is the epoch of the timescale in use. In the case of PTP transparent clocks, the epoch is locally defined and not necessarily aligned with the timescale. 6

default : When applied to attribute values and options means the configuration of a Precision Time Protocol device as it is delivered from the manufacturer. (IEEE Std 1588-2008)

device time inaccuracy : Time inaccuracy evaluated or measured between the time signal at the input of a device and the time signal that this device generates. (IEC/IEEE 61850-9-3:2016)

NOTE 1-Device time inaccuracy includes the uncertainties in the computation of the path delay assuming an ideal Pdelay\_Resp from an upstream neighbor, and the uncertainty introduced in responding to an ideal Pdelay\_Req from a downstream neighbor.

NOTE 2This definition applies to transparent clocks, boundary clocks, and media converters.

distribution time inaccuracy : Time inaccuracy evaluated or measured between the time signal at the output of a grandmaster and the time signal at the input of a slave clock.

NOTEDistribution time inaccuracy varies depending on the path the time signals take.

domain : A logical grouping of clocks that synchronize to each other using the protocol, but that are not necessarily synchronized to clocks in another domain. (IEEE Std 1588-2008)

end device :  A device with slave-only clock functionality.

3 IEEE publications are available from The Institute of Electrical and Electronics Engineers (http://  standards  .ieee  .org).

4 The IEEE standards or products referred to in Clause 2 are trademarks owned by the Institute of Electrical and Electronics Engineers, Incorporated.

5 The IEEE Standards Dictionary Online is available at http://  dictionary  .ieee  .org/  .

6 Notes in text, tables, and figures of a standard are given for information only and do not contain requirements needed to implement this standard.

NOTEEnd devices cover a plethora of applications with widely different time accuracy requirements (see Annex A). Their performance is out of scope, and they may or may not (see Annex D) use hardware time stamps and/or Pdelay messages to compensate their connecting-cable latencies. They may claim compliance with this standard provided that they accept the PTP specified in this profile and synchronize to the accuracy required for their intended use.

epoch : The origin of a timescale. (IEEE Std 1588-2008)

grandmaster-capable : Ordinary clock or boundary clock that is able to take the role of a grandmaster. (IEC/ IEEE 61850-9-3:2016)

NOTEA grandmaster-capable clock is not necessarily connected to a recognized standard time source.

grandmaster clock : Within a domain, a clock that is the ultimate source of time for clock synchronization using the protocol. (IEEE Std 1588-2008)

grandmaster  time  inaccuracy :  Time  inaccuracy  evaluated  or  measured  between  the  reference  time signal at the input of a grandmaster clock and the time signal(s) that the grandmaster generates. (IEC/IEEE 61850-9-3:2016)

NOTEGrandmaster time inaccuracy includes the uncertainty introduced in responding to an ideal Pdelay\_Req from a downstream neighbor.

holdover : A clock previously synchronized/syntonized to another clock (normally a primary reference or a master clock) but now free-running based on its own internal oscillator, whose frequency is being adjusted using data acquired while it had been synchronized/syntonized to the other clock. It is said to be in holdover or in the holdover mode, as long as it is within its accuracy requirements. (adapted from IEEE Std 1588-2008)

NOTESee Clause 7 of IEC/IEEE 61850-9-3:2016 regarding accuracy requirements for this profile.

intelligent electronic device (IED) : Any device incorporating one or more processors with the capability to receive or send data/control from or to an external source (e.g., electronic multifunction meters, digital relays, controllers).

link : A network segment between two Precision Time Protocol ports supporting the peer delay mechanism of this standard. The peer delay mechanism is designed to measure the propagation time over such a link. (adapted from IEEE Std 1588-2008)

network device :  A boundary clock or a transparent clock.

network time inaccuracy : Time inaccuracy evaluated or measured between the reference time signal at the input of a grandmaster clock and the time signal at the input of a given slave clock, considering the worst path between the grandmaster(s) and the slave. (IEC/IEEE 61850-9-3:2016)

NOTENetwork time inaccuracy varies depending on the path the time signals take.

ordinary clock :  A clock that has a single Precision Time Protocol port in a domain and maintains the timescale used in the domain. It may serve as a source of time, i.e., be a master clock, or may synchronize to another clock, i.e., be a slave clock. (adapted from IEEE Std 1588-2008)

NOTE-An ordinary clock is a clock that either can be grandmaster-capable or slave-only.

Precision Time Protocol (PTP) : The protocol defined by IEEE Std 1588-2008. As an adjective, it indicates that  the  modified  noun  is  specified  in  or  interpreted  in  the  context  of  IEEE  Std  1588-2008.  (IEEE  Std 1588-2008)

Precision Time Protocol (PTP) port : A logical access point of a clock for PTP communications to the communications network. (IEEE Std 1588-2008)

profile : The set of allowed Precision Time Protocol features applicable to a device. (IEEE Std 1588-2008)

recognized standard time source : A recognized standard time source is a source external to Precision Time Protocol that provides time and/or frequency as appropriate that is traceable to the international standards laboratories  maintaining  clocks  that  form  the  basis  for  the  International  Atomic  Time  and  Coordinated Universal Time timescales. Examples of these are Global Positioning System, Network Time Protocol, and National Institute of Standards and Technology timeservers. (adapted from IEEE Std 1588-2008)

residence time : The time difference between ingress and egress time stamps for an IEEE C37.238 event message.

slave-only clock :  An ordinary clock that has no ports capable of Precision Time Protocol Master state.

NOTE-See 9.2.2 of IEEE Std 1588-2008.

source time inaccuracy : Time inaccuracy evaluated or measured between absolute time and the reference time signal at the input of a grandmaster.

NOTE-Source time inaccuracy considers, e.g., the Global Positioning System or the DCF77 time inaccuracy as received at a particular geographical location.

synchronized clocks : Two clocks are synchronized to a specified uncertainty if they have the same epoch and their measurements of the time of a single event at an arbitrary time differ by no more than that uncertainty. (IEEE Std 1588-2008)

time error : Deviation from the time reference used for measurement or synchronization caused by a network element, evaluated over a short time span (a few sync intervals). (IEC/IEEE 61850-9-3:2016)

time inaccuracy : Time error not exceeded by 99.7% of the measurements, evaluated over a series of 1000 measurements (about 20 min) in steady state. (IEC/IEEE 61850-9-3:2016)

timescale :  A linear measure of time from an epoch. (IEEE Std 1588-2008)

total  time  inaccuracy :  Time  inaccuracy  evaluated  or  measured  between  the  time  maintained  by  the international standards laboratories that form the basis for the International Atomic Time and Coordinated Universal  Time  timescales  and  the  time  signal  at  the  input  of  a  slave  clock.  (adapted  from  IEC/IEEE 61850-9-3:2016)

NOTE-The TimeAccuracy attribute of IEC 61850-7-2 [B2] sums the total time inaccuracy and the time inaccuracy of the sampling. Therefore, the mapping from total time inaccuracy to TimeAccuracy is implementation-dependent.

traceable : Having the property of traceability. See also: traceability .

traceability : A property of the result of a measurement or the value of a standard whereby it can be related to stated references, usually national or international standards, through an unbroken chain of comparisons all having stated uncertainties. (adapted from the International Vocabulary of Basic and General Terms in Metrology [B10] 7 ) See also: recognized standard time source .

7 The numbers in brackets correspond to those of the bibliography in Annex G.

NOTE-For Precision Time Protocol applications in the power industry, traceability generally means 'traceability to a recognized standard time source,' which distributes time originating from the international time standard comprising an ensemble of atomic clocks maintained by recognized national laboratories.

transparent clock (TC) : A device that measures the time taken for a Precision Time Protocol (PTP) event message to transit the device and provides this information to clocks receiving this PTP event message. (IEEE Std 1588-2008)

## 3.2  Special terms

IEEE C37.238 device: A node with one or more Ethernet ports that is compliant to IEEE Std C37.238-2017.

NOTEIEEE C37.238 devices are network devices and ordinary clocks.

IEEE C37.238 message: A PTP message compliant to IEEE Std C37.238-2017.

## 3.3  Word usage

In this document, the word shall is used to indicate a mandatory requirement. The word should is used to indicate a recommendation. The word may is used to indicate a permissible action. The word can is used for statements of possibility and capability.

## 4.  Abbreviations

| ATOI   | alternate time offset indicator (TLV, per IEEE Std 1588-2008)                    |
|--------|----------------------------------------------------------------------------------|
| BC     | boundary clock (IEEE Std 1588-2008)                                              |
| BMC    | best master clock (IEEE Std 1588-2008)                                           |
| CTQ    | continuous time quality (IEEE Std C37.118.1™-2011 [B7])                          |
| DCF77  | German radio station DCF, transmitting time code at 77.5 kHz frequency           |
| DNP3   | Distributed Network Protocol Version 3 (IEEE Std 1815™-2010 [B5])                |
| DST    | Daylight Saving Time                                                             |
| GNSS   | Global Navigation Satellite System                                               |
| GPS    | Global Positioning System                                                        |
| ID     | identification                                                                   |
| IED    | intelligent electronic device (IEC 61850-7-2:2010 [B2])                          |
| IERS   | International Earth Rotation and Reference Systems Service                       |
| IRIG-B | Inter-Range Instrumentation Group Serial Time Code B(IRIG Standard 200-04 [B11]) |
| MAC    | media access control (IEEE Std 802.3™-2011 [B4])                                 |
| OUI    | organizational unique identifier (allocated by the IEEE)                         |

NOTEThe OUI is typically used in specifications or the implementation of devices for the purpose of identification. It identifies the organization that owns the OUI-dependent sub-identifier and may not necessarily be the organization that defines the specification or provides the hardware. 8

8 The IEEE OUI listing is available at http://  standards  .ieee  .org/  develop/  regauth/  oui/  public  .html.

| PMU   | phasor measurement unit (IEEE Std C37.118.1-2011 [B7])   |
|-------|----------------------------------------------------------|
| PDST  | Pacific Daylight Saving Time                             |
| PST   | Pacific Standard Time                                    |
| PTP   | Precision Time Protocol (IEEE Std 1588-2008)             |
| RAC   | Registration Authority Committee of IEEE                 |
| RSTP  | Rapid Spanning Tree Protocol                             |
| SBS   | straight binary seconds                                  |
| SCADA | Supervisory Control and DataAcquisition                  |
| SOC   | second of century                                        |
| SV    | sampled value (IEC 61850-9-2:2011)                       |
| TAI   | InternationalAtomic Time                                 |
| TC    | transparent clock (IEEE Std 1588-2008)                   |
| TLV   | type, length, value (IEEE Std 802.1AB™-2009 [B3])        |
| TQ    | time quality (IEEE Std C37.118.1-2011 [B7])              |
| UTC   | Coordinated Universal Time                               |

## 5.  Relationship to other standards

## 5.1  IEEE Std 1588:2008

IEEE Std  1588:2008,  Precision  Time  Protocol,  provides  methods  allowing  accurate  time  and  frequency transfer from one point (a grandmaster) to another (a slave) over a communications network comprising transparent clocks (TCs) and boundary clocks (BCs). It provides several alternative methods, but does not establish performance requirements. It is most often used over Ethernet, but can be used with many other network technologies. Thus, it can be applied in a wide variety of different industries.

To address the issues that arise from the many options it provides, IEEE Std 1588:2008 recommends the creation of 'profiles.' To enhance interoperability within an industry, a standard organization chooses particular options (from the selection provided by IEEE Std 1588:2008) appropriate for a specific application. Profiles may establish specific performance requirements. Additional features defined in a profile, but not present in IEEE Std 1588:2008 are called extensions.

## 5.2  IEC/IEEE 61850-9-3:2016

This standard is a profile of IEEE Std 1588:2008 jointly developed by the IEEE Power and Energy Society Power System Relaying Committee (PSRC) Working Group H24 and Substations Committee Working Group C7, and the IEC Technical Committee 57 Working Group 10, as a common base profile for the electric power industry. It is a Layer 2, peer-to-peer profile of based on J.4 of IEEE Std 1588-2008. It specifies options to be used and device performance, with the goal to deliver time to slaves with an accuracy of one microsecond or better over a network comprising up to 15 TCs. An optional extension allows operation with doubly attached clocks  for  critical,  high-availability  applications.  Transmission  of  local  time  through  the ALTERNATE\_ TIME\_OFFSET\_INDICATOR is optionally supported.

## 5.3  IEEE Std C37.238

This standard is an extension of IEC/IEEE 61850-9-3:2016, developed by Working Group H24/Sub C7 to provide additional functionality. The additional functions comprise two type, length, and values (TLVs): one mandatory TLV, providing additional information to monitor clock performance in real time, and an optional TLV, providing local time zone information, to ease transition from former Inter-Range Instrumentation Group B (IRIG-B) systems and for local display applications.

IEEE Std C37.238-2011 was superseded upon the IEEE-SA Standards Board approval of both IEC/IEEE 61850-9-3:2016 and this revision.

NOTEEven if it receives Announce messages with the IEEE C37.238 TLV attached, an IEEE C37.238 clock cannot detect that all TCs or BCs up to the grandmaster are also IEEE C37.238 compliant, so it is the responsibility of the network engineer to ensure this, also considering reconfiguration after failure of any network element [Rapid Spanning Tree Protocal (RSTP) bridge or clock].

## 5.4  Configuration

The default configuration for the domain, defaultDS.domainNumber, shall be 254. Implementation claiming conformance to this standard shall be able to configure domain numbers of the range 0 to 127 and the single value 254. The value 254 shall be used only for implementations of this profile that are conformant to Annex F of IEEE Std 1588-2008.

NOTE 1-This complies with IEEE Std 1588-2008 with the exception of the use of the reserved domain 254. The value 254 is an exception granted to this profile.

For operation in an IEC/IEEE 61850-9-3 network, domain number shall be configured to IEC/IEEE 61850-93 domain (93 is recommended).

NOTE 2Network engineering should ensure that all clocks participating in the PTP time distribution are set to the same domain(s) (see 7.9 of IEC/IEEE 61850-9-3:2016). More than one domain may be in use; for example, to allow redundant masters and/or network paths. See also Annex E.

Devices conformant to this standard shall have non-volatile settings that preserve their configuration during a power cycle, including the ability to be configured to comply with IEC/IEEE 61850-9-3:2016.

## 5.5  Compatibility with IEC/IEEE 61850-9-3:2016

All clocks claiming conformity with this standard shall comply with IEC/IEEE 61850-9-3:2016 and therefore can be used without restriction in an IEC/IEEE 61850-9-3 network (simply by setting the domain number to that of the network).

## 5.6  Slave-only clocks

Performance and features of slave-only clocks are not within the scope of this profile. In particular, for lower accuracy requirements (see Annex A ), slave-only clocks may not implement hardware time stamping and/or delay mechanisms. Slave-only clocks may not require or make use of the time inaccuracy information in the IEEE C37.238 TLV or the local offset information in the Alternate Time Offset Indicator TLV. Such slaveonly clocks may claim conformity with this profile by demonstrating that they meet their specified level of performance when connected to an IEEE C37.238 conformant network.

## 6.  Standard profile for power system applications

## 6.1  Identification

PTP Profile

IEEE Standard Profile for Use of IEEE 1588 Precision Time Protocol in Power System Applications

Version: 2.0

Profile identifier: 1C-12-9D-00-00-00

This profile is specified by the IEEE 1588 Profile for Power System Applications Working Group of the IEEE Power System Relaying Committee and IEEE Power System Substations Committee.

## 6.2  TLVs

The following TLVs shall be supported by all grandmaster-capable devices:

- -IEEE\_C37\_238 TLV (profile-specific)
- -ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV (specified by 16.3 of IEEE Std 1588-2008)

The IEEE\_C37\_238 TLV shall be appended to IEEE C37.238 Announce messages.

The use of ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV is optional, when used it shall follow the IEEE\_C37\_238 TLV. Further instances of ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV for multi timezone support shall follow the above two TLVs.

The implementation of these IEEE\_C37\_238 TLVs shall conform to 14.3 of IEEE Std 1588-2008 for an ORGANIZATION\_EXTENSION\_TLV.

Additional TLVs, if present, shall follow the mandatory TLV.

NOTE-Subclause 13.4 of IEEE Std 1588-2008 recommends that the interpretation of a TLV should not depend on its position in the message. This profile, however, intentionally mandates a specific TLV order so that simple end devices can access data directly by using fixed byte position in the message frame (see Annex D for details). This also minimizes testing because it does not require testing of free order of TLVs.

## 6.2.1  IEEE\_C37\_238 TLV (profile-specific)

The IEEE\_C37\_238 TLV is used to communicate the following:

- -Grandmaster ID (optional)
- -Total time inaccuracy

The IEEE\_C37\_238 TLV field values shall be as follows:

- a) tlvType (Enumeration16); ORGANIZATION\_EXTENSION value = 0003 hex
- b) lengthField (UInteger16); The number of remaining octets (after this) in the TLV value = 0012 hex
- c) organizationId (Octet[3]); The organizational unique identifier (OUI) value assigned by the IEEE Registration Authority Committee (RAC) = 1C129D hex
- d) organizationSubType (Enumeration24) value = 000002 hex

- e) dataField (12 octets) as follows:
- 1) grandmasterID (2 octets) value 0000-FFFF hex, if not used the value is 0000 hex
- 2) reserved (4 octets) set to 00000000 hex
- 3) totalTimeInaccuracy (Uinteger32) value 00000000-FFFFFFFF hex, in nanoseconds, where the maximum value (0xFFFFFFFF, approximately 4.29 s) indicates that this maximum value has been exceeded or the value is unknown
- 4) reserved (2 octets) set to 0000 hex

## 6.2.2  ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV

The implementation of this TLV shall conform to the terms of 16.3.3 of IEEE Std 1588-2008.

To provide local time, the following ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV field values shall be as follows:

- -keyField shall be &gt;0 when the offset is valid, else 0.
- -currentOffset shall be the current offset of the local time, in seconds, relative to the PTP timescale, including both accumulated leap seconds (UTC-PTP) and local offset (LCL-UTC).
- -jumpSeconds shall be 0 when the local time does not use Daylight Saving Time (DST), else shall be Nx900 with N an integer &lt;&gt; 0; except that jumpSeconds shall be ±1 when, and only when, a leap second is within the next 10 s ± 30% (see NOTE 2).
- -When not zero, timeOfNextJump shall be the seconds portion of the PTP time at the next DST event, OR the next leap second; this shall be provided for at least the 10 s prior to each event.
- -displayName (PTPText, X octets) shall be as specified in 5.3.9 of IEEE Std 1588-2008. Support and use of this field is optional, default being a single octet of value 0.
- -pad (0 or 1 octet) set to zero; shall be transmitted only if needed to make length of the extension an even number of octets (i.e., if X is odd).

NOTE 1The Announce message's currentUtcOffsetValid flag must be constantly checked to see if the local time is valid.

NOTE 2-Leap seconds and DST changes do not normally happen at the same time. If in the future, both changes are coincident, then jumpSeconds will be the sum of the DST change and ±1 for the leap second.

NOTE 3The above specification provides alternative time offset indicator (ATOI) TLVs (in IEEE C37.238 Announce messages) that are compliant to the IEEE 1588 ATOI TLV specification, when using the clarifications 9, 10 that were supplied to the IEEE PSRC Working Group H24/SubC7 by the IEEE 1588 Maintenance Working Group.

## 6.3  TimeInaccuracy

IEEE C37.238 totalTimeInaccuracy provides a mechanism using the profile-specific IEEE\_C37\_238 TLV, defined in 6.2, for applications to determine whether the time inaccuracy in the delivered time is acceptable.

9 Clarification 1: The IEEE 1588 requirement: 'The Alternate Time Offset Indicator shall not be used to indicate the offset or pending changes in the offset of UTC from the PTP timescale.' (changes caused by leap seconds) says only that this is a requirement on the user of the ATOI, namely an end application in a slave clock; it is therefore actually not in conflict with the IEEE 1588 requirement that 'If a discontinuity (jump) is about to occur, the node shall indicate this in a contiguous sequence of at least portDS.announceReceiptTimeout + 1 Announce messages transmitted immediately before the discontinuity.'

10 Clarification 2: When the Sync messages' timescale is PTP, the node time is PTP; thus the IEEE 1588 requirement 'The value of currentOffset shall be the offset of the alternate time, in seconds, from the node's time. The alternate time is the sum of this value and the node's time.' requires that the currentOffset shall be from PTP (not UTC as some clock vendors have assumed). Suggestion: To accommodate master-clocks whose designers had misinterpreted the IEEE 1588 standard, it is recommended that IEEE C37.238 slave clocks be designed to function correctly regardless of the interpretations used (as suggested in the note in D.2.3).

Total time inaccuracy comprises the sum of the following three values:

- -Grandmaster time inaccuracy
- -Distribution time inaccuracy
- -Source time inaccuracy

These three items are summed in the field totalTimeInaccuracy. This field is initialized by the grandmaster to the grandmaster time inaccuracy plus the source time inaccuracy, and then incremented by TCs and BCs.

Grandmaster time inaccuracy is provided by grandmaster clocks. Note that this value provides the clock's estimated time inaccuracy, as defined in 3.1.3 of IEC/IEEE 61850-9-3:2016, as opposed to the mean time error used for clockAccuracy of the clockQuality field specified in 7.6.2.5 and Table 6 of the IEEE Std 1588-2008. This value should be updated in real time, as conditions change. Factors that may be used by a grandmaster clock to estimate its time inaccuracy include time reference processing errors, holdover oscillator stability, and environmental conditions.

Source time inaccuracy is dependent on the time source used, and is required for the correct setting of the grandmaster clock's totalTimeInaccuracy. It represents the time inaccuracy contributed by the grandmaster's recognized standard time source, such as Global Positioning System (GPS) or German radio station DCF, transmitting time code at 77.5 kHz frequency (DCF77).

Distribution time inaccuracy represents the accumulated time inaccuracy between the grandmaster clock and an end device. Distribution time inaccuracy is a component of totalTimeInaccuracy. TotalTimeInaccuracy shall be automatically incremented by TCs and BCs. This value shall be updated in real time, as conditions change, so that end devices know when the time is usable for their applications.

Note that distribution time inaccuracy will normally vary from one end device to another, considering the network topology (number of hops, real-time performance of TCs/BCs, etc.). End devices with more critical requirements may advantageously be located 'closer' (in terms of hops) to the grandmaster. Since each TC or BC increments the totalTimeInaccuracy field, each end device will receive the most accurate value of totalTimeInaccuracy, reflecting the actual network topology. Changes in topology (caused for instance by spanning tree protocols) will automatically be reflected in the totalTimeInaccuracy received by each end device.

Network time inaccuracy, defined in IEC/IEEE 61850-9-3:2016, is the sum of grandmaster time inaccuracy and distribution time inaccuracy.

Device time inaccuracy is the time inaccuracy that a device contributes to the total time inaccuracy. Device manufacturers shall specify maximum device time inaccuracy. This value shall not exceed the value specified in Clause 7 of IEC/IEEE 61850-9-3:2016.

Overall time inaccuracy should be calculated during network engineering stage based on device specifications and network design. All time inaccuracy values used in this calculation should be based on the manufacturer's specified device time inaccuracy values, along with the source time inaccuracy of the recognized standard time source.

NOTEFor example, TCs could use the following parameters to define their device time inaccuracy:

- -Error introduced by the time-stamping hardware
- -Error of the Pdelay measurements on the receiving port
- -Syntonization error, i.e., uncertainty combined with the residence time of previous Sync messages

## Annex A

(informative)

## Timing requirements for power system applications

## A.1  Overview

This profile for use of IEEE 1588 Precision Time Protocol (PTP) in power system applications describes a robust, Ethernet-based method for precise clock synchronization. Although optimized for stringent timing applications, it is versatile enough to allow simple implementations while retaining good balance between performance and the complexity of implementation.

Substation applications using PTP time distribution can be broadly divided into following categories (see Table A.1):

- a) General purpose, visually observed time indicators (&lt; ± 100 ms)
- b) Time stamping of Supervisory Control and Data Acquisition (SCADA) data and operational data logs (&lt; ± 1 ms)
- c) Inter-Range Instrumentation Group B (IRIG-B) replacement applications with limited distance to the PTP grandmaster (&lt; ± 1 µs)
- d) Extended distance applications (full PTP support, &lt; ± 1 µs)

The first three categories operate as slave-only clocks and are not allowed to transmit IEEE C37.238  Announce messages to participate in the Best Master Clock election process. They are located at the network edge (end device) and do not pass PTP traffic to others, meaning they are not required to support transparent clock (TC) functionality. End devices in the first three categories are expected to process IEEE C37.238 Sync, Follow\_ Up, and Announce messages, but do not need to support Pdelay exchange or transmit IEEE C37.238 Pdelay messages. They process all IEEE C37.238 Sync message fields (including correctionField), support one-step and/or two-step operation (with and without Follow\_Up), and correctly process the leap second events, as described in Annex D.

Table A.1-Categories of end devices

| End device category   | time accuracy (application)   | Pdelay support   | TLVorder         | default domain (settable range)   | ATOITLV support (application)   |
|-----------------------|-------------------------------|------------------|------------------|-----------------------------------|---------------------------------|
| Category 1            | < ± 100 ms                    | optional         | fixed order      | 254 (1-127)                       | optional                        |
| Category 2            | < ± 1 ms                      | optional         | fixed order      | 254 (1-127)                       | optional                        |
| Category 3            | < ± 1 µs                      | optional         | fixed order      | 254 (1-127)                       | optional                        |
| Category 4            | < ± 1 µs                      | mandatory        | fixed order      | 254 (1-127)                       | optional                        |
| IEC/IEEE 61850-9-3    | < ± 1 µs                      | mandatory        | any order (free) | 0 (0-255) {93 recommended}        | optional                        |

## A.2  Description

Category 1 end devices typically target general purpose processors and do not require PTP-specific hardware. Although some evaluation of the software stack delays may be required, this category does not generally need specialized software techniques. The software stack needs to be capable of receiving and analyzing layer 2 messages.

Category 2 end devices may target general purpose processors and do not necessarily require PTP-specific hardware. Due to additional precision requirements, this implementation may need to use interrupts or careful/ customized software implementation. While it may be possible to a use general-purpose software stack, some optimization is likely to be required.

Category 3 end devices are intended for direct replacement of IRIG-B; for example, for pulse per second IRIG-B distribution networks in which the distance between the last PTP source [PTP grandmaster, boundary clock (BC), or TC] and the category 3 slave does not exceed 100 m (propagation delay &lt; 0.5 µs). It is intended to  replicate  current  applications  that  do  not  explicitly  compensate  IRIG-B  cable  length.  Category  3  end devices may target general purpose microprocessors, but depending on operating system, hardware, and other factors, may require PTP-specific hardware support (hardware-based timestamping). Category 3 end devices are expected to emulate the Category 4 slave behavior with the exception of not measuring the length of the last cable/fiber segment (not supporting IEEE C37.238 Pdelay message exchange).

Category 4 end devices require hardware assisted timestamping and participate in the IEEE C37.238 Pdelay message exchange. Category 4 end devices may be placed anywhere in the network.

## Annex B

(informative)

## Compatibility with IEEE Std C37.238-2011

The  previous  version  of  this  standard,  IEEE  Std  C37.238-2011,  separated  grandmaster  time  inaccuracy and what was then called NetworkTimeInaccuracy into two fields. The first, grandmasterTimeInaccuracy, was located immediately before totalTimeInaccuracy in this version (now a reserved field). The second, networkTimeInaccuracy, was located where totalTimeInaccuracy is now found.

In that version, the two fields were treated separately and summed in the end devices. There being no advantage to keeping them separate, in this version they were combined into one.

Note also that the grandmaster time inaccuracy of IEEE Std C37.238-2011 included the inaccuracy of the time source. This differs from the IEC/IEEE 61850-9-3:2016 definition of this term. The present version is consistent with IEC/IEEE 61850-9-3:2016, and source time inaccuracy has been introduced to allow inclusion of the time inaccuracy of the time source.

To ensure compatibility with grandmasters compliant with the earlier version, an end device may still sum these two fields (reserved field = 0 plus totalTimeInaccuracy) and achieve the same result as the previous version (grandmasterTimeInaccuracy plus networkTimeInaccuracy). Systems including only grandmasters compatible with this version may use totalTimeInaccuracy alone.

Transparent  clocks  (TCs)  compatible  with  the  previous  version  are  automatically  compatible  with  this version (provided they recognize the new version number) because the field they increment, whether called totalTimeInaccuracy or networkTimeInaccuracy, is located at the same offset in the type, length, and value (TLV). Boundary clocks (BCs) were not included in the previous version, and they have been added to this standard and in IEC/IEEE 61850-9-3:2016.

The required behavior of transparent clocks has been changed from muting all egressing messages when the TC is not stable (exceeding 50 ns inaccuracy), to always setting its egressing totalTimeInaccuracy field to an appropriate value.

The 2-octet field grandmasterID has been expanded to allow the full 16-bit range of values, its use is made optional. In the previous version, this field was 2 octets but the range of values was limited to 0x0003-0x00FE.

The ranges of the two user-settable priority fields, defaultDS.priority1 and defaultDS.priority2, have been restored to the standard ranges (0 through 255).

The version of this standard used by the grandmaster may be identified by the organizationSubType in this TLV. The previous version set this field to 0x01; this version sets it to 0x02.

IEEE Std C37.238-2011 states that IEEE C37.238 Announce messages without two mandatory TLVs attached shall be ignored by the BMCA. This alters general BMCA algorithm and leads to various possibilities such as not selecting a better grandmaster that does not have TLVs appended (e.g., IEC/IEEE 61850-9-3:2016), more than one grandmaster sending Sync messages, some end devices (e.g., IEEE Std C37.238-2011) synchronizing to  a  different  grandmaster  than  others,  etc.  The  requirement  to  ignore Announce  messages  without  two mandatory TLVs has been removed in this revision of the standard.

## Annex C

(informative)

## Time performance parameters and their use for IEC 61850, IEEE C37.118, and IRIG-B applications

This annex describes the following:

- -IEEE C37.238 time performance parameters
- -Use of time performance parameters for IEC 61850, IEEE C37.118™, and IRIG-B applications

## C.1  Time performance parameters

Power substation applications require accurate time synchronization and time quality information for phasor estimations relative to Coordinated Universal Time (UTC) time, sample synchronization, event time stamping, and other functions.

Time quality information generally includes the following:

- -Time error estimate
- -Traceability to a recognized standard time source

All IEEE C37.238 clocks, including grandmaster clocks, provide the totalTimeInaccuracy field, this provides an estimate of the time inaccuracy received by a device.

Grandmaster clocks normally receive time from a primary reference, via Global Navigation Satellite System (GNSS) such as GPS, by a means that is outside this standard.

In addition to the Announce messages' 64-bit grandmaster ID (sufficient for IEC 61850 applications), a 16-bit grandmaster ID parameter is provided in the IEEE\_C37\_238 type, length, and value (TLV); this has the possible advantage of being user-settable, and also provide an immunity to ID changes as a result of hardware changes.

IEEE C37.238 time performance parameters can also be mapped into application specific parameters. Their use for IEC 61850, IEEE C37.118, and IRIG-B applications is described in C.2, C.3, and C.4.

More detailed information regarding clock performance can be obtained from Precision Time Protocol (PTP) datasets. Boundary clocks (BCs), ordinary clocks, and transparent clocks (TCs) are required to support specific datasets, as required by Clause 8 of IEEE Std 1588-2008. If these clocks also support another protocol, such as Distributed Network Protocol Version 3 (DNP3) or Modbus, they may also support the mapping of the data available from either the clock datasets or TC datasets to provide that data via that supported protocol. Mapping of these values is outside the scope of this standard.

Slave clocks may need to track the performance of their parent in order to determine whether the parent's signal is a valid signal, as suggested by A.4 of IEEE Std 1588-2008. Remote substations utilizing PTP may be subject to grandmaster clock failure when time or frequency can become incorrect, plus deliberate effects such as GPS spoofing that substitutes the real GPS signals with other signals. Mechanisms to provide this performance monitoring may be considered in a future revision of the IEEE Std C37.238.

## C.2  Use of IEEE Std C37.238 for IEC 61850 applications

IEC 61850 specifies TimeStamp type for time stamping all data provided by intelligent electronic devices (IEDs).

## C.2.1  IED data timestamping

The IEC 61850 TimeStamp represents a UTC time with the epoch of midnight (00:00:00) of 1970-01-01 (IEC 61850-7-2 [B2]). The PTP TimeStamp represents a time with the epoch of 31 December 1969 23:59:51.999918 UTC. 11

The IED should therefore set the following IEC 61850 fields as shown:

If the required TimeStamps' timescale = UTC

LeapSecondsKnown = True

SecondsSinceEpoch = PTP Time (seconds) - currentUtcOffset 12

FractionOfSecond  13 = (Integer) PTP Time (nanoseconds) × 2 24 × 10 -9

If the required TimeStamps' timescale = PTP

LeapSecondsKnown = False

SecondsSinceEpoch = PTP Time (seconds)

FractionOfSecond = (Integer) PTP Time (nanoseconds) × 2 24 × 10 -9

The IEEE C37.238 totalTimeInaccuracy provides information for setting IEC 61850 TimeAccuracy value.

Per IEC 61850-7-2 [B2] , the IEC 61850 TimeAccuracy is the number of significant bits n in the TimeStamp's FractionOfSecond field (the latter being the number of 2 -24 s (approximately 60 ns) in the current UTC second).

Mapping between the IEEE C37.238 totalTimeInaccuracy and the IEC 61850 TimeAccuracy is shown in Table C.1 (refer to IEC 61850-5 [B1]).

Table C.1-Mapping between IEEE C37.238 totalTimeInaccuracy and IEC 61850 TimeAccuracy

| IEEE C37.238 TimeInaccuracy, plus uncertainty (in ns) in process generating the IED data   | IEC 61850-7-2 [B2] TimeAccuracy code n   | IEC 61850-7-2 [B2] TimeAccuracy code n   | IEC 61850-7-2 [B2] TimeAccuracy code n             |
|--------------------------------------------------------------------------------------------|------------------------------------------|------------------------------------------|----------------------------------------------------|
| IEEE C37.238 TimeInaccuracy, plus uncertainty (in ns) in process generating the IED data   | n                                        | Resulting time accuracy (2 -n )          | Time performance class defined in IEC 61850-5 [B1] |
| > 500 000 001                                                                              | 0                                        |                                          |                                                    |
| 250 000 001 to 500 000 000                                                                 | 1                                        |                                          |                                                    |
| 125 000 001 to 250 000 000                                                                 | 2                                        |                                          |                                                    |
| 62 500 001 to 125 000 000                                                                  | 3                                        |                                          |                                                    |
| 31 250 001 to 62 500 000                                                                   | 4                                        |                                          |                                                    |
| 15 625 001 to 31 250 000                                                                   | 5                                        |                                          |                                                    |
| 7 812 501 to 15 625 000                                                                    | 6                                        |                                          |                                                    |

Table continues

11 Historic note: Although these statements indicate a difference of 8 s and 82 μs between the two epochs, such difference does not exist; the difference between these epochs is actually exactly 8 s because since 1972 the seconds rollover of UTC and PTP have been aligned. 12 During a leap-second event, if leap-second indication is communicated, this value should be changed before the updated currentUtcOffset is received (using flagField[9:8]).

13 For the most accurate results, 1/2 the quantization step of 2 -24 s shall be added either at this IED (doing the conversion from IEEE Std C37.238 to IEC 61850) or somewhere else (e.g., at the devices using the IEC 61850 messages), but only once.

Table C.1-Mapping between IEEE C37.238 totalTimeInaccuracy and IEC 61850 TimeAccuracy (continued)

| IEEE C37.238 TimeInaccuracy, plus uncertainty (in ns) in process generating the IED data   | IEC 61850-7-2 [B2] TimeAccuracy code n   | IEC 61850-7-2 [B2] TimeAccuracy code n   | IEC 61850-7-2 [B2] TimeAccuracy code n             |
|--------------------------------------------------------------------------------------------|------------------------------------------|------------------------------------------|----------------------------------------------------|
| IEEE C37.238 TimeInaccuracy, plus uncertainty (in ns) in process generating the IED data   | n                                        | Resulting time accuracy (2 -n )          | Time performance class defined in IEC 61850-5 [B1] |
| 3 906 251 to 7 812 500                                                                     | 7                                        | Approx. 7.8 ms                           | 10 ms (performance class T0)                       |
| 1 953 126 to 3 906 250                                                                     | 8                                        |                                          |                                                    |
| 976 563 to 1 953 125                                                                       | 9                                        |                                          |                                                    |
| 488 282 to 976 562                                                                         | 10                                       | Approx. 0.9 ms                           | 1 ms (performance class T1)                        |
| 244 141 to 488 281                                                                         | 11                                       |                                          |                                                    |
| 122 071 to 244 140                                                                         | 12                                       |                                          |                                                    |
| 61 036 to 122 070                                                                          | 13                                       |                                          |                                                    |
| 30 518 to 61 035                                                                           | 14                                       | Approx. 61 μs                            | 100 µs (performance class T2)                      |
| 15 259 to 30 517                                                                           | 15                                       |                                          |                                                    |
| 7 630 to 15 258                                                                            | 16                                       | Approx. 15 μs                            | 25 µs (performance class T3)                       |
| 3 815 to 7 629                                                                             | 17                                       |                                          |                                                    |
| 1 908 to 3 814                                                                             | 18                                       | Approx. 3.8 μs                           | 4 µs (performance class T4)                        |
| 954 to 1 907                                                                               | 19                                       |                                          |                                                    |
| 477 to 953                                                                                 | 20                                       | Approx. 0.9 μs                           | 1 µs (performance class T5)                        |
| 239 to 476                                                                                 | 21                                       |                                          |                                                    |
| 120 to 238                                                                                 | 22                                       |                                          |                                                    |
| 60 to 119                                                                                  | 23                                       |                                          |                                                    |
| 0 to 59                                                                                    | 24                                       |                                          |                                                    |

## C.3  Use of IEEE Std C37.238 for IEEE C37.118 applications

The IEEE C37.118 TimeStamp represents a UTC time with the epoch of midnight (00:00:00) of 1970 01 01. The PTP TimeStamp represents a time with the epoch of 31 December 1969 23:59:51.999918 UTC. 14

The IED should therefore set the following IEEE C37.118 fields as shown:

second of century (SOC) = PTP Time (seconds) - currentUtcOffset 15

FRACSEC[23:0] 5 = (Integer) PTP Time (nanoseconds) × 2 24 × 10 -9 (for IEC 61850 compatibility) 16

IEEE C37.118 synchrophasor applications require information on time quality and traceability to a recognized standard time source, e.g., UTC (IEEE Std C37.118-2005 [B6], IEEE Std C37.118.1-2011 [B7], and IEEE Std C37.118.2™-2011 [B8]).

IEEE Std C37.238 provides time quality and traceability via totalTimeInaccuracy; it provides a loss of clock (loss of synchronization) using clockClass (6 when locked).

IEEE  Std  C37.118.1-2011  [B7]  requires  providing  a  time  synchronization  and  time  quality(inaccuracy) indication with each measurement. Since it only covers measurement requirements and not any external reporting, the format and representation is not specified.

14 See footnote 10.

15 See footnote 11.

16 Other quantization steps are allowed by IEEE Std C37.118 [B6] (for other applications).

## IEEE Standard Profile for Use of IEEE 1588™ Precision Time Protocol in Power System Applications

In IEEE Std C37.118.2-2011 [B8], bit[13] of the STAT in the Synchrophasor Data frame is normally cleared; but set if the time source is not 'synchronized' (locked) to a traceable source, and within the inaccuracy needed for its application..

IEEE Std C37.118.2-2011 [B8] also provides time quality (TQ) (inaccuracy) in the data frame, both for the overall frame in the FRACSEC word (MSG\_TQ) and for each phasor measurement unit (PMU) segment in the STAT word (PMU\_TQ). These indications should be derived from the IEEE Std C37.238 totalTimeInaccuracy value.

The IEEE C37.238 totalTimeInaccuracy represents an estimate of the time inaccuracy error provided to the end device, in this case the PMU. The PMU should process the timing signal internally as it is applied to the measurement and data. This internal processing may add some uncertainty to the timing precision. The totalTimeInaccuracy value provided under IEEE Std C37.238 should be increased sufficiently to cover these internal PMU inaccuracies before assignment of the measurement time quality value required for IEEE Std C37.118.2-2011 [B8].

The time quality fields provided by IEEE Std C37.118.2-2011 [B8] are a 4-bit (MSG\_TQ) and a 3-bit (PMU\_ TQ) field. The mappings from the IEEE C37.238 totalTimeInaccuracy are shown in Table C.2.

The message flag field provided by IEEE Std C37.118.2-2011 [B8] additionally provides the mechanism required to differentiate records with identical time stamps (an artifact from the use of UTC time); the IEEE C37.238 flagField[9:8] bits (leap59 and leap61) provide the information needed for this.

Table C.2-Inaccuracy mapping between IEEE Std C37.238 and IEEE C37.118.1 and IEEE C37.118.2 fields

| IEEE C37.238 totalTimeInaccuracy,                                                                        | IEEE C37.118.2 MSG_TQfield IEEE C37.118.1 IRIG-B TQfield   | IEEE C37.118.2 PMU_TQfield IEEE C37.118.1 IRIG-B CTQfield   |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------|
| If FFFFFFFF hex (unknown, or > ~4s) else use below                                                       | 15                                                         | 7                                                           |
| IfTAI-UTC offset 'unknown' (currentUtcOffsetValid flag= 0) (e.g., due to expiry of last IERS bulletin-C) | 11 (for 1 s to >10 s) else use below                       | 7 else use below                                            |
| If clock is 'locked' (clockClass= 6)                                                                     | 0 else use below                                           | ignore (use below)                                          |
| 100 000 001 to 1 000 000 000                                                                             | 10                                                         | 7                                                           |
| 10 000 001 to 100 000 000                                                                                | 9                                                          | 7                                                           |
| 1 000 001 to 10 000 000                                                                                  | 8                                                          | 6                                                           |
| 100 001 to 1 000 000                                                                                     | 7                                                          | 5                                                           |
| 10 001 to 100 000                                                                                        | 6                                                          | 4                                                           |
| 1001 to 10 000                                                                                           | 5                                                          | 3                                                           |
| 101 to 1000                                                                                              | 4                                                          | 2                                                           |
| 11 to 100                                                                                                | 3                                                          | 1                                                           |
| 1 to 10                                                                                                  | 2                                                          | 1                                                           |
| 0                                                                                                        | 1                                                          | 1                                                           |

## C.4  Use of IEEE Std C37.238 for IRIG-B time-distribution applications

Whereas IEEE Std C37.118.2-2011 [B8] specifies the fields to accompany the Syncrophasor data (as described above), IEEE Std C37.118.1-2011 [B7] suggests how the information needed can be provided using some of the unreserved 'control' bits in IRIG-B frames. (IRIG-B is a time-distribution technology in common use in many substations.)

Limitations of the IRIG-B as currently implemented (per IEEE Std C37.118) comprise the very coarse TQ and continuous time quality (CTQ) granularities (order of magnitude steps), and the inability for an IED to derive the International Atomic Time (TAI) timescale timestamps arguably expected to be used in forthcoming IEDs. To overcome these limitations, plus providing an ID of the time source (useful during holdover events), the draft standard IEEE PC37.237™ [B9] (for time stamping data) includes a repurposing of the IRIG-B's Straight Binary Seconds (SBS) field (whose information is redundant) to provide the following IEEE C37.238:

- -totalTimeInaccuracy (same 32-bit field)
- -currentUtcOffset [TAI-UTC seconds used (so TAI can always be derived correctly)]
- -grandmasterID (same 16-bit field)

The  extensive  installed  base  of  IRIG-sourced  IEDs,  with  the  traditional  10+  years  of  expected  usage, implies an expectation that the transition of time-distribution networks from IRIG-B to IEEE C37.238 will be  accompanied  by  IEEE  C37.238  to  IRIG-B  translation  boxes;  the  following  is  intended  to  clarify  the translations needed.

## C.4.1  Generation of UTC and local-timescale IRIG outputs (IEEE C37.118.1 format)

IEEE C37.238 messages can be used to generate local-timescale IRIG-B outputs using the following steps:

- -Set the seconds, minutes, hours, days, and years fields to the desired time (UTC or local). UTC time is the received PTP time, less the IEEE C37.238 Announce message's currentUtcOffset field. The local time is the PTP time with an offset for the local time zone, and optionally a change for Daylight Saving Time (DST).
- -Set the LSP (Leap Second Pending) bit during the last minute of an event month (when leap59 or leap61 is set).
- -Set the LS (Leap Second direction) bit to flag a leap-second deletion (i.e., when leap59 is set).
- -Set the DSP (Daylight Savings Pending) bit during the last minute before a DST event (0 for UTC time). (This can be derived from the sign of the alternative time offset indicator's (ATOI's) jumpSeconds field, as described in Annex D.)
- -Set the DST (in effect) bit whilst DST is in effect (0 for UTC time).
- -Set the Time Offset to the number of half hours that the local time is currently ahead of UTC (so -16 for Pacific Standard Time (PST), -14 for Pacific Daylight Saving Time (PDST), and 0 for UTC time).
- -Set the TQ field to 0 (for locked to a traceable source) when clockClass=6, else set the TQ field using the IEEE\_C37\_238 TLV's totalTimeInaccuracy, per Table C.2.
- -Also set the CTQ (Continuous Time Quality) field for the IEEE\_C37\_238 TLV's totalTimeInaccuracy, per Table C.2.

## C.4.2  Generation of additional IRIG fields using IEEE C37.237 format

For the enhancements specified in IEEE PC37.237 [B9] (repurposing the IRIG-B's SBS field):

- -Set the 32-bit 'PTQ' field to the IEEE\_C37\_238 TLV's totalTimeInaccuracy
- -Set the 'offset-valid' flag to the Announce message's currentOffsetValid flag
- -Set the 14-bit 'offset' field to the to the Announce message's currentUtcOffset 14-lsb (+36 s in 2016)
- -Set the 16-bit 'Source-ID' field to the IEEE\_C37\_238 TLV's grandmasterID

## Annex D

(informative)

## Use of IEEE C37.238 messages for end devices (IRIG-B replacement)

This annex describes how end devices (slave-only clocks) can use the IEEE C37.238 message bytes.

This suggestion does not provide automatic compensation for the cable delay to the destination IED with a slave-only clock as this is normally negligible, being only approximately 5 ns/m and, if desired, could be compensated in a manner similar to the compensation for the cable delay to GPS antennae (a configurable delay-correction field). The non-negligible delays introduced by the network bridges are compensated.

NOTE 1-For the most reliable functionality, if an end device does not receive the expected type, length, and values (TLVs) in the expected order, it should continue to function as well as possible with the information it does receive (and it may raise an appropriate alert).

NOTE 2-For this annex, the position of a byte in a frame is designated by the integer B n , with n starting at 0 for the byte after the frame's EtherType field. See D.4 for their official names, and their description in the relevant standard.

## D.1  Use of received IEEE C37.238 Sync and Follow\_Up messages to obtain a Precision Time Protocol (PTP) time

Detect IEEE C37.238 Sync messages by checking the following four fields:

- -A Destination media access control (MAC) Address of 01-1B-19-00-00-00
- -An EtherType field of 88F7 16
- -B0 = 0 16 (identifier for IEEE C37.238 Sync messages)
- -B4 = 254 (identifier for the extended profile specified in this standard)

If the message's twoStepFlag B 6 [1] = 0, the PTP Timestamp (the time when the one-step IEEE C37.238 Sync message entered the cable, as the number of seconds since the start of 1970, International Atomic Time [TAI]) comprises the sum of the following three fields.

In the IEEE C37.238 Sync message:

- -The 48-bit unsigned-integer B 34 through B 39 (48-bit seconds of the originTimestamp)
- -The 32-bit unsigned-integer B 40 through B 43 (32-bit nanoseconds field of the originTimestamp)
- -The 64-bit signed-integer B 8 through B 15 (correctionField in 2 -16 ns)

If the message's twoStepFlag B 6 [1] = 1, the PTP Timestamp (the time when the two-step IEEE C37.238 Sync message entered the cable, as the number of seconds since the start of 1970, TAI) comprises the sum of the following four fields.

In the IEEE C37.238 Sync message:

- -64-bit correctionField B 8 through B 15 (first correctionField in 2 -16 ns)

In the IEEE C37.238 Follow\_Up message (same bytes except B 0 = 08 16 ):

- -The 48-bit unsigned-integer B 34 through B 39 (48-bit seconds field of the originTimestamp)
- -The 32-bit unsigned-integer B 40 through B 43 (32-bit nanoseconds field of the originTimestamp)
- -The 64-bit signed-integer B 8 through B 15 (second correctionField in 2 -16 ns)

## D.2  Use of received IEEE C37.238 Announce messages to determine Coordinated Universal Time (UTC) time and local time

NOTEEach  IEEE  C37.238  Announce  message  is  suffixed  by  an  IEEE\_C37\_238  TLV  (for  grandmaster  ID  and TimeInaccuracy) and (optionally) followed by an ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV (for local time).

Detect IEEE C37.238 Announce messages by checking the following fields:

- -A Destination MAC Address of 01 - 1B - 19 - 00 - 00 - 00
- -An EtherType field of 88F7 16
- -B0 = 0B 16 (identifier for IEEE C37.238 Announce messages)
- -B4 =  254 (identifier for the profile that extends the capabilities of IEC/IEEE 61850-9-3 profile, specified in this standard)

And to check for the presence of a ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV suffix:

- -B86 through B 87 = 0009 16 (TLV Type for ALTERNATE\_TIME\_OFFSET\_INDICATOR TLV)

Also check that the frame's currentUtcOffsetValid flag B7[2] is set (equal to 1 for 'TRUE').

## D.2.1  Determining UTC time

The  frame's  currentUtcOffset  bytes  B 44 B45 have  the  number  of  seconds  to  be  subtracted  (from  the  PTP Timestamp) to get UTC time.

## D.2.2  Determining future leap-second adjustments to UTC time

If the frame's byte B 7 [0] is set, the last minute of the current UTC day will have 61 s.

If the frame's byte B 7 [1] is set, the last minute of the current UTC day will have 59 s.

## D.2.3  Determining local time

If the frame's keyField B 90 = 0, the local time offset is unknown; otherwise:

The frame's signed 32-bit (seconds) field currentOffset, comprising bytes B 91 through B 94 , is the number of seconds to be added (to the PTP Timestamp) to get the local time.

NOTEFor compatibility with IEEE Std C37.238-2011 implementations using an offset from UTC, it is suggested that the received currentOffset number be replaced by the closest Nx900, with N being an integer.

## D.2.4  Determining local time through DST events

The frame's jumpSeconds field, comprising bytes B 95 through B 98 , with the frame's timeOfNextJump field, comprising bytes B 99 through B 104 , provide an advance indication of the PTP time for the next DST event.

NOTESince this standard requires these fields to always indicate the next DST event, the sign of the jumpSeconds field always indicates if DST is active (if negative) or inactive (if positive). Caveat: this information is interrupted for up to 13 s prior to a leap second event.

## D.3  Use of received IEEE C37.238 Announce messages (with TLVs) to determine the time's quality

Slave-only clocks require a given time quality for their application functions as well as traceability to a recognized standard time source. They also may need to report these parameters in an application specific format.

## D.3.1  Time traceability

To determine traceability of received time, the slave-only clock should

- -Check that the frame's B 7 [3] bit is set (denotes timescale is PTP)
- -Check that the frame's B 7 [4] bit is set (denotes that time is traceable to a recognized standard time source)

## D.3.2  Time inaccuracy

The totalTimeInaccuracy provides an estimate of the worst-case error, in nanoseconds, of the time being provided; this is the sum of the time source's uncertainty (to UTC), the grandmaster clock's uncertainty, and the uncertainties of all the other (e.g., transparent) clocks transporting the messages.

B80 through B 83 = the totalTimeInaccuracy (in nanoseconds)

## D.3.3  Determining the grandmaster clock sourcing the time

The  grandmasterID  field  B74  through  B75  identifies  the  grandmaster  clock  source  with  a  16-bit  userconfigurable value. This allows IEDs receiving time-stamped data from different source to determine if the time-sources used are the same (useful when the time sources may be in a holdover mode (e.g., due to a solar flare causing loss of GPS).

The grandmasterIdentity field B 53 through B 60 (aka clockIdentity ) also identifies the grandmaster clock source, but with a 64-bit value automatically derived from the device's MAC address. Both fields have the same purpose, but have different benefits and limitations.

## D.4  References for B n

Bytes (aka octets) in Sync Messages

| Position in message,B n   | Field name        | Additional details             |
|---------------------------|-------------------|--------------------------------|
| B 0 [7:4]                 | transportSpecific | 13.3.2.1 of IEEE Std 1588-2008 |
| B 0 [3:0]                 | messageType       | 13.3.2.2 of IEEE Std 1588-2008 |

| Position in message,B n   | Field name                                 | Additional details             |
|---------------------------|--------------------------------------------|--------------------------------|
| B 4                       | domainNumber                               | 13.3.2.5 of IEEE Std 1588-2008 |
| B 6                       | flagField (1 st octet) Bit[1]= twoStepFlag | 13.3.2.6 of IEEE Std 1588-2008 |
| B 8 throughB 15           | correctionField                            | 13.3.2.7 of IEEE Std 1588-2008 |
| B 34 throughB 43          | originTimestamp                            | 13.6.2.1 of IEEE Std 1588-2008 |

Bytes (aka octets) in Follow\_up Messages

| B n                 | Field name                    | Additional details                                            |
|---------------------|-------------------------------|---------------------------------------------------------------|
| B 0 [7:4] B 0 [3:0] | transportSpecific messageType | 13.3.2.1 of IEEE Std 1588-2008 13.3.2.2 of IEEE Std 1588-2008 |
| B 8 throughB 15     | correctionField               | 13.3.2.7 of IEEE Std 1588-2008                                |
| B 34 throughB 43    | preciseOriginTimestamp        | 13.7.2.1 of IEEE Std 1588-2008                                |

Bytes (aka octets) in Announce Messages

| B n                 | Field name                                                                                                                    | Additional details                                            |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| B 0 [7:4] B 0 [3:0] | transportSpecific messageType                                                                                                 | 13.3.2.1 of IEEE Std 1588-2008 13.3.2.2 of IEEE Std 1588-2008 |
| B 4                 | domainNumber                                                                                                                  | 13.3.2.5 of IEEE Std 1588-2008                                |
| B 7                 | flagField (2 nd octet) Bit[0]= leap61 Bit[1]= leap59 Bit[2]= currentUtcOffsetValid Bit[3]= ptpTimescale Bit[4]= timeTraceable | 13.3.2.6 of IEEE Std 1588-2008                                |
| B 44 B 45           | currentUtcOffset                                                                                                              | 13.5.2.2 of IEEE Std 1588-2008                                |
| B 53 throughB 60    | grandmasterIdentity                                                                                                           | 13.5.2.6 of IEEE Std 1588-2008                                |
| B 74 throughB 75    | grandmasterID                                                                                                                 | 6.2.2                                                         |
| B 80 throughB 83    | totalTimeInaccuracy                                                                                                           | 6.2.2                                                         |
| B 90                | ATOI's keyField                                                                                                               | 16.3.3 of IEEE Std 1588-2008                                  |
| B 91 throughB 94    | ATOI's currentOffset                                                                                                          | 16.3.3 of IEEE Std 1588-2008                                  |
| B 95 throughB 98    | ATOI's jumpSeconds                                                                                                            | 16.3.3 of IEEE Std 1588-2008                                  |
| B 99 throughB 104   | ATOI's timeOfNextJump                                                                                                         | 16.3.3 of IEEE Std 1588-2008                                  |

## Annex E

(informative)

## Mixed profile operation

Note that networks supporting a plurality of IEEE 1588 profiles (e.g., IEEE Std 802.1AS, ITU Telecom) isolate them by using different domains (or different VLANs); however there are exceptions to be considered.

## E.1  Using IEC/IEEE 61850-9-3 slave devices

Because an IEC/IEEE 61850-9-3 slave device can be configured to use the domain 254, it can operate in an IEEE C37.238 network in the same manner as in an IEC/IEEE 61850-9-3 network.

Precision Time Protocol (PTP) traffic originating in a IEEE C37.238-compliant grandmaster passes through IEEE  C37.238-compliant  boundary  clocks  (BCs)  and  transparent  clocks  (TCs),  with  the  IEEE  C37.238 applications receiving the required information.

IEC/IEEE 61850-9-3 devices will also receive the IEEE\_C37\_238 type, length, and values (TLVs), but they will ignore them (per 14.1 of IEEE Std 1588-2008), seeing the IEEE C37.238 GM, BCs and TCs as though they were IEC/IEEE 61850-9-3 devices. Because IEEE C37.238 devices must also satisfy all requirements of IEC/IEEE 61850-9-3:2016, the IEC/IEEE 61850-9-3 applications will receive the performance they require.

NOTEThe specification in 6.2.2 provides ATOI TLVs (in IEEE C37.238 Announce messages) that are compliant to the IEEE 1588 ATOI TLV specification, when using the clarifications 17 that were supplied to the IEEE PSRC Working Group H24/SubC7 by the IEEE 1588 Maintenance Working Group.

## E.2  Using other-profile Master clocks

The IEEE C37.238 power profile shares many common features with the default peer-to-peer profile defined in J.4 of IEEE Std 1588-2008. While it is possible (by configuring its domain number) for an IEEE C37.238 slave clock to synchronize to an IEEE 1588 J.4 grandmaster or use IEEE 1588 J.4 transparent clocks, this is not recommended as performance cannot be guaranteed because J.4 of IEEE Std 1588-2008 does not specify performance requirements.

If such a hybrid or mixed-mode system is used, then it is the responsibility of the system integrator or designer to ensure that there are no interoperability issues, and that performance requirements are met. Some means to supply slave devices with the information contained in the TLV (see 6.2) should be provided if required by the application, but in this case no monitoring of degradation of clock performance is possible.

For compatibility with IEEE C37.238-2011 devices, see Annex B.

17 See footnotes 8 and 9.

## Annex F

(normative)

## IEEE C37.238 PICS

The manufacturer shall list the capabilities and options supported by its clock in the PICS according to Table F.1. Based upon the declaration in F.1 ,  the manufacture shall then fill in the appropriate tables (see Table F.2 through Table F.5). This PICS includes the information from the IEC/IEEE 61850-9-3 PICS, labelled as 'Base,' and is extended by IEEE C37.238, labelled as 'F/S'.

## F.1  Conventions

The 'Base' column reflects the definitions and specifications in the base standard. For the purpose of this clause, the Base column refers to IEC/IEEE 61850-9-3:2016. The Functional Specification (F/S) column refers to IEEE Std C37.238.

Each entry in the Base or F/S column contains an entry from the following list:

- -Mandatory (m): The base standard mandates this capability and it is implemented.
- -Optional (o): The base standard leaves this capability optional, but it is implemented.
- -Excluded (x): Indicates that the standard expressly states that it shall not be implemented.
- -Out-of-scope (i): Indicates that the specification is mute on the entry.
- -Numerical specifications for parameters that require such specification.
- -Conditional entries where constraints need to be applied.

For  conditional  entries,  where  there  are  declaration  dependencies,  the  conditions  are  annotated  with  the explanation at the bottom of the table.

The 'Support' column shall be filled by the manufacturer. The support column shall contain the word 'True' if support is declared and a number is not required for PICS declaration. If the PICS declaration requirement requires a numeric value, the value shall be entered instead of 'True.' Declaration of 'Support' shall indicate that the feature is implemented.

## F.2  PICS

Table F.1-PICS

| PICS proforma reference   | Capability                                               | Base                            | F/S                             | Support                         |
|---------------------------|----------------------------------------------------------|---------------------------------|---------------------------------|---------------------------------|
| CLOCK_TYPE_OC             | Clock is OCaccording to this base                        | AtLeastOne(1)                   | AtLeastOne(1)                   |                                 |
| CLOCK_TYPE_TC             | Clock is TCaccording to this base                        | AtLeastOne(1)                   | AtLeastOne(1)                   |                                 |
| CLOCK_TYPE_BC             | Clock is BCaccording to this base                        | AtLeastOne(1)                   | AtLeastOne(1)                   |                                 |
| SLAVE_ONLY                | Clock is ordinary clock that is not grand master capable | AtLeastOne(1)                   | AtLeastOne(1)                   |                                 |
| REDBOX_DATC               | Red Box isTC                                             | AtLeastOne(1)                   | AtLeastOne(1)                   |                                 |
| REDBOX_DABC               | Red Box isBC                                             | AtLeastOne(1)                   | AtLeastOne(1)                   |                                 |
| AtLeastOne(1):            | at least one shall be supported                          | at least one shall be supported | at least one shall be supported | at least one shall be supported |

## Table F.2-PICS for master capable ordinary clock

| PICS proforma reference                                                                                                 | Capability                                                                                                                                                                                           | Base                                                                                                                    | F/S                                                                                                                     | Support                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| NR_PORTS                                                                                                                | Number of clock ports (total)                                                                                                                                                                        | integer > 0                                                                                                             | 1                                                                                                                       | 1                                                                                                                       |
| PORTS_STEP.1                                                                                                            | All ports support 1-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                              | OnlyOne(1)                                                                                                              |                                                                                                                         |
| PORTS_STEP.2                                                                                                            | All ports support 2-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                              | OnlyOne(1)                                                                                                              |                                                                                                                         |
| PORTS_STEP.3                                                                                                            | All ports support both 1-step and 2 on egress                                                                                                                                                        | OnlyOne(1)                                                                                                              | OnlyOne(1)                                                                                                              |                                                                                                                         |
| TIME_TRACEABLE                                                                                                          | Connectable to a time reference outside of PTP(e.g., GPS)                                                                                                                                            | o                                                                                                                       | m                                                                                                                       |                                                                                                                         |
| FREQ_ TRACEABLE                                                                                                         | Connectable to a frequency reference outside of PTP(e.g., GPS)                                                                                                                                       | o                                                                                                                       | m                                                                                                                       |                                                                                                                         |
| ATOI                                                                                                                    | SupportsATOITLVas specified in IEC 61588:2009 ¦ IEEE Std 1588-2008, 16.3                                                                                                                             | o                                                                                                                       | m                                                                                                                       |                                                                                                                         |
| PPS                                                                                                                     | Clock has a 1 PPS output                                                                                                                                                                             | o                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| ACCURACY                                                                                                                | Design value of clockAccuracy. Specify in nanoseconds.                                                                                                                                               | o                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| DEVIATION                                                                                                               | Design value ofAllan deviation. Specify in nanoseconds.                                                                                                                                              | o                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| HOLDOVER                                                                                                                | The length of time the clock is expected to stay in clockClass 7, if it is the grandmaster and no longer synchronized to its time reference signal. The length of time shall be provided in seconds. | o                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| 238_TLV_GMID                                                                                                            | 238 TLV: gmID                                                                                                                                                                                        | i                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| 238_TLV_TI                                                                                                              | 238 TLV: Total time inaccuracy                                                                                                                                                                       | i                                                                                                                       | m                                                                                                                       |                                                                                                                         |
| PDELAY_SUPPORT                                                                                                          | Pdelay support for slave IEDs                                                                                                                                                                        | i                                                                                                                       | m                                                                                                                       |                                                                                                                         |
| PDELAY_DOMAIN                                                                                                           | Indicates if the implementation accepts a Pdelay_Req with any Domain Number                                                                                                                          | i                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| MASTER_ONLY                                                                                                             | Slave not supported                                                                                                                                                                                  | i                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| MAX_DEVICE_ INACURACY                                                                                                   | Maximum device inaccuracy. Shall be specified in nanoseconds. See 6.3.                                                                                                                               | m                                                                                                                       | m                                                                                                                       |                                                                                                                         |
| Management Information Support                                                                                          | Management Information Support                                                                                                                                                                       |                                                                                                                         |                                                                                                                         |                                                                                                                         |
| MIB_SNMP                                                                                                                | Supports MIBof IEC 62439- 3:2016,AnnexE                                                                                                                                                              | o                                                                                                                       | AtLeastOne(2)                                                                                                           |                                                                                                                         |
| MIB_61850                                                                                                               | Supports IEC TR61859- 90-4 Clock Objects                                                                                                                                                             | o                                                                                                                       | AtLeastOne(2)                                                                                                           |                                                                                                                         |
| MIB_OTHER                                                                                                               | Clock supports fixed values or a mechanism defined by the manufacturer (if True, this list is appended to this PICS)                                                                                 | o                                                                                                                       | AtLeastOne(2)                                                                                                           |                                                                                                                         |
| IEC 62439-3 Support                                                                                                     | IEC 62439-3 Support                                                                                                                                                                                  |                                                                                                                         |                                                                                                                         |                                                                                                                         |
| DAC                                                                                                                     | Doubly attached                                                                                                                                                                                      | o                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| PORTS_PAIRED                                                                                                            | Paired clock ports for redundancy (e.g., {3-4}). Must specify the list of paired ports.                                                                                                              | o                                                                                                                       | o                                                                                                                       |                                                                                                                         |
| OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented                                                                              | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented |

## Table F.3-PICS for BC

| PICS proforma reference                                                                                                  | Capability                                                                                                                                                                                           | Base                                                                                                                     | F/S                                                                                                                      | Support                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| NR_PORTS                                                                                                                 | Number of clock ports (total)                                                                                                                                                                        | integer >0                                                                                                               | integer >=2                                                                                                              |                                                                                                                          |
| PORTS_STEP.1                                                                                                             | All ports support 1-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| PORTS_STEP.2                                                                                                             | All ports support 2-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| PORTS_STEP.3                                                                                                             | All ports support both 1-step and 2 on egress                                                                                                                                                        | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| TIME_TRACEABLE                                                                                                           | Connectable to a time reference outside of PTP(e.g., GPS)                                                                                                                                            | o                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| FREQ_ TRACEABLE                                                                                                          | Connectable to a frequency reference outside of PTP(e.g., GPS)                                                                                                                                       | o                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| ATOI                                                                                                                     | SupportsATOITLVas specified in IEC 61588:2009 ¦ IEEE Std 1588-2008, 16.3                                                                                                                             | o                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| PPS                                                                                                                      | Clock has a 1 PPS output                                                                                                                                                                             | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| ACCURACY                                                                                                                 | Design value of clockAccuracy. Specify in nanoseconds.                                                                                                                                               | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| DEVIATION                                                                                                                | Design value ofAllan deviation. Specify in nanoseconds.                                                                                                                                              | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| HOLDOVER                                                                                                                 | The length of time the clock is expected to stay in clockClass 7, if it is the grandmaster and no longer synchronized to its time reference signal. The length of time shall be provided in seconds. | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| 238_TLV_GMID                                                                                                             | 238 TLV: gmID                                                                                                                                                                                        | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| 238_TLV_TI                                                                                                               | 238 TLV: Total time inaccuracy                                                                                                                                                                       | i                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| PDELAY_SUPPORT                                                                                                           | PDelay support for slave IEDs                                                                                                                                                                        | i                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| PDELAY_DOMAIN                                                                                                            | Indicates if the implementation accepts a Pdelay_Req with any Domain Number                                                                                                                          | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| MASTER_ONLY                                                                                                              | Slave not supported                                                                                                                                                                                  | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| MAX_DEVICE_ INACURACY                                                                                                    | Maximum device inaccuracy. Shall be specified in nanoseconds. See 6.3.                                                                                                                               | m                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| Management Information Support                                                                                           | Management Information Support                                                                                                                                                                       |                                                                                                                          |                                                                                                                          |                                                                                                                          |
| MIB_SNMP                                                                                                                 | Supports MIBof IEC 62439- 3:2016,AnnexE                                                                                                                                                              | o                                                                                                                        | AtLeastOne(2)                                                                                                            |                                                                                                                          |
| MIB_61850                                                                                                                | Supports IEC TR61859- 90-4 Clock Objects                                                                                                                                                             | o                                                                                                                        | AtLeastOne(2)                                                                                                            |                                                                                                                          |
| MIB_OTHER                                                                                                                | Clock supports fixed values or a mechanism defined by the manufacturer (if True, this list is appended to this PICS)                                                                                 | o                                                                                                                        | AtLeastOne(2)                                                                                                            |                                                                                                                          |
| IEC 62439-3 Support                                                                                                      | IEC 62439-3 Support                                                                                                                                                                                  |                                                                                                                          |                                                                                                                          |                                                                                                                          |
| DAC                                                                                                                      | Doubly attached                                                                                                                                                                                      | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| PORTS_PAIRED                                                                                                             | Paired clock ports for redundancy (e.g., {3-4}). Must specify the list of paired ports.                                                                                                              | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented.                                                                             | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. |

## Table F.4-PICS for TC

| PICS proforma reference                                                                                                  | Capability                                                                                                                                                                                           | Base                                                                                                                     | F/S                                                                                                                      | Support                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| NR_PORTS                                                                                                                 | Number of clock ports (total)                                                                                                                                                                        | integer > 0                                                                                                              | integer >= 2                                                                                                             |                                                                                                                          |
| PORTS_STEP.1                                                                                                             | All ports support 1-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| PORTS_STEP.2                                                                                                             | All ports support 2-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| PORTS_STEP.3                                                                                                             | All ports support both 1-step and 2 on egress                                                                                                                                                        | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| TIME_TRACEABLE                                                                                                           | Connectable to a time reference outside of PTP(e.g., GPS)                                                                                                                                            | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| FREQ_ TRACEABLE                                                                                                          | Connectable to a frequency reference outside of PTP(e.g., GPS)                                                                                                                                       | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| ATOI                                                                                                                     | SupportsATOITLVas specified in IEC 61588:2009 ¦ IEEE Std 1588-2008, 16.3                                                                                                                             | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| PPS                                                                                                                      | Clock has a 1 PPS output                                                                                                                                                                             | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| ACCURACY                                                                                                                 | Design value of clockAccuracy. Specify in nanoseconds.                                                                                                                                               | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| DEVIATION                                                                                                                | Design value ofAllan deviation. Specify in nanoseconds.                                                                                                                                              | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| HOLDOVER                                                                                                                 | The length of time the clock is expected to stay in clockClass 7, if it is the grandmaster and no longer synchronized to its time reference signal. The length of time shall be provided in seconds. | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| 238_TLV_GMID                                                                                                             | 238 TLV: gmID                                                                                                                                                                                        | i                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| 238_TLV_TI                                                                                                               | 238 TLV: Total time inaccuracy                                                                                                                                                                       | i                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| PDELAY_SUPPORT                                                                                                           | Pdelay support for slave IEDs                                                                                                                                                                        | i                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| PDELAY_DOMAIN                                                                                                            | Indicates if the implementation accepts a Pdelay_Req with any Domain Number                                                                                                                          | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| MAX_DEVICE_ INACURACY                                                                                                    | Maximum device inaccuracy. Shall be specified in nanoseconds. See 6.3.                                                                                                                               | m                                                                                                                        | m                                                                                                                        |                                                                                                                          |
| Management Information Support                                                                                           | Management Information Support                                                                                                                                                                       |                                                                                                                          |                                                                                                                          |                                                                                                                          |
| MIB_SNMP                                                                                                                 | Supports MIBof IEC 62439- 3:2016,AnnexE                                                                                                                                                              | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| MIB_61850                                                                                                                | Supports IEC TR61859- 90-4 Clock Objects                                                                                                                                                             | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| MIB_OTHER                                                                                                                | Clock supports fixed values or a mechanism defined by the manufacturer (if True, this list is appended to this PICS)                                                                                 | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| IEC 62439-3 Support                                                                                                      | IEC 62439-3 Support                                                                                                                                                                                  |                                                                                                                          |                                                                                                                          |                                                                                                                          |
| DAC                                                                                                                      | Doubly attached                                                                                                                                                                                      | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| PORTS_PAIRED                                                                                                             | Paired clock ports for redundancy (e.g., {3-4}). Must specify the list of paired ports.                                                                                                              | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented.                                                                             | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. |

## Table F.5-PICS for Slave Only Ordinary Clock (SLAVE)

| PICS proforma reference                                                                                                  | Capability                                                                                                                                                                                           | Base                                                                                                                     | F/S                                                                                                                      | Support                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| NR_PORTS                                                                                                                 | Number of clock ports (total)                                                                                                                                                                        | integer > 0                                                                                                              | 1                                                                                                                        | 1                                                                                                                        |
| PORTS_STEP.1                                                                                                             | All ports support 1-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| PORTS_STEP.2                                                                                                             | All ports support 2-step on egress                                                                                                                                                                   | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| PORTS_STEP.3                                                                                                             | All ports support both 1-step and 2 on egress                                                                                                                                                        | OnlyOne(1)                                                                                                               | OnlyOne(1)                                                                                                               |                                                                                                                          |
| TIME_TRACEABLE                                                                                                           | Connectable to a time reference outside of PTP(e.g., GPS)                                                                                                                                            | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| FREQ_ TRACEABLE                                                                                                          | Connectable to a frequency reference outside of PTP(e.g., GPS)                                                                                                                                       | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| ATOI                                                                                                                     | SupportsATOITLVas specified in IEC 61588:2009 ¦ IEEE Std 1588-2008, 16.3                                                                                                                             | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| PPS                                                                                                                      | Clock has a 1 PPS output                                                                                                                                                                             | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| ACCURACY                                                                                                                 | Design value of clockAccuracy. Specify in nanoseconds.                                                                                                                                               | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| DEVIATION                                                                                                                | Design value ofAllan deviation. Specify in nanoseconds.                                                                                                                                              | o                                                                                                                        | i                                                                                                                        |                                                                                                                          |
| HOLDOVER                                                                                                                 | The length of time the clock is expected to stay in clockClass 7, if it is the grandmaster and no longer synchronized to its time reference signal. The length of time shall be provided in seconds. | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| 238_TLV_GMID                                                                                                             | 238 TLV: gmID                                                                                                                                                                                        | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| 238_TLV_TI                                                                                                               | 238 TLV: Total time inaccuracy                                                                                                                                                                       | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| PDELAY_SUPPORT                                                                                                           | Pdelay support for slave IEDs                                                                                                                                                                        | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| PDELAY_DOMAIN                                                                                                            | Indicates if the implementation accepts a Pdelay_Req with any Domain Number                                                                                                                          | i                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| Management Information Support                                                                                           | Management Information Support                                                                                                                                                                       | Management Information Support                                                                                           | Management Information Support                                                                                           | Management Information Support                                                                                           |
| MIB_SNMP                                                                                                                 | Supports MIBof IEC 62439- 3:2016,AnnexE                                                                                                                                                              | o                                                                                                                        | AtLeastOne(2)                                                                                                            |                                                                                                                          |
| MIB_61850                                                                                                                | Supports IEC TR61859- 90-4 Clock Objects                                                                                                                                                             | o                                                                                                                        | AtLeastOne(2)                                                                                                            |                                                                                                                          |
| MIB_OTHER                                                                                                                | Clock supports fixed values or a mechanism defined by the manufacturer (if True, this list is appended to this PICS)                                                                                 | o                                                                                                                        | AtLeastOne(2)                                                                                                            |                                                                                                                          |
| IEC 62439-3 Support                                                                                                      | IEC 62439-3 Support                                                                                                                                                                                  | IEC 62439-3 Support                                                                                                      | IEC 62439-3 Support                                                                                                      | IEC 62439-3 Support                                                                                                      |
| DAC                                                                                                                      | Doubly attached                                                                                                                                                                                      | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| PORTS_PAIRED                                                                                                             | Paired clock ports for redundancy (e.g., {3-4}). Must specify the list of paired ports.                                                                                                              | o                                                                                                                        | o                                                                                                                        |                                                                                                                          |
| OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented.                                                                             | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. | OnlyOne(1) only one shall be supported.At least one shall be supported. AtLeastOne(2) at least one shall be implemented. |

## Table F.6-PICS for Red Box as Transparent (REDBOX\_DATC)

| PICS proforma reference                  | Capability                               | Base                                     | F/S                                      | Support                                  |
|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| Must declare TCCapabilities in Table F.4 | Must declare TCCapabilities in Table F.4 | Must declare TCCapabilities in Table F.4 | Must declare TCCapabilities in Table F.4 | Must declare TCCapabilities in Table F.4 |
| REDBOX_SLTC                              | Redbox as StatelessTC                    | o                                        | o                                        |                                          |

## Table F.7-PICS for Red Box as BC (REDBOX\_DABC)

| PICS proforma reference                               | Capability                                            | Base                                                  | F/S                                                   | Support                                               |
|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Must declare Boundary Clock Capabilities in Table F.3 | Must declare Boundary Clock Capabilities in Table F.3 | Must declare Boundary Clock Capabilities in Table F.3 | Must declare Boundary Clock Capabilities in Table F.3 | Must declare Boundary Clock Capabilities in Table F.3 |
| REDBOX_TWBC                                           | Redbox as three-wayBC                                 | o                                                     | o                                                     |                                                       |

## Annex G

(informative)

## Bibliography

Bibliographical  references  are  resources  that  provide  additional  or  helpful  material  but  do  not  need  to  be understood or used to implement this standard. Reference to these resources is made for informational use only.

[B1] IEC 61850-5:2013, Ed. 2.0, Communication networks and systems for power utility automation-Part 5: Communication requirements for functions and device models. 18

[B2] IEC 61850-7-2:2010, Ed. 2.0, Communication networks and systems for power utility automationPart  7-2:  Basic  communication  structure  for  substation  and  feeder  equipment-Abstract  communication service interface (ACSI).

[B3] IEEE Std 802.1AB™-2009, IEEE Standard for Local and Metropolitan Area Networks-Station and Media Access Control Connectivity Discovery.

[B4] IEEE Std 802.3™-2011, IEEE Standard for LAN/MAN-Specific requirements-Part 3: Carrier Sense Multiple Access with Collision Detection (CSMA/CD) Access Method. 19,20

[B5]  IEEE  Std  1815™-2010,  IEEE  Standard  for  Electric  Power  Systems  Communications-Distributed Network Protocol (DNP3).

[B6] IEEE Std C37.118™-2005, IEEE Standard for Synchrophasors for Power Systems.

[B7] IEEE Std C37.118.1™-2011, IEEE Standard for Synchrophasor Measurements for Power Systems.

[B8] IEEE Std C37.118.2™-2011, IEEE Standard for Synchrophasor Data Transfer for Power Systems.

[B9] IEEE PC37.237™ (Draft 0.6, April 2016), Draft Standard for Requirements for Time Tags Created by Intelligent Electronic Devices-COMTAG™. 21

- [B10] International Vocabulary of Basic and General Terms in Metrology.

[B11] IRIG Standard 200-04, IRIG Serial Time Code Formats; Secretariat, Range Commanders Council, US Army White Sands Missile Range, New Mexico, September 2004. (Available online at: http://  jcs  .mil/  RCC.)

18 IEC publications are available from the International Electrotechnical Commission (http://  www  .iec  .ch/  ) and from the American National Standards Institute (http://  www  .ansi  .org/  ).

19 IEEE publications are available from the Institute of Electrical and Electronics Engineers (http://  standards  .ieee  .org).

20 The IEEE standards or products referred to in Annex G are trademarks owned by the Institute of Electrical and Electronics Engineers, Incorporated.

21 Numbers preceded by P are IEEE authorized standards projects that were not approved by the IEEE-SA Standards Board at the time this publication went to press. For information about obtaining drafts, contact the IEEE (http://  standards  .ieee  .org/  ).

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Connect with us on:

Facebook: https://www.facebook.com/ieeesa

Twitter: @ieeesa

LinkedIn: http://www.linkedin.com/groups/IEEESA-Official-IEEE-Standards-Association-1791118

BLOG IEEE-SA Standards Insight blog: http://standardsinsight.com

You

YouTube:IEEE-SAChannel

Tube

Phone: +1 732 981 0060    Fax: +1 732 562 1571

© IEEE

## Consensus WE BUILD IT.

<!-- image -->