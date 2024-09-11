// import $ from "jquery"
document.getElementById("ql-editor").onfocus = () => {
	document.getElementById("actual-editor").focus();
}
document.getElementById("ql-editor").onkeydown = () => {
	document.getElementById("actual-editor").focus();
}
let variableNode = [];
/**
 * @param {KeyboardEvent} e
 */
document.getElementById("actual-editor").onkeydown = (e) => {
	if (e.key === "Tab") {
		e.preventDefault();
		/** @type {HTMLInputElement} */
		let editor = document.getElementById("actual-editor");
		let curpos = editor.selectionStart;
		document.getElementById("actual-editor").value = editor.value.slice(0, editor.selectionStart) + "    " + editor.value.slice(editor.selectionEnd);
		document.getElementById("actual-editor").selectionStart = curpos + 4;
		document.getElementById("actual-editor").selectionEnd = curpos + 4;
	}
	document.getElementById("ql-editor").innerHTML =
		highlightQuery(document.getElementById("actual-editor").value);
	variableNode.forEach(el => {
		let variable = document.createElement("span");
		variable.classList.add("variable-desc");
		variable.innerHTML = el.title;

		document.getElementsByClassName("ql-variable")[el.key].appendChild(variable);
		document.getElementsByClassName("ql-variable")[el.key].setAttribute("data-key", el.key);
	})
};
/**
 * @param {String} query MyQL query
 */
function highlightQuery(query) {
	variableNode = [];
	let varMatch = query.match(/^\$([a-z]|[A-Z])+:\s?([a-z]|[A-Z])+$/g);
	if (varMatch) {
		varMatch = query.match(/^\$([a-z]|[A-Z])+:\s?([a-z]|[A-Z])+$/g);
		varMatch.forEach(v => {
			query = query.replace(v, `<span class="ql-variable" title="${v.split(":")[1].trim()}>${v.split(":")[0].trim()}</span>`);
		})
	}

	let isQuery = query.includes("query");
	if (isQuery) {
		if (!query.includes("query")) return;
		let other = query.slice(query.indexOf("query") + 5);
		if (!other.match(/[a-z]|[A-Z]/)) return;

		let rem = other.trim().slice(1).trim().match(/([a-z]|[A-Z])+/g);

		if (!data.Query.properties.map(el => el.name == rem[0].match(/([a-z]|[A-Z])+/)[0]).includes(true))
			query = query.replace(rem, `<span class="ql-err" title="Error: No such query: ${rem}">${rem}</span>`);
		else {
			data.Query.properties.map((el, i) => {
				if (el.name == rem[0].match(/([a-z]|[A-Z])+/)[0]) {
					query = query.replace(el.name, `<span class="ql-variable">${el.name}</span>`);
					variableNode.push({ key: i, title: el.type.name });
					if (rem.slice(1).length > 0) {
						for (let i = 0; i < rem.slice(1).length; i++) {
							const element = rem.slice(1)[i];
							if (typeof el.type == "object") {
								let isFoundName = false;
								el.type.properties.map((el2, i) => {
									if (el2.name == element) {
										query = query.replace(element, `<span class="ql-variable">${element}</span>`);
										variableNode.push({ key: i + 1, title: el2.type });
										isFoundName = true;
									}
								})
								if (!isFoundName) {
									query = query.replace(element, `<span class="ql-err" title="Error: No such variable: ${element}">${element}</span>`);
								}
							}
						}
					}
				}
			});
		}
	}
	query = query.replace(/\n/g, '<br />');


	let keyMatch = query.match(/(query|mutation|Int|String|Boolean|Float|Array)/g);
	if (keyMatch) {
		keyMatch.forEach((key) => {
			query = query.replace(key, `<span class="ql-keyword">${key}</span>`);
		})
	} else if (query.match(/\s([a-z]|[A-Z])+\s/g)) {
		query.match(/\s([a-z]|[A-Z])+\s/g).forEach(el => {
			query = query.replace(el.slice(1, -1), `<span class="ql-variable">${el.slice(1, -1)}</span>`);
		})
	}
	let spaces = query.match(/    /g)
	if (spaces)
		spaces.forEach((space) => {
			query = query.replace(space, `&nbsp;&nbsp;&nbsp;&nbsp;`);
		})


	let symMatch = query.match(/(\s|\s+|\n)?(\(|\)|\{|\})/g);

	if (symMatch) {
		symMatch.forEach((sym) => {

			let spaceCount = sym.length - 1;
			let space = " ".repeat(spaceCount)
			query = query.replace(sym, `${space}<span class="ql-sym">${sym.trim()}</span>`);
		})
	}

	return query;
}
/**
 * @typedef {{name: String, type: String, additional: "null" | String}} QlProperty
 * @typedef {"null" | {name: String, properties: QlProperty[], additional: "null" | QlType }} QlType
 * @type { {Query: {properties: {name:String, parameters: QlType[], type: QlType}[]}, Mutation: {properties: {name:String, parameters: QlType[], type: QlType}[]}} }
 */
let data;
document.addEventListener("DOMContentLoaded", async () => {
	let res = await fetch("/types");
	data = await res.json();
	console.log(data);
})
