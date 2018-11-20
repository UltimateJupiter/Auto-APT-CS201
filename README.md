# Auto-APT
APT solution violent auto-completer for DUKE CS201 (Java)

### ! Please do not rely on this for all your APTs or you will fail the exam, get a low GPA, be unemployed, have no family, and die alone

##### The current version only takes String[], String, int[], int for input and output, multiple input/output is not supported

1. Visit the APT Info page. You'll see the block containing sample code such as
```java
public class FloodRelief {
    public int minimumPumps(String[] heights){
       // fill in code here
    }
}
```
In this case, fill out the CONFIG file

```txt
CLASS :: FloodRelief
FUNC_NAME :: minimumPumps
INPUT :: String[] heights
RETURN :: int

=========================
int :: return -3131;
int[] :: int[] ret = new int[1232]; return ret;
String :: String ret = "there's no way this is the answer"; return ret;
String[] :: String[] ret = new String[1232]; return ret;
```

2. Run [blank_java.py](https://github.com/UltimateJupiter/Auto-APT/blob/master/blank_java.py) and you'll find a FloodRelief.java in "Fake" folder

3. Submit this code to the platform, it should be all red. Download the page (e.g. APT _floodrelief.html) to "HTMLS" folder, **please do not rename that html file.**

4. Run [fake_gen.py](https://github.com/UltimateJupiter/Auto-APT/blob/master/fake_gen.py), you'll find a FloodRelief.java in "Solution" folder

5. Submit that java class and you'll get all-green
