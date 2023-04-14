# RegexZoo

[![CodeFactor](https://www.codefactor.io/repository/github/k-wu/regexzoo/badge?s=42726d31077e811519a1154a974499049e407d75)](https://www.codefactor.io/repository/github/k-wu/regexzoo)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/23d36dd14441404b98690f4fb835ac8e)](https://app.codacy.com?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)


Reproducing regex from [AutomataZoo](https://github.com/tjt7a/AutomataZoo)。

## Source
* [ClamAV](https://github.com/tjt7a/AutomataZoo/tree/master/ClamAV/code)
* [Brill](https://github.com/tjt7a/AutomataZoo/blob/master/Brill/code/regex.txt)
* [EntityResolution](https://github.com/tjt7a/AutomataZoo/blob/master/EntityResolution/code/name_generator/10000_names.db)
* [Snort](https://github.com/tjt7a/AutomataZoo/blob/master/Snort/benchmarks/automata/snort.regex)
* [Protomata](https://github.com/tjt7a/AutomataZoo/blob/master/Protomata/code/protomata.regex)
* [YARA](https://github.com/tjt7a/AutomataZoo/blob/master/YARA/code/README.md)
### ClamAV
* [Clamwin 0.99.4](https://sourceforge.net/projects/clamwin/files/clamwin/0.99.4/)
* [ClamAV daily-24356.cvd](https://src.fedoraproject.org/repo/pkgs/clamav/daily-24356.cvd)


## Discussion on Cases in Automata Zoo
### (To deprecate) EntityResolution

EntityResolution generates automata from the 10,000 names with fuzzy, using the following pattern.

"<Last Name w/ fuzzy> *, +<First Name w/ fuzzy>"

The fuzzy rule is 1 letter mismatch allowance in each of the laste name and first name substring.

This does not seem a good regex task to me and should better be implemented on GPU using a specific kernel that counts mismatch.

## License
The inputs and rules raw files are from AutomataZoo, ClamAV, and snort. They may be licensed under their own licenses. Please check the corresponding subdirectory or website for licensing information.

Please feel free to raise issue or email us if you feel there is a license infringement.

## Reference
https://github.com/katef/libfsm/
