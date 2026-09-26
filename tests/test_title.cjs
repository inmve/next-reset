const {test} = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
function setup(reduced = false) {
  const listeners = {}, documentListeners = {}, timers = new Map();
  const code = {textContent:'first'};
  const button = {disabled:true, querySelector:()=>code, addEventListener:(name,fn)=>{listeners[name]=fn;}};
  const root = {querySelectorAll:()=>[], querySelector:()=>button};
  const strings = {shellTitle:'first',shellTitleWatch:'second',shellTitleLog:'third'};
  const document = {hidden:false, getElementById:id=>id==='reset-zen'?root:{textContent:JSON.stringify({strings,cards:[],config:{}})}, querySelector:()=>({}), addEventListener:(name,fn)=>{documentListeners[name]=fn;}};
  let id=0;
  vm.runInNewContext(fs.readFileSync('src/site.js','utf8'), {document,window:{matchMedia:()=>({matches:reduced,addEventListener:()=>{}})},Date,URLSearchParams,setInterval:(fn,ms)=>{timers.set(++id,{fn,ms});return id;},clearInterval:id=>timers.delete(id)});
  return {code,button,listeners,document,documentListeners,timers};
}
test('headline chooses a variant on load and wraps through variants on click without a timer',()=>{
  const s=setup();
  assert.equal(s.button.disabled,false);
  assert.ok(['first','second','third'].includes(s.code.textContent));
  const initial=s.code.textContent;
  s.listeners.click(); assert.notEqual(s.code.textContent,initial);
  s.listeners.click(); s.listeners.click(); assert.equal(s.code.textContent,initial);
  assert.equal([...s.timers.values()].some(t=>t.ms!==60000),false);
});
test('manual switching works with reduced motion',()=>{
  const s=setup(true);
  const initial=s.code.textContent;
  s.listeners.click(); assert.notEqual(s.code.textContent,initial);
});
