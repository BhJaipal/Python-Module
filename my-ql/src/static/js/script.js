let variableNode = [];
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
		let other = query.slice(query.indexOf("query") + 5);
		if (other.match(/[a-z]|[A-Z]/)) {

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
	}
	isQuery = query.includes("mutation");
	if (isQuery) {
		let other = query.slice(query.indexOf("mutation") + 8);
		if (other.match(/[a-z]|[A-Z]/)) {

			let rem = other.trim().slice(1).trim().match(/([a-z]|[A-Z])+/g);

			if (!data.Mutation.properties.map(el => el.name == rem[0].match(/([a-z]|[A-Z])+/)[0]).includes(true))
				query = query.replace(rem, `<span class="ql-err" title="Error: No such query: ${rem}">${rem}</span>`);
			else {
				data.Mutation.properties.map((el, i) => {
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
	}
	query = query.replace(/\n/g, '<br />');


	let keyMatch = query.match(/(query|mutation|Int|String|Boolean|Float|Array)/g);
	if (keyMatch) {
		keyMatch.forEach((key) => {
			query = query.replace(key, `<span class="ql-keyword">${key}</span>`);
			console.log(query);

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
		symMatch.forEach((sym, i) => {
			let spaceCount = sym.length - 1;
			let space = " ".repeat(spaceCount)
			if (symMatch.indexOf(sym) != symMatch.lastIndexOf(sym)) {
				query = query.slice(0, query.lastIndexOf(sym)) + query.slice(query.lastIndexOf(sym)).replace(sym, `${space}<span class="ql-sym">${sym.trim()}</span>`);
			}
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
const { createApp, ref, watch } = Vue

createApp({
	setup() {
		/**
		 * @typedef {<T>{value: T}} Ref
		 * @type {Ref<string>}
		 */
		const queryInput = ref("");
		/**
		 * @type {Ref<string>}
		 */
		let htmlOut = ref("");

		watch(queryInput, () => {
			htmlOut.value = highlightQuery(queryInput.value);
			setTimeout(() => {

				variableNode.forEach(el => {
					let variable = document.createElement("span");
					variable.classList.add("variable-desc");
					variable.innerHTML = el.title;

					document.getElementsByClassName("ql-variable")[el.key].appendChild(variable);
					document.getElementsByClassName("ql-variable")[el.key].setAttribute("data-key", el.key);
				})
			}, 1000);
		})
		// let icon = ref("send")
		return {
			queryInput,
			htmlOut,
			icon: "send",
			sendDisabled: false
		}
	},
	methods: {
		/** @param {KeyboardEvent} e */
		onkd(e) {
			if (e.key === "Tab") {
				e.preventDefault();
				/** @type {HTMLInputElement} */
				let editor = document.getElementById("actual-editor");
				let curpos = editor.selectionStart;
				document.getElementById("actual-editor").value = editor.value.slice(0, editor.selectionStart) + "    " + editor.value.slice(editor.selectionEnd);
				document.getElementById("actual-editor").selectionStart = curpos + 4;
				document.getElementById("actual-editor").selectionEnd = curpos + 4;
			}
		},

		sendData() {
			this.sendDisabled = true;
			console.log("Sending data", this.sendDisabled);
			document.getElementById("send-data").setAttribute("disabled", this.sendDisabled);
			this.icon = "refresh";
			setTimeout(() => {
				this.icon = "send";
				this.sendDisabled = false;
				console.log("done", this.sendDisabled);
				document.getElementById("send-data").removeAttribute("disabled");
			}, 3000);
		}
	}
}).mount('#app')