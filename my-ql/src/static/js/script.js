// import $ from "jquery"
document.getElementById("ql-editor").onfocus = () => {
	document.getElementById("actual-editor").focus();
}
document.getElementById("ql-editor").onkeydown = () => {
	document.getElementById("actual-editor").focus();
}
let waitingNode = [];
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
	waitingNode.forEach(el => {
		document.getElementsByClassName("ql-variable")[el.key].setAttribute("title", el.title);
	})
};
/**
 * @param {String} query MyQL query
 */
function highlightQuery(query) {
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

		let rem = other.trim().slice(1).trim().match(/([a-z]|[A-Z])+/)[0];

		if (!data.Query.properties.map(el => el.name == rem.match(/([a-z]|[A-Z])+/)[0]).includes(true))
			query = query.replace(rem, `<span class="ql-err" title="Error: No such query: ${rem}">${rem}</span>`);
		else
			data.Query.properties.map((el, i) => {
				if (el.name == rem.match(/([a-z]|[A-Z])+/)[0]) {
					query = query.replace(rem, `<span class="ql-variable">${rem}</span>`);
					waitingNode.push({ key: i, title: el.type.name });
				}
			})
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
			console.log(sym.charCodeAt(0));

			let spaceCount = sym.length - 1;
			let space = " ".repeat(spaceCount)
			query = query.replace(sym, `${space}<span class="ql-sym">${sym.trim()}</span>`);
		})
	}

	return query;
}
/**
 * @typedef {"null" | {name: String, type: String, additional: "null" | QlType }} QlType
 * @type { {Query: {properties: {name:String, parameters: QlType[], type: QlType}[]}, Mutation: {properties: {name:String, parameters: QlType[], type: QlType}[]}} }
 */
let data;
document.addEventListener("DOMContentLoaded", async () => {
	let res = await fetch("/types");
	data = await res.json();
	console.log(data);
})
