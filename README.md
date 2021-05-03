# 🏷️ fuuid

FUUID stands for Functional Universally Unique IDentifier. FUUIDs are compatible with regular UUIDs but are naturally ordered by generation time, collision-free and support succinct representations such as raw binary and base58-encoded strings.

In short, running FUUIDs through the UNIX sort command will result in a list ordered by generation time.

# Installation

You can install this package using `pip` or build it from source using `poetry`:

    # Using pip
    pip install fuuid

    # Using poetry
    pip install poetry
    poetry build

# Example

```python
from fuuid import fuuid, fuuid_ns, raw_fuuid, raw_fuuid_ns, b58_fuuid, b58_fuuid_ns, b64_fuuid, b64_fuuid_ns

fuuid()
# UUID('01324332-f66a-054a-76e4-fbdc7f772cd1')

fuuid_ns()
# UUID('00474eaa-b5d8-3844-338c-e77ecd424b06')

raw_fuuid()
# b'\x012C2\xc5\xfc\x18\xca\x96N\xe5_\xaaU86'

raw_fuuid_ns()
# b'\x00GN\xaa\xb5\xd88D\xfb\xfe%\xcf_\x90\xb8\xa8'

b58_fuuid()
# 9ZxgTVssa99BdQF3n5tSj

b58_fuuid_ns()
# 12zi36Vm1zaBQmpmpZ2xXk

b64_fuuid()
# ATJDMhbpQxNUfC7BL3F3kQ==

b64_fuuid_ns()
# AEdOqrXYOES+VjlfTHElKw==
```

# License
```text
BSD 3-Clause License

Copyright (c) 2021, Phil Demetriou
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```