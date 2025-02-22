# backlog

## features

graph-copy

- same nodes
- same edges
- same roots
- modify the original the copy shouldn't change
- modify the copy the origianl shouldn't change

graph-equal

add-node

- should fail on trees

add-node-with-parent

add-edge

- has to do computation on trees

- has to do computation on acyclic

remove-node

- should fail on non-leaf notes for trees

remove-link

make-frozen-copy

- has to do computation for trees

depth

- how do we handle multiple roots

- how do we handle cyclics

descendents (iterable)

- depth first or breadth first

ancestors (iterable)

- depth first or breadth first

step-count-from-to(node, node)

is-tree

is-acyclic

to-s

- should this be guaranteed ordering?

to-repr

- should this be guaranteed ordering?

python style load

load-from-repr

is-empty

- #nodes is zero

is-path

path-from-to

is-in-acycle

- should always be false for trees

various make froms

nodes (iterable)

edges (iterable)

connections (iterable)

## refactoring

better representation

- do we need "finals" at all

- collapse roots, nodes, edges -> dict

- dict should be to-set rather than to-list

make modifiable

## pytest maintenance

don't call make tuple directly

rather than having global constants for sample data, have functions that make them each time

was-modified

make-unique-node-name

@param's

pytest support in vscode

running make in vscode

watch mode

code coverage

## python maintenance

python version -> file

pretty print on save

## git maintance

before commit hook to run the test

## pair programming

https://chatgpt.com/share/67b804b0-5bcc-800e-8d63-cdb2288d3876

### vscode

Pair programming in **VS Code** can be done efficiently using **Live Share**, a built-in extension from Microsoft. Here’s how to set it up and use it:

---

#### **1. Install Live Share Extension**

- Open **VS Code**.
- Go to the **Extensions Marketplace** (`Ctrl + Shift + X`).
- Search for **"Live Share"**.
- Install the **Live Share** extension by Microsoft.

---

#### **2. Sign In & Start a Session**

- After installation, click on the **Live Share** icon in the activity bar (left side).
- Sign in using **GitHub** or **Microsoft** account.
- Click **Start a Collaboration Session**.
- A unique link is generated—share this with your programming partner.

---

#### **3. Join a Live Share Session**

- If you receive a **Live Share link**, open it in a browser.
- It will prompt you to **open VS Code**.
- Click **Join Collaboration Session**.

---

#### **4. Features of Live Share for Pair Programming**

✅ **Real-time Code Sharing** – Both partners can code in the same file simultaneously.  
✅ **Shared Terminals** – Run and view terminal commands together.  
✅ **Voice Chat** – Built-in audio calling without needing external apps.  
✅ **Independent Navigation** – Move across files separately without interrupting each other.  
✅ **Follow Mode** – One user can follow the cursor of the other to stay in sync.

---

#### **5. Debugging Together**

- The **host** can start debugging, and the **guest** can see breakpoints and logs.
- Share debugging sessions, watch variables, and step through code together.

---

#### **6. Stopping the Session**

- Click **Live Share** > **End Session**.
- The guest will be disconnected.

---

### git codspace

Pair programming in **GitHub Codespaces** can be done using **Live Share** in VS Code (since Codespaces is essentially a VS Code environment). Here’s how you and your programming partner can collaborate effectively:

---

#### **1. Start a GitHub Codespace**

1. Go to your **GitHub repository**.
2. Click the **"Code"** button > Select the **"Codespaces"** tab.
3. Click **"Create codespace on main"** (or your desired branch).

Once the Codespace loads, you have a full cloud-based development environment.

---

#### **2. Install Live Share in Codespace**

Since Codespaces runs **VS Code in the browser**, Live Share isn't preinstalled by default. You'll need to install it:

1. Open the **Extensions Marketplace** (`Ctrl + Shift + X`).
2. Search for **Live Share**.
3. Install **Live Share** (by Microsoft).

---

#### **3. Start a Live Share Session**

1. Click on the **Live Share** icon in the activity bar (left side).
2. Sign in using a **GitHub** or **Microsoft** account.
3. Click **"Start a collaboration session"**.
4. Copy the generated **Live Share link** and share it with your pair programming partner.

---

#### **4. Join a Live Share Session in Codespaces**

1. If your partner receives the **Live Share link**, they can open it in a browser.
2. It will prompt them to **open Codespaces in VS Code (web or desktop)**.
3. They click **"Join Collaboration Session"** and can now edit the same files in real-time.

---

#### **5. Pair Programming Features in Codespaces**

✅ **Real-time Code Collaboration** – Both users can edit files together.  
✅ **Shared Terminal Access** – You can run terminal commands and let your partner see them.  
✅ **Shared Servers** – If you run a local server (e.g., a web app), your partner can access it via a shared URL.  
✅ **Debugging Together** – Debug sessions are visible to both users.  
✅ **Follow Mode** – One person can "follow" the other's cursor for guided programming.

---

#### **6. Ending the Session**

- The host can click **"End Session"** to disconnect everyone.
- The guest will automatically lose access.

---

## done

## inbox

do we want to make this a class?

should the type be called `DirectedGraph` rather than `Tree`
