--
-- PostgreSQL database dump
--

-- Dumped from database version 16rc1
-- Dumped by pg_dump version 16rc1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dict; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dict (
    id integer NOT NULL,
    word text NOT NULL,
    translation text NOT NULL,
    context text,
    CONSTRAINT dict_translation_check CHECK ((translation ~* '^[a-zA-Z├í├®├¡├│├║├╝├ü├ë├ì├ô├Ü├£├▒├æ├ñ├Â├╝├ƒ├ä├û├£ ]+$'::text)),
    CONSTRAINT dict_word_check CHECK ((word ~* '^[a-zA-Z├í├®├¡├│├║├╝├ü├ë├ì├ô├Ü├£├▒├æ├ñ├Â├╝├ƒ├ä├û├£]+$'::text))
);


ALTER TABLE public.dict OWNER TO postgres;

--
-- Name: dict_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dict_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.dict_id_seq OWNER TO postgres;

--
-- Name: dict_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dict_id_seq OWNED BY public.dict.id;


--
-- Name: dict id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dict ALTER COLUMN id SET DEFAULT nextval('public.dict_id_seq'::regclass);


--
-- Name: dict dict_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dict
    ADD CONSTRAINT dict_pkey PRIMARY KEY (id);


--
-- Name: dict dict_word_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dict
    ADD CONSTRAINT dict_word_key UNIQUE (word);


--
-- PostgreSQL database dump complete
--

