# Caravan
---
Woah! Cool!<br/>
How does it work?

### Running Caravan
---

To run caravan, simply open it with Python! Something like the following should work:

`py cvn.py`

### Downloading Packages
---

To download a package, type the command `get` followed by the package name in the interface. This will download the package to a new local directory called `caravan`, which stores all the files. To import the package, you can then do
```camel
import("caravan/<mainPackageScript>.camel")
```

### Uploading Packages
---

Uploading packages can be done by first sending all the files related to your package to a `zip` archive. You can then use the `upload` command followed by the archive name (*including the extension! [**.zip, duh!**]*).

After this, you will be prompted for a key. This is like a password for your package. If this is your first time uploading, enter anything, but make it memorable! Whenever you update your package, you'll have to enter the same key as before to verify yourself.

Finally, you'll be met with the dependencies prompt. Simply list off each external package your package depends on, pressing enter after each. Once you're done, or if there are none, enter `|end|`.

Upload complete!

