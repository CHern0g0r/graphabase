// Generated from /home/chernogor/Workspace/Python/graphabase/src/antlr_parser/Gram.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GramParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DIV=1, CONNECT=2, TO=3, LIST=4, SELECT=5, FROM=6, WHERE=7, COUNT=8, EXISTS=9, 
		L=10, R=11, PAR=12, SUB=13, RARR=14, UNDERLINE=15, DOT=16, ID=17, EQ=18, 
		ALT=19, STAR=20, PLUS=21, QUEST=22, STRING=23, IDENT=24, INT=25, NT=26, 
		WS=27;
	public static final int
		RULE_full_script = 0, RULE_script = 1, RULE_statement = 2, RULE_select = 3, 
		RULE_obj = 4, RULE_unit = 5, RULE_where_expr = 6, RULE_vert_expr = 7, 
		RULE_named_pattern = 8, RULE_pattern = 9, RULE_alt = 10, RULE_seq = 11, 
		RULE_subseq = 12, RULE_scoped = 13;
	public static final String[] ruleNames = {
		"full_script", "script", "statement", "select", "obj", "unit", "where_expr", 
		"vert_expr", "named_pattern", "pattern", "alt", "seq", "subseq", "scoped"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "';'", "'connect'", "'to'", "'list'", "'select'", "'from'", "'where'", 
		"'count'", "'exists'", "'('", "')'", "','", "'-'", "'->'", "'_'", "'.'", 
		"'id'", "'='", "'|'", "'*'", "'+'", "'?'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "DIV", "CONNECT", "TO", "LIST", "SELECT", "FROM", "WHERE", "COUNT", 
		"EXISTS", "L", "R", "PAR", "SUB", "RARR", "UNDERLINE", "DOT", "ID", "EQ", 
		"ALT", "STAR", "PLUS", "QUEST", "STRING", "IDENT", "INT", "NT", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Gram.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GramParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class Full_scriptContext extends ParserRuleContext {
		public ScriptContext script() {
			return getRuleContext(ScriptContext.class,0);
		}
		public TerminalNode EOF() { return getToken(GramParser.EOF, 0); }
		public Full_scriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_full_script; }
	}

	public final Full_scriptContext full_script() throws RecognitionException {
		Full_scriptContext _localctx = new Full_scriptContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_full_script);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			script();
			setState(29);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ScriptContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode DIV() { return getToken(GramParser.DIV, 0); }
		public ScriptContext script() {
			return getRuleContext(ScriptContext.class,0);
		}
		public ScriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_script; }
	}

	public final ScriptContext script() throws RecognitionException {
		ScriptContext _localctx = new ScriptContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_script);
		try {
			setState(36);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CONNECT:
			case LIST:
			case SELECT:
			case NT:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				statement();
				setState(32);
				match(DIV);
				setState(33);
				script();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public TerminalNode CONNECT() { return getToken(GramParser.CONNECT, 0); }
		public TerminalNode TO() { return getToken(GramParser.TO, 0); }
		public TerminalNode STRING() { return getToken(GramParser.STRING, 0); }
		public TerminalNode LIST() { return getToken(GramParser.LIST, 0); }
		public SelectContext select() {
			return getRuleContext(SelectContext.class,0);
		}
		public Named_patternContext named_pattern() {
			return getRuleContext(Named_patternContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CONNECT:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				match(CONNECT);
				setState(39);
				match(TO);
				setState(40);
				match(STRING);
				}
				break;
			case LIST:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				match(LIST);
				}
				break;
			case SELECT:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				select();
				}
				break;
			case NT:
				enterOuterAlt(_localctx, 4);
				{
				setState(43);
				named_pattern();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectContext extends ParserRuleContext {
		public TerminalNode SELECT() { return getToken(GramParser.SELECT, 0); }
		public ObjContext obj() {
			return getRuleContext(ObjContext.class,0);
		}
		public TerminalNode FROM() { return getToken(GramParser.FROM, 0); }
		public TerminalNode STRING() { return getToken(GramParser.STRING, 0); }
		public TerminalNode WHERE() { return getToken(GramParser.WHERE, 0); }
		public Where_exprContext where_expr() {
			return getRuleContext(Where_exprContext.class,0);
		}
		public SelectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_select; }
	}

	public final SelectContext select() throws RecognitionException {
		SelectContext _localctx = new SelectContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_select);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(SELECT);
			setState(47);
			obj();
			setState(48);
			match(FROM);
			setState(49);
			match(STRING);
			setState(50);
			match(WHERE);
			setState(51);
			where_expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObjContext extends ParserRuleContext {
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public TerminalNode COUNT() { return getToken(GramParser.COUNT, 0); }
		public TerminalNode EXISTS() { return getToken(GramParser.EXISTS, 0); }
		public ObjContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_obj; }
	}

	public final ObjContext obj() throws RecognitionException {
		ObjContext _localctx = new ObjContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_obj);
		try {
			setState(58);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case L:
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				unit();
				}
				break;
			case COUNT:
				enterOuterAlt(_localctx, 2);
				{
				setState(54);
				match(COUNT);
				setState(55);
				unit();
				}
				break;
			case EXISTS:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				match(EXISTS);
				setState(57);
				unit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnitContext extends ParserRuleContext {
		public TerminalNode L() { return getToken(GramParser.L, 0); }
		public List<TerminalNode> IDENT() { return getTokens(GramParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(GramParser.IDENT, i);
		}
		public TerminalNode PAR() { return getToken(GramParser.PAR, 0); }
		public TerminalNode R() { return getToken(GramParser.R, 0); }
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_unit);
		try {
			setState(66);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case L:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				match(L);
				setState(61);
				match(IDENT);
				setState(62);
				match(PAR);
				setState(63);
				match(IDENT);
				setState(64);
				match(R);
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(65);
				match(IDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Where_exprContext extends ParserRuleContext {
		public List<TerminalNode> L() { return getTokens(GramParser.L); }
		public TerminalNode L(int i) {
			return getToken(GramParser.L, i);
		}
		public List<Vert_exprContext> vert_expr() {
			return getRuleContexts(Vert_exprContext.class);
		}
		public Vert_exprContext vert_expr(int i) {
			return getRuleContext(Vert_exprContext.class,i);
		}
		public List<TerminalNode> R() { return getTokens(GramParser.R); }
		public TerminalNode R(int i) {
			return getToken(GramParser.R, i);
		}
		public TerminalNode SUB() { return getToken(GramParser.SUB, 0); }
		public PatternContext pattern() {
			return getRuleContext(PatternContext.class,0);
		}
		public TerminalNode RARR() { return getToken(GramParser.RARR, 0); }
		public Where_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_expr; }
	}

	public final Where_exprContext where_expr() throws RecognitionException {
		Where_exprContext _localctx = new Where_exprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_where_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(L);
			setState(69);
			vert_expr();
			setState(70);
			match(R);
			setState(71);
			match(SUB);
			setState(72);
			pattern();
			setState(73);
			match(RARR);
			setState(74);
			match(L);
			setState(75);
			vert_expr();
			setState(76);
			match(R);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vert_exprContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(GramParser.IDENT, 0); }
		public TerminalNode UNDERLINE() { return getToken(GramParser.UNDERLINE, 0); }
		public TerminalNode DOT() { return getToken(GramParser.DOT, 0); }
		public TerminalNode ID() { return getToken(GramParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GramParser.EQ, 0); }
		public TerminalNode INT() { return getToken(GramParser.INT, 0); }
		public Vert_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vert_expr; }
	}

	public final Vert_exprContext vert_expr() throws RecognitionException {
		Vert_exprContext _localctx = new Vert_exprContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_vert_expr);
		try {
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				match(IDENT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				match(UNDERLINE);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(80);
				match(IDENT);
				setState(81);
				match(DOT);
				setState(82);
				match(ID);
				setState(83);
				match(EQ);
				setState(84);
				match(INT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Named_patternContext extends ParserRuleContext {
		public TerminalNode NT() { return getToken(GramParser.NT, 0); }
		public TerminalNode EQ() { return getToken(GramParser.EQ, 0); }
		public PatternContext pattern() {
			return getRuleContext(PatternContext.class,0);
		}
		public Named_patternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_named_pattern; }
	}

	public final Named_patternContext named_pattern() throws RecognitionException {
		Named_patternContext _localctx = new Named_patternContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_named_pattern);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(NT);
			setState(88);
			match(EQ);
			setState(89);
			pattern();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PatternContext extends ParserRuleContext {
		public AltContext alt() {
			return getRuleContext(AltContext.class,0);
		}
		public TerminalNode ALT() { return getToken(GramParser.ALT, 0); }
		public PatternContext pattern() {
			return getRuleContext(PatternContext.class,0);
		}
		public PatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pattern; }
	}

	public final PatternContext pattern() throws RecognitionException {
		PatternContext _localctx = new PatternContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_pattern);
		try {
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(91);
				alt();
				setState(92);
				match(ALT);
				setState(93);
				pattern();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				alt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AltContext extends ParserRuleContext {
		public SeqContext seq() {
			return getRuleContext(SeqContext.class,0);
		}
		public TerminalNode L() { return getToken(GramParser.L, 0); }
		public TerminalNode R() { return getToken(GramParser.R, 0); }
		public AltContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alt; }
	}

	public final AltContext alt() throws RecognitionException {
		AltContext _localctx = new AltContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_alt);
		try {
			setState(101);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				seq();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				match(L);
				setState(100);
				match(R);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SeqContext extends ParserRuleContext {
		public SubseqContext subseq() {
			return getRuleContext(SubseqContext.class,0);
		}
		public SeqContext seq() {
			return getRuleContext(SeqContext.class,0);
		}
		public SeqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seq; }
	}

	public final SeqContext seq() throws RecognitionException {
		SeqContext _localctx = new SeqContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_seq);
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				subseq();
				setState(104);
				seq();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				subseq();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubseqContext extends ParserRuleContext {
		public ScopedContext scoped() {
			return getRuleContext(ScopedContext.class,0);
		}
		public TerminalNode STAR() { return getToken(GramParser.STAR, 0); }
		public TerminalNode PLUS() { return getToken(GramParser.PLUS, 0); }
		public TerminalNode QUEST() { return getToken(GramParser.QUEST, 0); }
		public SubseqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subseq; }
	}

	public final SubseqContext subseq() throws RecognitionException {
		SubseqContext _localctx = new SubseqContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_subseq);
		try {
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				scoped();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				scoped();
				setState(111);
				match(STAR);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(113);
				scoped();
				setState(114);
				match(PLUS);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(116);
				scoped();
				setState(117);
				match(QUEST);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ScopedContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(GramParser.IDENT, 0); }
		public TerminalNode NT() { return getToken(GramParser.NT, 0); }
		public TerminalNode L() { return getToken(GramParser.L, 0); }
		public PatternContext pattern() {
			return getRuleContext(PatternContext.class,0);
		}
		public TerminalNode R() { return getToken(GramParser.R, 0); }
		public ScopedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scoped; }
	}

	public final ScopedContext scoped() throws RecognitionException {
		ScopedContext _localctx = new ScopedContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_scoped);
		try {
			setState(127);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(121);
				match(IDENT);
				}
				break;
			case NT:
				enterOuterAlt(_localctx, 2);
				{
				setState(122);
				match(NT);
				}
				break;
			case L:
				enterOuterAlt(_localctx, 3);
				{
				setState(123);
				match(L);
				setState(124);
				pattern();
				setState(125);
				match(R);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35\u0084\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\3\3\3"+
		"\3\3\5\3\'\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6=\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7E\n\7\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t"+
		"X\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13c\n\13\3\f\3\f\3\f"+
		"\5\fh\n\f\3\r\3\r\3\r\3\r\5\rn\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\5\16z\n\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0082\n"+
		"\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2\u0086\2\36\3"+
		"\2\2\2\4&\3\2\2\2\6.\3\2\2\2\b\60\3\2\2\2\n<\3\2\2\2\fD\3\2\2\2\16F\3"+
		"\2\2\2\20W\3\2\2\2\22Y\3\2\2\2\24b\3\2\2\2\26g\3\2\2\2\30m\3\2\2\2\32"+
		"y\3\2\2\2\34\u0081\3\2\2\2\36\37\5\4\3\2\37 \7\2\2\3 \3\3\2\2\2!\"\5\6"+
		"\4\2\"#\7\3\2\2#$\5\4\3\2$\'\3\2\2\2%\'\3\2\2\2&!\3\2\2\2&%\3\2\2\2\'"+
		"\5\3\2\2\2()\7\4\2\2)*\7\5\2\2*/\7\31\2\2+/\7\6\2\2,/\5\b\5\2-/\5\22\n"+
		"\2.(\3\2\2\2.+\3\2\2\2.,\3\2\2\2.-\3\2\2\2/\7\3\2\2\2\60\61\7\7\2\2\61"+
		"\62\5\n\6\2\62\63\7\b\2\2\63\64\7\31\2\2\64\65\7\t\2\2\65\66\5\16\b\2"+
		"\66\t\3\2\2\2\67=\5\f\7\289\7\n\2\29=\5\f\7\2:;\7\13\2\2;=\5\f\7\2<\67"+
		"\3\2\2\2<8\3\2\2\2<:\3\2\2\2=\13\3\2\2\2>?\7\f\2\2?@\7\32\2\2@A\7\16\2"+
		"\2AB\7\32\2\2BE\7\r\2\2CE\7\32\2\2D>\3\2\2\2DC\3\2\2\2E\r\3\2\2\2FG\7"+
		"\f\2\2GH\5\20\t\2HI\7\r\2\2IJ\7\17\2\2JK\5\24\13\2KL\7\20\2\2LM\7\f\2"+
		"\2MN\5\20\t\2NO\7\r\2\2O\17\3\2\2\2PX\7\32\2\2QX\7\21\2\2RS\7\32\2\2S"+
		"T\7\22\2\2TU\7\23\2\2UV\7\24\2\2VX\7\33\2\2WP\3\2\2\2WQ\3\2\2\2WR\3\2"+
		"\2\2X\21\3\2\2\2YZ\7\34\2\2Z[\7\24\2\2[\\\5\24\13\2\\\23\3\2\2\2]^\5\26"+
		"\f\2^_\7\25\2\2_`\5\24\13\2`c\3\2\2\2ac\5\26\f\2b]\3\2\2\2ba\3\2\2\2c"+
		"\25\3\2\2\2dh\5\30\r\2ef\7\f\2\2fh\7\r\2\2gd\3\2\2\2ge\3\2\2\2h\27\3\2"+
		"\2\2ij\5\32\16\2jk\5\30\r\2kn\3\2\2\2ln\5\32\16\2mi\3\2\2\2ml\3\2\2\2"+
		"n\31\3\2\2\2oz\5\34\17\2pq\5\34\17\2qr\7\26\2\2rz\3\2\2\2st\5\34\17\2"+
		"tu\7\27\2\2uz\3\2\2\2vw\5\34\17\2wx\7\30\2\2xz\3\2\2\2yo\3\2\2\2yp\3\2"+
		"\2\2ys\3\2\2\2yv\3\2\2\2z\33\3\2\2\2{\u0082\7\32\2\2|\u0082\7\34\2\2}"+
		"~\7\f\2\2~\177\5\24\13\2\177\u0080\7\r\2\2\u0080\u0082\3\2\2\2\u0081{"+
		"\3\2\2\2\u0081|\3\2\2\2\u0081}\3\2\2\2\u0082\35\3\2\2\2\f&.<DWbgmy\u0081";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}