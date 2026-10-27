<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/process-matching/ -->

# Process Matching

The ‘process match’ can be a simple process name, wildcards, or even a [Regular Expression checked against multiple process attributes](https://rulebuilder.bitsum.com), such as the user and command line.

## Traditional

Traditional process name matching uses a simple wildcard match, with ‘?’ indicating any single character and ‘\*’ indicating a sequence of any characters. It is case insensitive. The user name may be appended to the match string with a colon. Depending on the feature, after toggling on path or command line matching, those fields are also compared to the match phrase.

**Examples (non-Regex):**

```
chrome.exe
 Match any process named chrome.exe

chrome*
 Match any process that begins with 'chrome'

chrome.exe:bob
 Match any process named chrome.exe running under user 'bob'
```

## Child Processes (childof:)

To match every process launched by a given application, prefix the parent's process name with `childof:`. All descendants match, not just direct children, so a process started by a child of the parent also matches. The parent name accepts the same wildcards as traditional matching and is case insensitive. Spaces after the colon are ignored.

**Examples:**

```
childof:steam.exe
 Match any process descended from steam.exe, such as games and their helper processes

childof: boinc.exe
 Match any process descended from boinc.exe

childof:epic*.exe
 Match any process descended from a process whose name begins with 'epic'
```

The parent process itself does not match a `childof:` rule; add a separate rule for it if needed. A process is only matched while its parent chain is known: if an intermediate parent exits before Process Lasso sees the child, or the child outlives the parent and rules are re-evaluated, the child no longer matches.

`childof:` is supported by CPU priority, CPU affinity, CPU Sets, I/O priority, memory priority, GPU priority, thread priority boost, Efficiency Mode, Startup Boost, the CPU Limiter, the Instance Balancer, the Watchdog, processor group extension, ProBalance exclusions, and Performance Mode exclusions.

It is **not** supported by Disallowed Processes, instance count limits, GPU adapter preferences, or rules enforced by registry (Enforce by Registry requires a plain process name).

`childof:` can't be combined with a user name. To restrict a child process match by user or other attributes, use a [Regular Expression](process-matching.md#htoc-regular-expressions). Regular Expressions only see the direct parent (the ParentName field), while `childof:` checks every ancestor.

## Regular Expressions

Process Lasso supports Regular Expression (RegEx) matching to multiple process attributes. This allows for the creation of complex rules not otherwise possible. For instance, a rule could act on Chrome.exe or Firefox.exe when user is Bob or Jeremy. Previously, this would require 4 different rules, but using a Regular Expression they can be combined into one.

You can use our [Process Lasso Rule Builder](https://rulebuilder.bitsum.com) to create these rules or continue below to learn to do it manually.

##### What Is a Regular Expression?

A Regular Expression is a language for pattern matching (and substitution). It has been in use for decades and enjoys widespread support.

|  |
| --- |
| A regular expression is a special text string for describing a search pattern. You can think of regular expressions as wildcards on steroids. You are probably familiar with wildcard notations such as \*.txt to find all text files in a file manager. The regex equivalent is .\*.txt. – [RegexBuddy](https://www.regexbuddy.com/regex.html) |

Read more: [Quick Reference](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) (Microsoft) [RegEx101 Tester](https://regex101.com/r/t69lfP/1)

##### Use of RegEx in Process Lasso

When matching a RegEx, Process Lasso concatenates multiple fields about the process. The format of this consolidated process information string is:

```
PID,User,ProcessName,Path,ParentPID,ParentName,,,,CommandLine (always last)
```

PID process ID User user under which process is running Process basename of process Path file path of process image ParentPID parent ID Parent parent process name CommandLine instance command line (this field is always last. Its index is subject to change if new fields are inserted later!) In this way, an expression can match to anything in the concatenated string, or only to specific fields, depending on how precise the expression is. With Process Lasso, Regular Expressions are differentiated from traditional match phrases by *encapsulation in forward slashes* (e.g. ‘/myregex/’). All matching is case insensitive. Embedded commas in a field (normally only in the command line field) are escaped with a backslash, so for precise rules this should be taken into account.

##### Examples

###### Simple

While RegEx allows for powerful matching on multiple patterns and fields, it can also be used in simple ways:

```
/firefox.exe/  
 Match 'firefox?exe' anywhere in any field. Note '.' is a wildcard in RegEx, but you can escape it like 'firefox\.exe' for more precision.  

/,firefox\.exe/  
 Match only firefox.exe at the start of a field (>0)  

/,fire[^,]*\.exe/  
 Match a field (>0) that starts with 'fire' and contains '.exe', such as firefox.exe  

/,(fire|chr)[^,]*\.exe,/  
 Match a field (>0) that starts with 'fire' or 'chr' and ends with '.exe'  

/,app[123]\.exe/  
 Match if any field is app1.exe, app2.exe, or app3.exe (>0)  

/,bobsmith/   
 Match user bobsmith at the start of a field (>0)  

/10280,/  
 Match PID 10280. (simplified form, technically this could match other fields)  

/,.*-type=renderer[^,]*$/  
 Match '-type=renderer' in the last field (command line). No comma may follow it (see the next example for embedded commas).  

/,.*-type=renderer([^,\\]|\\.)*$/  
 Prior with handling of escaped embedded commas (\,) in the command line.
```

###### Advanced

To match specific fields, an expression such as this can be used to match specifically field 3 (the process name):

```
^([^,]*,){2}
 Explanation:
 ^ = Starts at beginning of string
 ([^,]*,) = Not a comma repeated zero or more times, followed by a comma
 {2} = Repeat prior match (a comma delimited field) 2 times
```

```
/^[^,]*,(jeremy|bob),/  
 Match processes with username of jeremy or bob  

/^([^,]*,){2}chrome\.exe,/  
 Match processes named chrome.exe  

/^([^,]*,){2}[^,]*chr[^,]*,/  
 Match processes whose name contains 'chr'  

/^([^,]*,){2}(chrome|firefox)\.exe,/  
 Match processes named chrome.exe or firefox.exe  

/^([^,]*,){5}boinc\.exe,/  
 Match processes that are direct children of boinc.exe (to include all descendants, use childof: instead)  

/^([^,]*,){2}conhost\.exe,([^,]*,){2}boinc\.exe,/  
 Match processes named conhost.exe that are children of boinc.exe  

/^[^,]*,(jeremy|bob),chrome\.exe,/  
 Match processes whose name is chrome.exe under user of jeremy or bob.  

/^([^,]*,){2}chrome\.exe,.*-type=renderer([^,\\]|\\.)*$/  
 Match process name 'chrome.exe' and has '-type=renderer' in the command line (last field)  

/^([^,]*,){3}[^,]*\\program files/  
 Match path containing '\Program Files' (matching is case insensitive).
```

**Writing Your Own**

- Use `[^,]*` rather than `.*` to stay within one field. `.*` runs on into the fields that follow, so `/^([^,]*,){2}.*chr.*,/` would also match a process whose path or parent contains 'chr'.
- Put alternatives in parentheses: `(jeremy|bob)`. Without them, `|` splits the whole expression in two, so `/^([^,]*,)(jeremy)|(bob),/` matches 'bob,' anywhere in the string.
- End a field match with a comma, as in `chrome\.exe,`, so it doesn't also match a longer value such as chrome.exe.old.
- Start and end every phrase with a forward slash. Without the leading slash, the phrase is treated as a traditional wildcard match. The phrase ends at the first forward slash after the opening one, even an escaped one, so write a literal slash as `\x2f`.
- Process Lasso converts the phrase to lowercase before using it. Lowercase escapes such as `\d`, `\s` and `\w` work, but their uppercase forms (`\D`, `\S`, `\W`, `\B`) turn into the lowercase ones; write `[^0-9]` instead of `\D`, and so on.

**How to test Regular Expressions** To test your Regular Expressions, we recommend [this site](https://regex101.com/r/t69lfP/1). We’ve preloaded a sample of what you’d be matching against, again with fields being (also see above):

```
PID,User,Process,Path,ParentPID,Parent,,,,CommandLine (always last)
```

Alternatively, create a text file with row(s) simulating Process Lasso’s provided match string. Then use grep (WSL or Linux) or another tool to match RegEx. Note that the encapsulating forward slashes need to be removed. An example is:

```
sample.txt:
20116,jeremy,chrome.exe,C:\Program Files (x86)\Google\Chrome\Application\chrome.exe,19233,chrome.exe,,,,"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --type=renderer
```

```
test command:  
grep -P 'chr.*' sample.txt
```
