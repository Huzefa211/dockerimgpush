from flask import Flask

app = Flask(__name__)

def normal_function():
    return """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Apache OFBiz – Functional Hierarchy</title>

  <style>
    body {
      font-family: "Segoe UI", Roboto, Arial, sans-serif;
      background: #ffffff;
      color: #022B53;
    }

    .tree ul {
      list-style: none;
      padding-left: 28px;
    }

    .tree li {
      margin: 8px 0;
    }

    .node {
      cursor: pointer;
      padding: 10px 18px;
      border-radius: 14px;
      display: inline-block;
      font-weight: 600;
      transition: all 0.25s ease;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .system {
      background: #022B53;
      color: #ffffff;
    }

    .module {
      background: #0B5C9E;
      color: #ffffff;
    }

    .submodule {
      background: #118AD6;
      color: #ffffff;
    }

    .section {
      background: #6EC1E4;
      color: #022B53;
      font-weight: 700;
    }

    .tab {
      background: #EAF6FC;
      color: #022B53;
      cursor: default;
      margin-left: 10px;
      border: 1px solid #6EC1E4;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }

    .system:hover,
    .module:hover,
    .submodule:hover,
    .section:hover {
      transform: translateX(6px);
      filter: brightness(1.1);
    }

    .tab:hover {
      background: #D4ECF9;
    }

    .hidden {
      display: none;
    }
  </style>
</head>

<body>

  <h2>ERP OFBiz Framework – Interactive Functional Hierarchy</h2>

  <div class="tree">
    <ul>
      <li>
        <span class="node system" onclick="toggle(this)">▶ Apache OFBiz</span>
        <ul class="hidden">
          <li>
            <span class="node module" onclick="toggle(this)">▶ Party</span>
            <ul class="hidden">
              <li>
                <span class="node submodule" onclick="toggle(this)">▶ Main</span>
                <ul class="hidden">
                  <li class="node tab">Profile</li>
                  <li class="node tab">References</li>
                  <li class="node tab">Roles</li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </div>

  <script>
    function toggle(el) {
      const next = el.nextElementSibling;
      if (!next) return;
      next.classList.toggle("hidden");
    }
  </script>

</body>
</html>"""

@app.route("/")
def home():
    return normal_function()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
